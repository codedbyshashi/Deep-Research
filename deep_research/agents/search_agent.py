from agents import Agent, ModelSettings, function_tool
from dotenv import load_dotenv
from tavily import TavilyClient
import os
from config import gemini_model, groq_model, nvidia_model2, openrouter_model
load_dotenv(override=True)

# Tavily client
tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


# Web search tool
@function_tool
def web_search(query: str) -> str:
    response = tavily_client.search(
        query=query,
        max_results=5,
        search_depth="advanced"
    )

    results = []

    for result in response["results"]:
        results.append(
            f"Title: {result['title']}\n"
            f"URL: {result['url']}\n"
            f"Content: {result['content']}\n"
        )

    return "\n\n".join(results)


# Agent instructions
INSTRUCTIONS = """
You are a research assistant. Given a search term, you search the web for that term and
produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 words.

Capture the main points and be succinct. Reply only with the summary.
"""


# Force the agent to use a tool
settings = ModelSettings(
    tool_choice="required"
)


# Search agent
search_agent = Agent(
    name="search_agent",
    instructions=INSTRUCTIONS,
    model=nvidia_model2,
    tools=[web_search],
    model_settings=settings
)