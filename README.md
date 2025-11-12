# genai-chatbot-devops-demo
A simple GenAI chatbot built with Flask and OpenAI API for DevOps CI/CD demo
# 🤖 GenAI Chatbot - DevOps Demo

A simple AI Chatbot built using **Flask** and **OpenAI API**, designed for demonstrating **DevOps CI/CD pipelines**.

---

## 🧩 Features
- Interactive Chat UI (HTML + JS)
- Flask backend integrated with OpenAI
- Ready for Dockerization and CI/CD
- Can be deployed on AWS EC2, ECS, or Kubernetes

---

## 🚀 Run Locally (Optional)
```bash
export OPENAI_API_KEY="your-openai-key"
pip install -r requirements.txt
python app.py
docker build -t genai-chatbot .
docker run -p 5000:5000 -e OPENAI_API_KEY=your-openai-key genai-chatbot

---

🎯 **You’re Done With Project Setup!**
No local setup needed — everything’s ready in GitHub.

---

### ✅ Next Step
Now we’ll::
1. **Create DockerHub repo**
2. **Build + Push Docker image using GitHub Actions**
3. **Deploy on AWS EC2**

---
