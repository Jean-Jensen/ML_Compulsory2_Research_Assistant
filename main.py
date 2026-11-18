
from pydantic_ai import Agent, capture_run_messages
import os
import asyncio

from dotenv import load_dotenv
from paper_search import PaperSearchError, search_papers


load_dotenv()

base_url = os.getenv("LLM_BASE_URL", "https://api.groq.com/openai/v1")
model = os.getenv("LLM_MODEL", "groq:qwen/qwen3.8-27b")
api_key = os.getenv("GROQ_API_KEY", "")


async def run_agent(prompt: str):
    print("running agent")

    agent = Agent(
        model,
        retries=0,
        tools=[search_papers],
        instructions=(
            "You are an AI research assistant. "

            "Call search_papers for every paper request. "

            "Identify the research topic, requested publication year "
            "and year condition (before, after, or exact), "
            "and any minimum or maximum citation count. "
            "Pass the year and year_operator arguments when a year "
            "requirement is specified. "
            "Use 'before' for papers published before the requested year, "
            "'after' for papers published after the requested year, "
            "and 'exact' for papers published in the requested year. "
            "Pass min_citations and max_citations when citation limits "
            "are specified. "

            "Use the information returned by search_papers. "
            "Choose one returned record that meets the user's constraints. "

            "Include the title, authors, publication year, citation count, "
            "citation source, paper URL, and an explanation of why "
            "the paper matches the request. "

            "Use the exact citation count returned by OpenAlex. "
            "If the citation count is missing, say it is unavailable. "

            "If none of the returned papers qualify, clearly say "
            "that no matching paper was found. "
            "Do not present a paper that fails the user's constraints."
        ),
    )

    with capture_run_messages() as captured:
        try:
            result = await agent.run(prompt)
        except Exception as error:
            error.model_messages = list(captured)
            raise

    return result.output


def main():
    while True:
        try:
            text = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if text == "haii":
            print("hello beautiful ;)")
        elif text:
            try:
                print(asyncio.run(run_agent(text)))
            except PaperSearchError as error:
                print(error)


if __name__ == "__main__":
    main()
