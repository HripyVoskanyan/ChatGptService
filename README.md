# ChatGptService

ChatGptService is a Flask-based API for a chatbot service utilizing the Llama model. This service includes two different endpoints for handling requests: a free service and a premium service.

## Prerequisites

Before you run the service, you need to ensure you have Python installed on your machine. This project uses Python 3.8+.

## Installation

1. **Clone the repository**:
   ```bash
   git clone [Your Repository URL]
   cd ChatGptService

2. **Installing Requirements for the LLM Model**
   ```bash
   pip install -r requirements.txt

3. **Running the Application**
   ```bash
   flask run --host=0.0.0.0 --port=5000

4. **Testing the Application**
You can test the API endpoints using curl from the command line. Below are examples of how to invoke the service:
   ```bash
   curl -X POST http://localhost:5000/generate -H "Content-Type: application/json" -d '{"text": "Hello, how are you?"}'
   curl -X POST http://localhost:5000/generate -H "Content-Type: application/json" -d '{"text": "Explain quantum mechanics to me."}'

Using **Postman**
Postman is a popular tool for testing APIs. To use Postman to test the endpoints:

- Open Postman.
- Create a new request.
- Set the method to POST.
- Enter the URL http://localhost:5000/generate.
- Under the "Headers" section, add a key Content-Type with value application/json.
- In the "Body" section, select raw and input a JSON object like {"text": "Hello, how are you?"}.
Send the request and view the response.

## Further Help

This README should provide a comprehensive guide to getting your Flask API up and running and testing it effectively using both command line tools and graphical interfaces like Postman. If there are any specific details or configurations that differ for your setup, make sure to adjust the instructions accordingly.
If you encounter any further problems, contact us at
- hripsime_voskanyan@edu.aua.am
- kristine_manukyan@edu.aua.am
- laura_barseghyan@edu.aua.am
- ani_babayan2@edu.aua.am
- anna_stepanyan@edu.aua.am
