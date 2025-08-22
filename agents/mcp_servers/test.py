from openai import OpenAI
import base64
from dotenv import load_dotenv
load_dotenv()

client = OpenAI() 

response = client.responses.create(
    model="gpt-5",
    input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools=[{"type": "image_generation"}],
)

print(response.output, 'output')