from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    """Render chat page"""
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    """Handle user input and return AI response"""
    user_input = request.form.get("user_input")
    reply = ""

    if not user_input:
        reply = "Please type a question."
    else:
        try:
            # Use the new OpenAI 1.0+ API
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

    return render_template("chat.html", user_input=user_input, reply=reply)

if __name__ == "__main__":
    # Expose app to all IPs (0.0.0.0) for Docker/EC2
    app.run(host="0.0.0.0", port=5000, debug=True)
