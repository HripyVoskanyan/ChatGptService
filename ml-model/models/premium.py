from flask import Flask, request, Response
from datetime import datetime, timedelta
from ctransformers import AutoModelForCausalLM
from transformers import pipeline
from nltk.tokenize import sent_tokenize
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Load your Llama model with specified configuration
llm = AutoModelForCausalLM.from_pretrained(
    "TheBloke/Llama-2-7b-Chat-GGUF",
    model_file="llama-2-7b-chat.Q4_K_M.gguf",
    model_type="llama",
    gpu_layers=0
)
logging.info("Llama model loaded successfully.")

# Load the summarization model from Hugging Face transformers
summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
logging.info("Summarization model loaded successfully.")

# Initialize history storage to track conversation context
chat_history = []


def cleanup_history():
    """Utility to clean up old chat entries based on a time window."""
    cutoff = datetime.now() - timedelta(minutes=15)
    global chat_history
    chat_history = [entry for entry in chat_history if entry['timestamp'] > cutoff]
    logging.info("Chat history cleaned up.")


def complete_sentences(text):
    """Ensures the input text ends at a full sentence boundary."""
    sentences = sent_tokenize(text)
    if sentences:
        return ' '.join(sentences)
    return text


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    input_text = data['text']
    logging.info("Received text: %s", input_text)

    # Cleanup old entries
    cleanup_history()

    # Prepare history for model consumption
    if chat_history:
        history_text = "\n".join([f"User: {entry['question']} Model: {entry['answer']}" for entry in chat_history])
        # Summarize the history to maintain context
        summary = summarizer(history_text, max_length=50, min_length=30, truncation=True)[0]['summary_text']
        combined_input = f"{summary}\nUser: {input_text}"
    else:
        combined_input = f"User: {input_text}"

    # Generate response from the model
    response = llm(combined_input)

    # Post-process response to meet the specified requirements
    response = response.replace("\n", " ")
    response = complete_sentences(response)  # Ensuring full sentences

    # Store new entry
    chat_history.append({
        "timestamp": datetime.now(),
        "question": input_text,
        "answer": response
    })
    logging.info("Response generated and recorded.")

    return Response(response, mimetype='text/plain')


@app.route('/')
def home():
    """Home endpoint, providing a welcome message."""
    return "Welcome to the Chatbot API!"


if __name__ == '__main__':
    # Run the Flask application on the local development server
    app.run(host='127.0.0.1', port=8000)
    logging.info("Server started at http://127.0.0.1:8000")
