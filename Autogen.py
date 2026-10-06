import asyncio  # <--- Add this import line
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage

# Load API keys from environment
load_dotenv()

# Build model client
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

async def main():
    reply = await model_client.create(
        [UserMessage(content="Say 3 lines about autogen.", source="user")]
    )
    print(reply.content)

if __name__ == "__main__":
    asyncio.run(main())