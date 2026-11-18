from langchain.chat_models import init_chat_model

# Follow the steps here to configure your credentials:
# https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

model = init_chat_model(
    "global.anthropic.claude-haiku-4-5-20251001-v1:0",
    model_provider="bedrock_converse",
)



response = model.invoke("Why do parrots have colorful feathers?")
print(response)