import openai
import os

openai.environ['OPENAI_API_KEY'] = ''

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=200,
    temperature=0.1,
    messages=[
        {"role": "system", "content": "Você é um programador. Retorne apenas códigos limpos."},
        {
            "role": "user",
            "content": "Escreva um código de Hello World em Python"
        }
    ]
)

print(completion.choices[0].message['content'])
