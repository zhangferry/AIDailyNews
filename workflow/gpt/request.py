import json, os, threading
import httpx
from google import genai
from openai import OpenAI
from loguru import logger

# 全局 HTTP 客户端复用连接
_global_httpx_client = None
_config_file_lock = threading.Lock()

def get_httpx_client():
    """获取全局 httpx 客户端"""
    global _global_httpx_client
    if _global_httpx_client is None:
        proxy_url = os.environ.get("https_proxy") or os.environ.get("http_proxy")
        if proxy_url:
            _global_httpx_client = httpx.Client(proxy=proxy_url)
        else:
            _global_httpx_client = httpx.Client()
    return _global_httpx_client


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
        sync_runtime_config(name=name, model=model)

        return AIProvider(name=name, api_key=api_key, model=model, base_url=base_url)

    def request(self, prompt, content):
        try:
            if self.name == "openai":
                result = request_openai(provider=self, prompt=prompt, content=content)
            else:
                result = request_gemini(provider=self, prompt=prompt, content=content)
            # 只记录响应状态，避免泄露敏感内容
            response_preview = result[:100] + "..." if result and len(result) > 100 else result
            logger.info(f"{self.name} 请求成功，响应预览: {response_preview}")
            return result
        except Exception as e:
            logger.error(f"request {self.name} failed: {e}")
            return None

def request_gemini(provider: AIProvider, prompt, content):
    """
    https://ai.google.dev/gemini-api/docs
    """
    input_text = f"{prompt}: {content}"

    client = genai.Client(api_key=provider.api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=input_text)
    return response.text

def request_openai(provider: AIProvider, prompt, content):
    """
    https://platform.openai.com/docs/guides/text-generation
    """
    http_client = get_httpx_client()

    client = OpenAI(api_key=provider.api_key,
                    base_url=provider.base_url,
                    http_client=http_client)

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


def sync_runtime_config(name: str, model: str):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_directory)
    config_file = f"{project_root}/../src/config/config.json"

    with _config_file_lock:
        config_content = {}
        if os.path.exists(config_file):
            try:
                with open(config_file, "r") as file:
                    raw_content = file.read().strip()
                if raw_content:
                    config_content = json.loads(raw_content)
            except Exception as e:
                logger.warning(f"sync config read failed: {e}")

        config_content["aiprovider_name"] = name
        config_content["aiprovider_model"] = model

        temp_file = f"{config_file}.tmp"
        try:
            with open(temp_file, "w") as file:
                json.dump(config_content, file, indent=4)
            os.replace(temp_file, config_file)
        except Exception as e:
            logger.warning(f"sync config write failed: {e}")
            if os.path.exists(temp_file):
                os.remove(temp_file)
