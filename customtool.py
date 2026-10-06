from dotenv import load_dotenv
load_dotenv()
import asyncio

from autogen_agentchat.messages import UserMessage
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

def to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5.0/9.0  

def weeks_to_days(weeks: int) -> int:
    """Convert weeks to days"""
    return weeks * 7

helper_agent = AssistantAgent(
    name="helper_agent",
    model_client=model_client,
    tools=[to_celsius, weeks_to_days],
    reflect_on_tool_use=True,
    system_message="You are a helpful assistant. Use the provided tools to answer questions."   
)

async def main():
    # Await the agent execution
    result = await helper_agent.run(
        task="Convert 100 degrees Fahrenheit to Celsius and 3 weeks to days."
    )
    # Output: 100 degrees Fahrenheit is approximately 37.78 degrees Celsius, and 3 weeks is 21 days.
    print(result.messages[-1].content)

if __name__ == "__main__":
    asyncio.run(main())