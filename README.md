# DevGenAiFannieMae

## Labs, courseware and survey
- [Courseware and labs](https://us-east-1.student.classrooms.aws.training/class/ilt%23jFevEchiN2toTN974chqQB)
## Class links
### Day 1 links
- [Neural network zoo](https://www.asimovinstitute.org/neural-network-zoo/)
- AWS's "what is" series:
    - [What is RAG (Retrieval-Augmented Generation)?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
    - [What is generative AI?](https://aws.amazon.com/what-is/generative-ai/)
    - [What are Embeddings in Machine Learning?](https://aws.amazon.com/what-is/embeddings-in-machine-learning/)
    - [What are Transformers in Artificial Intelligence?](https://aws.amazon.com/what-is/transformers-in-artificial-intelligence/)
    - [What is Deep Learning?](https://aws.amazon.com/what-is/deep-learning/)
- [Embedding projector](https://projector.tensorflow.org/)
- [Attention Is All You Need](https://arxiv.org/pdf/1706.03762)
- [Spatial Transformer Networks](https://arxiv.org/pdf/1506.02025)
- [Built-in algorithms and pretrained models in Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)
- [AWS SDKs](https://builder.aws.com/build/tools#SDKs)
- [Influence response generation with inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html)
- Prompt engineering
    - [Implementing advanced prompt engineering with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/implementing-advanced-prompt-engineering-with-amazon-bedrock/)
    - [Design a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html), in Bedrock's documentation
    - [What is prompt engineering?](https://aws.amazon.com/what-is/prompt-engineering/)
    - [Amazon Bedrock introduces new advanced prompt optimization and migration tool](https://aws.amazon.com/blogs/aws/amazon-bedrock-introduces-new-advanced-prompt-optimization-and-migration-tool/)
    - [Construct and store reusable prompts with Prompt management in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html)
- ReAct: Synergizing Reasoning and Acting in Language Models: [blog](https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/) and [research paper](https://arxiv.org/pdf/2210.03629)
- Inference modes
    - [Batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)
    - [Provisioned throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)
    - Inference profiles
        - [Cross-region inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
        - [Application inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html)
    - [Prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
    - [Choosing an AWS vector database for RAG use cases](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html)
    - [Amazon S3 Vectors now generally available with increased scale and performance](https://aws.amazon.com/blogs/aws/amazon-s3-vectors-now-generally-available-with-increased-scale-and-performance/)
    - [Build semantic search with native vector support in Amazon DynamoDB](https://aws.amazon.com/blogs/database/build-semantic-search-with-native-vector-support-in-amazon-dynamodb/)

### Day 2 links
- [Bedrock runtime](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Operations_Amazon_Bedrock_Runtime.html). This is where we do have the two "invocation" patterns on bedrock-runtime, which are:
    - The "model-independent" [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) and its streamed variant, [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)
    - The "model-dependent" [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) and [InvokeModelWithResponsteStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)
    - [Try the new console experience in Amazon Bedrock, optimized for Anthropic- and OpenAI-compatible APIs](https://aws.amazon.com/blogs/aws/try-the-new-console-experience-in-amazon-bedrock-optimized-for-anthropic-and-openai-compatible-apis/)
- [Introducing Amazon Bedrock Managed Knowledge Base for faster, more accurate enterprise AI applications](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications/)
- RAG-related calls 
    - [Query a knowledge base and retrieve data](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve.html) using the [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) operation
    - [Query a knowledge base and generate responses based off the retrieved data](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html) using the [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html)operation
    - [Rerank](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Rerank.html), which allows you to ["Improve the relevance of query responses with a reranker model in Amazon Bedrock"](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html)
