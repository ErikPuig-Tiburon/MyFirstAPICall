import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="featherless-ai",
    api_key=os.environ["HF_TOKEN"],
)

response = client.chat_completion(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Escriu un paragraf curt sobre machine learning."
        }
    ],
    max_tokens=200,
    temperature=0.2,
)

print(response.choices[0].message.content)
