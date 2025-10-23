import os

# LLM Settings
LLM_MODE = os.getenv("LLM_MODE", "light")

LLM_CONFIG = {
    "light": {
        "model": "llama3:8b",
        "api_base": "http://localhost:11434/api/generate",
        "type": "ollama"
    },
    "heavy": {
        "model": "gpt-4o",
        "api_key": os.getenv("OPENAI_API_KEY"),
        "type": "gpt"
    }
}