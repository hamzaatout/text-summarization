# Flask-Free-AI: Local Hugging Face Model Deployment

**Developed by:**
- **Hamza Atout** (`text_generation` branch)
- **Ahmad Jazaerli** (`text_summarization` branch)

---

## 🚀 Project Overview

**Flask-Free-AI** is a lightweight AI API service built using **Flask** and **Hugging Face Transformers** that runs entirely for free and locally. It features:

- **Text Generation** using `distilgpt2` (by Hamza)
- **Text Summarization** using `facebook/bart-large-cnn` (by Ahmad)

All inference is done **locally**, without the need for any paid API keys.

---

## 🧠 Features

- Local inference (no internet or API keys needed after setup)
- Lightweight Flask API
- Two powerful endpoints:
  - `/generate_text` – Generates text from a prompt
  - `/summarize_text` – Summarizes long text input
- Git-based collaboration using branches and pull requests

---

## ⚙️ Tech Stack

- **Flask**: Web server
- **Transformers**: Hugging Face library for NLP models
- **Torch**: Backend engine for deep learning models
- **Git & GitHub**: Collaboration and version control

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/flask-free-ai.git
cd flask-free-ai
```

### 2. Create and activate a virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
Create a `requirements.txt` file with:
```
Flask
transformers
torch
```

Then install:
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

The server will run at `http://localhost:5000/`.

---

## 🧪 Usage

### 🔹 Text Generation (`text_generation` branch by Hamza)
**Endpoint:** `POST /generate_text`

**Request Example:**
```json
{
  "prompt": "AI is the future of",
  "max_length": 50
}
```

**Curl Example:**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"prompt":"AI is the future of","max_length":50}' \
  http://localhost:5000/generate_text
```

**Sample Response:**
```json
{
  "generated_text": "AI is the future of technology and society..."
}
```

---

### 🔹 Text Summarization (`text_summarization` branch by Ahmad)
**Endpoint:** `POST /summarize_text`

**Request Example:**
```json
{
  "text": "A very long piece of text that needs to be summarized...",
  "max_length": 60,
  "min_length": 20
}
```

**Curl Example:**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"text":"A very long piece of text...","max_length":60,"min_length":20}' \
  http://localhost:5000/summarize_text
```

**Sample Response:**
```json
{
  "summary": "A concise version of the input text."
}
```

---

## 👨‍💻 Collaboration & Branching

### Branch Structure:
- **Hamza Atout** → `text_generation` (base branch, implements `/generate_text`)
- **Ahmad Jazaerli** → `text_summarization` (feature branch, implements `/summarize_text`)

All collaboration was done using GitHub Pull Requests and feature branching.

---

## 📄 License

This project is for academic and demonstration purposes. Please comply with [Hugging Face](https://huggingface.co/) and [PyTorch](https://pytorch.org/) licenses if using in production.