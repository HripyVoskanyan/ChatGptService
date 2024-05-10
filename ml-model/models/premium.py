from flask import Flask, request, Response
from datetime import datetime, timedelta
from ctransformers import AutoModelForCausalLM
from transformers import pipeline
from nltk.tokenize import sent_tokenize

app = Flask(__name__)


# Load your Llama model
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7b-Chat-GGUF", model_file="llama-2-7b-chat.Q6_K.gguf", model_type="llama", gpu_layers=0)

# Load the summarization model
summarizer = pipeline('summarization', model='facebook/bart-large-cnn')

# Initialize history storage

chat_history = []

# Utility to clean up old entries
def cleanup_history():
    cutoff = datetime.now() - timedelta(minutes=15)
    global chat_history
    chat_history = [entry for entry in chat_history if entry['timestamp'] > cutoff]

def complete_sentences(text):
    # This function takes a string and ensures it ends at a full sentence boundary.
    sentences = sent_tokenize(text)
    if sentences:
        # Joins all complete sentences into one string.
        return ' '.join(sentences)
    return text

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    input_text = data['text']

    # Cleanup old entries
    cleanup_history()

    # Prepare history for model consumption
    if chat_history:
        history_text = "\n".join([f"User: {entry['question']} Model: {entry['answer']}" for entry in chat_history])
        # Summarize the history
        summary = summarizer(history_text, max_length=50, min_length=30, truncation=True)[0]['summary_text']
        combined_input = f"{summary}\nUser: {input_text}"
    else:
        combined_input = f"User: {input_text}"

    # Generate response from the model
    response = llm(combined_input)

    # Post-process response to meet the specified requirements
    response = response.replace("\n", " ")  # Remove newlines
    response = complete_sentences(response.replace("\n", " "))  # Removing newlines and ensuring full sentences
    # Store new entry
    chat_history.append({
        "timestamp": datetime.now(),
        "question": input_text,
        "answer": response
    })

    return Response(response, mimetype='text/plain')

@app.route('/')
def home():
    return "Welcome to the Chatbot API!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)