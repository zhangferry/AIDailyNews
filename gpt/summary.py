import google.generativeai as genai
import gpt.prompt as prompt
from environs import Env


def request_gpt(content):
    return request_gemini(prompt=prompt.structured_prompt, content=content)


def request_gemini(prompt, content):
    # Initialize Vertex AI
    env = Env()
    env.read_env()
    input_text = f"{prompt}: ```{content}```"

    api_key = env("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("gemini key is empty")

    genai.configure(api_key=api_key)
    # Set up the model
    generation_config = genai.GenerationConfig(temperature=0.3)

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
    return response.text
