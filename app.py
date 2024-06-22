from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Predefined responses for health-related questions
health_responses = {
    "What are the symptoms of COVID-19?": "Common symptoms of COVID-19 include fever, dry cough, and tiredness. Some patients may have aches and pains, nasal congestion, sore throat, or diarrhea.",
    "How can I prevent heart disease?": "To prevent heart disease, maintain a healthy diet, exercise regularly, avoid smoking, and manage stress.",
    "What should I do if I have a fever?": "If you have a fever, rest, stay hydrated, and take over-the-counter fever-reducing medications. If the fever persists or is very high, consult a healthcare provider.",
    "What are the benefits of regular exercise?": "Regular exercise helps improve cardiovascular health, strengthens muscles, enhances flexibility, and boosts mental health.",
    "How much water should I drink daily?": "It is generally recommended to drink at least 8 glasses of water per day, but individual needs may vary based on factors such as activity level and climate.",
    # Add more questions and answers as needed
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        reply = health_responses.get(user_message, "I'm sorry, I don't have an answer for that question. Please consult a healthcare provider for more information.")
        return jsonify({'reply': reply})
    return jsonify({'error': 'No message received'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
