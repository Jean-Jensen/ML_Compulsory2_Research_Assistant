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
            "Call search_papers for every paper request. Use short topic keywords. "
            "Choose one returned record that meets the user's constraints. "
            "Use that record's title, authors, year, and exact citation count. "
            "Cite OpenAlex using that record's URL. If the citation count is missing, say it is unavailable. "
            "If none of the results qualify, say so."
        ),
    )
    with capture_run_messages() as captured:
        try:
            result = await agent.run(prompt)
        except Exception as error:
            error.model_messages=list(captured)
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
