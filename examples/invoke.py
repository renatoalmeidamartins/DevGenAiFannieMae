
# import AWS SDK for Python and json encoder
import boto3, json
# Instantiate a bedrock runtime client
bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

# Construct a payload for the model
body = json.dumps({
	"anthropic_version": "bedrock-2023-05-31",
	"max_tokens": 5000,
	"messages": [
		{
			"role": "user",
			#"content": "Hello"
			"content": "Create a script to resize images"
		}
	]
})


# Invoke Claude 4.5 Sonnet model using the payload
response = bedrock_runtime.invoke_model(
	body=body,
	modelId="global.anthropic.claude-haiku-4-5-20251001-v1:0",
	accept="application/json",
	contentType="application/json"
)

# Print a model response
#print (response)
response_body = json.loads(response.get("body").read())
#print(response_body)
print("Response from the model:")
print(response_body["content"][0]["text"])


