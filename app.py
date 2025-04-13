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

# NOTE: Summarizer loaded once at the top-level for performance.
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/summarize_text", methods=["POST"])
def summarize_text():
    """
    Endpoint to summarize a given text.
    Expects JSON: {"text": "<long text>", "max_length": <int>, "min_length": <int>}
    """
    data = request.get_json()
    text_to_summarize = data.get("text", "")
    max_length = data.get("max_length", 60)
    min_length = data.get("min_length", 20)

    summary_list = summarizer(
        text_to_summarize, max_length=max_length, min_length=min_length, do_sample=False
    )

    summary = summary_list[0]["summary_text"]
    return jsonify({"summary": summary})
if __name__ == "__main__":
    # Run Flask in debug mode
    app.run(host="0.0.0.0", port=5000, debug=True)