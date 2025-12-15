import os
import json
import getpass
from pathlib import Path
from typing import List, Any, Dict
from openai import OpenAI

BASE_URL = "https://api.moonshot.cn/v1"

def get_api_key():
    """
    尝试多种方式获取 API Key
    """
    api_key = os.getenv("MOONSHOT_API_KEY")
    if api_key:
        return api_key

    try:
        config_path = Path.home() / ".kimi" / "config.json"
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
                if "llm" in config and "api_key" in config["llm"]:
                     return config["llm"]["api_key"]
    except Exception:
        pass

    print("\033[33m[Warning] MOONSHOT_API_KEY not found in environment variables.\033[0m")
    api_key = getpass.getpass("Please enter your Moonshot API Key: ")
    if not api_key:
        raise ValueError("API Key is required to run Mini Kimi.")
    return api_key

class LLMClient:
    """
    简化的 LLM 客户端。
    """
    def __init__(self):
        self.api_key = get_api_key()
        self.client = OpenAI(api_key=self.api_key, base_url=BASE_URL)
        self.model = "kimi-k2-thinking" 

    def chat(self, messages: List[Dict[str, Any]], tools: List[Any] = None):
        api_tools = [t.schema for t in tools] if tools else None
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=api_tools,
                temperature=0.3
            )
            return response.choices[0].message
        except Exception as e:
            print(f"\033[31m[Error] LLM Call Failed: {e}\033[0m")
            raise e

