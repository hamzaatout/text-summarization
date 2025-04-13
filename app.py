from flask import Flask, request, jsonify
from transformers import pipeline

# initialize the Flask app
app = Flask(__name__)

# Load a text-generation pipeline
generator = pipeline("text-generation", model="distilgpt2")

@app.route("/")
def home():
    return "Welcome to the our C2.2 assignment!"

@app.route("/generate_text", methods=["POST"])
def generate_text():
    """
    Endpoint to generate text from a given prompt.
    Expects JSON: {"prompt": "<text prompt>", "max_length": <int>}
    """
    data = request.get_json()

    prompt = data.get("prompt", "") # default to empty string
    max_length = data.get("max_length", 50)  # default to 50 tokens

    # Generate text
    outputs = generator(prompt, max_length=max_length, num_return_sequences=1)
    generated_text = outputs[0]["generated_text"] # Extract the generated text

    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    # Run Flask in debug mode
    app.run(host="0.0.0.0", port=5000, debug=True)