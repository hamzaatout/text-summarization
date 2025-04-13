from flask import Flask
from transformers import pipeline

# initialize the Flask app
app = Flask(__name__)

# Load a text-generation pipeline
generator = pipeline("text-generation", model="distilgpt2")

@app.route("/")
def home():
    return "Welcome to the our C2.2 assignment!"

if __name__ == "__main__":
    # Run Flask in debug mode
    app.run(host="0.0.0.0", port=5000, debug=True)