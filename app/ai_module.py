from openai import OpenAI
import pathlib

path = str(pathlib.Path(__file__).parent.resolve()) + '\\secret_key.txt'
print(path)
file = open(path, "r")

client = OpenAI(
  organization='org-HQQB3V2KlBXlCQ1EGvYk6V9D',
  project='proj_bYcU0YvaWZ6J6LICnfOMIGZM',
  api_key=file.read()
)

def get_advice(query):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": query}],
        stream=False
    )
    return response.choices[0].message.content