import asyncio  # <--- Add this import line
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage
from autogen_agentchat.agents import AssistantAgent

# Load API keys from environment
load_dotenv()

# Build model client
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

# 2) Agent (give it a name and a job)
assistant = AssistantAgent(
    name="assistant",
    model_client=model_client,
    system_message="You are a friendly helper. Keep answers short.",
)

# 3) Define main execution loop
async def main():
    # Run the task on the agent
    result = await assistant.run(task="Give me one fun fact about the moon.")
    
    # The agent's answer is the LAST message
    print(result.messages[-1].content)

if __name__ == "__main__":
    asyncio.run(main())