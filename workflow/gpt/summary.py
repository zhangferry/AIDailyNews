import os
import google.generativeai as genai
from openai import OpenAI
import workflow.gpt.prompt as prompt_template
from dotenv import load_dotenv


def request_gpt(content):
    load_dotenv()
    prompt = prompt_template.structured_prompt
    if os.environ.get("AI_PROVIDER") == "gemini":
        return request_gemini(prompt=prompt, content=content)
    else:
        return request_openai(prompt=prompt, content=content)


def request_gemini(prompt, content):
    input_text = f"{prompt}: ```{content}```"

    api_key = os.environ.get("GPT_API_KEY")
    if not api_key:
        raise ValueError("gemini key is empty")

    genai.configure(api_key=api_key)
    # Set up the model
    generation_config = genai.GenerationConfig(temperature=0.2,
                                               max_output_tokens=512)

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]
    model = genai.GenerativeModel(model_name='gemini-pro',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    try:
        response = model.generate_content([input_text])
        print(response.text)
        return response.text
    except Exception as e:
        # 兜底
        if os.environ.get("RETRY_MODE") == "openai":
            print(f"request gemini failed: {e}, retry with openai")
            response = request_openai(prompt, content)
            return response
        else:
            print(f"request gemini failed: {e}, skip")
            return None


def request_openai(prompt, content):
    try:
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"],
                        base_url=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com"))

        chat_completion = client.chat.completions.create(messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": content
            }
        ], model="gpt-3.5-turbo")
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"request openai failed: {e}")
