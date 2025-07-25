import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_chatbot(prompt, system_role="You are a helpful teaching assistant."):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
