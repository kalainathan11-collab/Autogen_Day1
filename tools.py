import asyncio
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent

# Load environment variables
load_dotenv()

# Initialize model client
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

# Define tool function with clean type hints and docstring
def add(a: int, b: int) -> int:
    """Adds two integers and returns the sum."""
    return a + b

# Create Assistant Agent with tool attached
math_agent = AssistantAgent(
    name="math_agent",
    model_client=model_client,
    tools=[add],
    reflect_on_tool_use=True,  # Corrected spelling here
    system_message="You are a helpful math assistant. Use the 'add' tool to compute additions.",
)

# Define async execution loop
async def main():
    result = await math_agent.run(task="What is the sum of 5 and 7?")
    print(result.messages[-1].content)

if __name__ == "__main__":
    asyncio.run(main())