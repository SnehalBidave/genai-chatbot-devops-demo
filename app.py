from flask import Flask, request, render_template
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("user_input")
    reply = ""

    if not user_input:
        reply = "Please type a question."
    else:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful DevOps assistant."},
                    {"role": "user", "content": user_input},
                ],
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"Error: {str(e)}"

    return render_template("chat.html", user_input=user_input, reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
