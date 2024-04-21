from openai import AzureOpenAI
import json

with open('config.json') as config_file:
    config = json.load(config_file)

client = AzureOpenAI(
    azure_endpoint = config['ai_playground']['endpoint'],
    api_key = config['ai_playground']['api_key'],
    api_version = config['ai_playground']['api_version'],
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"},
]

completion = client.chat.completions.create(
    model = config['ai_playground']['model_name'],
    messages = messages
)

print(completion.model_dump_json(indent=2))