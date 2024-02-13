import os
import google.generativeai as genai
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
    # Initialize Vertex AI
    input_text = f"{prompt}: ```{content}```"

    api_key = os.environ.get("GPT_API_KEY")
    if not api_key:
        raise ValueError("gemini key is empty")

    genai.configure(api_key=api_key)
    # Set up the model
    generation_config = genai.GenerationConfig(temperature=0.2)

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

    response = model.generate_content([input_text])
    print(response.text)
    return response.text


def request_openai(prompt, content):
    raise RuntimeError("openai provider is not support")
