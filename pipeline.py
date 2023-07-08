import openai
from dotenv import dotenv_values

secrets = dotenv_values(".secrets")
openai.api_key=secrets['API_KEY']
messages = [{"role": "system", "content": "You are a story writer. You give them only one sentence output"}]

def chat(user_input):
    messages.append({"role": "user", "content": user_input})
    prompt = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        max_tokens=20,
        messages=messages,
        n=1,
        frequency_penalty=0.3
    )
    reply = prompt.choices[0]['message']['content']
    messages.append({'role': 'assistant', 'content': reply})
    print(prompt['choices'][0]['message'])
    return reply
  