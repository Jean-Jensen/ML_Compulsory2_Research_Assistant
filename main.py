from pydantic_ai import Agent, capture_run_messages
import os
import asyncio


base_url = os.getenv("LLM_BASE_URL", "https://api.groq.com/openai/v1")
model = os.getenv("LLM_MODEL", "groq:qwen/qwen3.8-27b")
api_key = os.getenv("GROQ_API_KEY", "")

async def run_agent(prompt: str):
    print("running agent")
    agent = Agent(model, retries=0)
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
        elif text == "do the thing":
            result = asyncio.run(run_agent("output one short sentence describing what you do"))
            print(result)



if __name__ == "__main__":
    main()