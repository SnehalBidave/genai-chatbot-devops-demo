from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

# Load OpenAI key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"]
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful DevOps assistant."},
                {"role": "user", "content": user_input},
            ],
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error: {str(e)}"
    return render_template("index.html", user_input=user_input, reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
