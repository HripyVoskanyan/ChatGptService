from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


@app.route('/generate', methods=['POST'])
def generate():
    logging.debug("Received data: %s", request.data)
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text in request'}), 400

    input_text = data['text']
    logging.debug("Input text: %s", input_text)

    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')
    output_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response_text = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    logging.debug("Response text: %s", response_text)
    return jsonify({'response': response_text})

@app.route('/')
def home():
    return "Welcome to the Chatbot API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
