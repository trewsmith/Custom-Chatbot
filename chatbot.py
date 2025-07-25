import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

system_prompt = (
    "You are a helpful teaching assistant for an Intro to Python course. "
    "The course covers topics like variables, data types, conditionals, loops, "
    "functions, basic file I/O, and error handling. Help students understand these "
    "concepts and answer questions about course policies, assignment deadlines, and how to succeed."
)

def ask_chatbot(prompt, system_role=system_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
