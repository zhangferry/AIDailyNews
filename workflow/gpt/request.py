import json, os
from google import genai
from openai import OpenAI
from loguru import logger


class AIProvider:
    name: str
    api_key: str
    model: str
    base_url: str

    def __init__(self, name: str, api_key: str, model: str, base_url: str):
        self.name = name
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

    @staticmethod
    def build_from_envs():
        name = os.environ.get("AI_PROVIDER", "gemini")

        api_key = os.environ.get("GPT_API_KEY")
        if not api_key:
            raise ValueError("ai provider api key is empty!")
        model = os.environ.get("GPT_MODEL_NAME", "gpt-3.5-turbo" if name == "openai" else "gemini-pro")
        base_url = os.environ.get("GPT_BASE_URL", "https://api.openai.com")

        # update config.json
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # workflow folder
        project_root = os.path.dirname(current_directory)
        config_file = f"{project_root}/../src/config/config.json"
        with open(config_file, "r") as file:
            config_content = json.load(file)
        config_content["aiprovider_name"] = name
        config_content["aiprovider_model"] = model
        with open(config_file, "w") as file:
            json.dump(config_content, file, indent=4)

        return AIProvider(name=name, api_key=api_key, model=model, base_url=base_url)

    def request(self, prompt, content):
        try:
            if self.name == "openai":
                result = request_openai(provider=self, prompt=prompt, content=content)
            else:
                result = request_gemini(provider=self, prompt=prompt, content=content)
            logger.info(f"{self.name} response: {result}")
            return result
        except Exception as e:
            logger.error(f"request {self.name} failed: {e}")
            return None

def request_gemini(provider: AIProvider, prompt, content):
    """
    https://ai.google.dev/gemini-api/docs
    """
    input_text = f"{prompt}: {content}"

    genai.configure(api_key=provider.api_key)
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
    model = genai.GenerativeModel(model_name=provider.model,
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    response = model.generate_content([input_text])
    return response.text

def request_openai(provider: AIProvider, prompt, content):
    """
    https://platform.openai.com/docs/guides/text-generation
    """
    client = OpenAI(api_key=provider.api_key,
                    base_url=provider.base_url)

    chat_completion = client.chat.completions.create(messages=[
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": content
        }
    ], model=provider.model)
    return chat_completion.choices[0].message.content
