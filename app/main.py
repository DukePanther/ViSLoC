from flask import Flask, request, render_template
from app.ai_module import get_advice
from app.study_planner import generate_study_plan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    response = get_advice(query)
    return response

@app.route('/study_plan', methods=['POST'])
def study_plan():
    history = request.form['history']
    plan = generate_study_plan(history)
    return plan

if __name__ == '__main__':
    app.run(debug=True)