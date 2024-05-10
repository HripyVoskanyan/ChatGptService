from flask import Flask, request, Response
from ctransformers import AutoModelForCausalLM
from nltk.tokenize import sent_tokenize
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


def complete_sentences(text):
    """Ensures the input text ends at a full sentence boundary."""
    sentences = sent_tokenize(text)
    if sentences:
        return ' '.join(sentences)
    return text


# Load your Llama model with specified configuration
llm = AutoModelForCausalLM.from_pretrained(
    "TheBloke/Llama-2-7b-Chat-GGUF",
    model_file="llama-2-7b-chat.Q4_K_M.gguf",
    model_type="llama",
    gpu_layers=0
)
logging.info("Llama model loaded successfully.")


@app.route('/generate', methods=['POST'])
def generate():
    # Process input data from the request
    data = request.get_json()
    input_text = data['text']
    logging.info("Received text: %s", input_text)

    # Generate response from the model
    response = llm(input_text)
    logging.info("Generated response.")

    response = response.replace("\n", " ")
    response = complete_sentences(response)  # Ensuring full sentences

    return Response(response, mimetype='text/plain')


@app.route('/')
def home():
    # Home endpoint, providing a welcome message
    return "Welcome to the Chatbot API!"


if __name__ == '__main__':
    # Run the Flask application on the local development server
    app.run(host='127.0.0.1', port=5000)
    logging.info("Server started at http://127.0.0.1:5000")
