import boto3

# Instantiate a bedrock runtime client
bedrock_client = boto3.client("bedrock-runtime")

# Send the message.
response = bedrock_client.converse(
    #modelId="global.anthropic.claude-haiku-4-5-20251001-v1:0",
    modelId="amazon.nova-pro-v1:0",

    messages=[{
        "role": "user",
        "content": [{"text": "Create a hello world script."}]
    }],
    system=[{"text": "You are an app developer proficient in Python. Only engage in discussion of coding topics."}],
    inferenceConfig={"temperature": 0.7, 
        #"topP": 0.9, 
        "maxTokens": 500}
    #,additionalModelRequestFields={"top_k": 200}
)
print (response)
