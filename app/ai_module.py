import openai
import pathlib

path = str(pathlib.Path(__file__).parent.resolve()) + '\\secret_key.txt'
print(path)
file = open(path, "r")
openai.api_key = file.read()

def get_advice(query):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=query,
        max_tokens=200
    )
    return response.choices[0].text.strip()