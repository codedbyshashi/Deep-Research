# config.py

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel


# Load .env from the project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)


# API keys
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")


# OpenRouter client
openrouter_client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_api_key,
)


# Gemini client
gemini_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=gemini_api_key,
)


# Models
openrouter_model = OpenAIChatCompletionsModel(
    openai_client=openrouter_client,
    model="openrouter/free",
)


gemini_model = OpenAIChatCompletionsModel(
    openai_client=gemini_client,
    model="gemini-3.5-flash-lite",
)


deepseek_model = OpenAIChatCompletionsModel(
    openai_client=openrouter_client,
    model="deepseek/deepseek-chat-v3.1:free",
)


# Application settings
USE_EMAIL = True
HOW_MANY_SEARCHES = 5