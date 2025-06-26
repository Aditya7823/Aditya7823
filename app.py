from flask import Flask, render_template, request
from generate import generate_queue_question

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    question = None
    result = None

    if request.method == 'POST':
        if 'difficulty' in request.form:
            difficulty = request.form.get('difficulty')
            question = generate_queue_question(difficulty)
        elif 'user_answer' in request.form:
            user_answer = request.form.get('user_answer')
            original_question = request.form.get('question')
            # Placeholder logic for now, since we don't have expected answers
            result = f"Thanks! You answered: '{user_answer}'. (Auto-checking not implemented yet)"
            question = original_question  # Retain the original question

    return render_template('questions.html', question=question, result=result)

if __name__ == '__main__':
    app.run(debug=True)
