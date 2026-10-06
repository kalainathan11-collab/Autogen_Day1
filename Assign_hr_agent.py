import asyncio
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Load API key from .env file
load_dotenv()

# Initialize model client
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

# Create AssistantAgent with strict HR persona
agent = AssistantAgent(
    name="hr_assistant",
    model_client=model_client,
    system_message="You are an HR assistant."
)

async def main():
    # Stream the output directly to the terminal using Console UI
    await Console(
        agent.run_stream(
            task="Write a job description for a Junior Python Developer using exactly 5 bullet points (one line per bullet point) and no extra text."
        )
    )
    
    # Close model client to prevent the script from hanging
    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())