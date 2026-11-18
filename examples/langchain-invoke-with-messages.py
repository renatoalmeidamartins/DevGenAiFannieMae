from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model

# Follow the steps here to configure your credentials:
# https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

model = init_chat_model(
    "global.anthropic.claude-haiku-4-5-20251001-v1:0",
    model_provider="bedrock_converse",
)


messages= [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]
response = model.invoke(messages)
print (response)
