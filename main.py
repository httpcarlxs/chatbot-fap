import openai
from dotenv import load_dotenv
import os

def load_configuration():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    return api_key

key = load_configuration()

client = openai.OpenAI(
  api_key=key,
  base_url="https://chat.maritaca.ai/api", 
)

messages = [
    {"role": "user", "content": "Quanto é 25 + 27?"},
]

response = client.chat.completions.create(
    model="sabia-2-small", 
    messages=messages,
    temperature=0.7,
    max_tokens=512,
)
answer = response.choices[0].message.content
