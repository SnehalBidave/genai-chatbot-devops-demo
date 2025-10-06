from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

# Load OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

openai.api_key = openai_api_key

@app.route("/")
def home():
    """Render chat page."""
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    """Handle user input and return AI response."""
    user_input = request.form.get("user_input")
    reply = ""

    if not user_input:
        reply = "Please type a question."
    else:
        try:
            # Use the OpenAI 1.0+ API
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful DevOps assistant."},
                    {"role": "user", "content": user_input},
                ],
                temperature=0.5,
                max_tokens=500
            )
            reply = response.choices[0].message.content.strip()
        except openai.error.OpenAIError as oe:
            # Handle OpenAI-specific errors
            reply = f"OpenAI API Error: {str(oe)}"
        except Exception as e:
            # Handle generic errors
            reply = f"Unexpected Error: {str(e)}"

    return render_template("chat.html", user_input=user_input, reply=reply)


if __name__ == "__main__":
    # Expose app to all IPs for Docker/EC2
    app.run(host="0.0.0.0", port=5000, debug=True)
