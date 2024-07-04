import openai

openai.api_key = 'sk-proj-HaLU43DeQXgX28G8sCUrT3BlbkFJIVjIKOq9t1dkrc7EG25u'

def get_advice(query):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=query,
        max_tokens=200
    )
    return response.choices[0].text.strip()