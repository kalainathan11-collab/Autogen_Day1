import autogen_agentchat
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import UserMessage
from autogen_agentchat.messages import TextMessage
my_message = TextMessage(content="Hello, how are you?", source="user")
print(my_message.content)  # Output: Hello, how are you?
print(my_message.source)   # Output: user