from flask import Flask, request, jsonify
from chatbot import ask_chatbot
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = ask_chatbot(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
