from flask import Flask, render_template, request, jsonify
import openai, os

app = Flask(__name__)

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    if not openai.api_key:
        return jsonify({"reply": "⚠️ Error: Missing OpenAI API key."}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response["choices"][0]["message"]["content"]
    except Exception as e:
        bot_reply = f"⚠️ Error while connecting to OpenAI API: {str(e)}"

    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    # Bind to all interfaces for Docker
    app.run(host="0.0.0.0", port=5000)
