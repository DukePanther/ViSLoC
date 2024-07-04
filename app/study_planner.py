def generate_study_plan(history):
    prompt = f"Create a study plan for a student with the following history: {history}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()