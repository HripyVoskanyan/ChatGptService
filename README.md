# AI-powered Chat Service

An AI-powered Chat Service that hosts a pre-trained AI model that responds to questions from logged-in users.
We provide two services: Standard and Premium. The standard plan provides a usual chat experience with basic features, the premium plan unlocks the functionality of having conversation context, which facilitates smart replies.

<br>

#LLM Model

We use a Flask-based API for a chatbot service utilizing the Llama model. This service includes two different endpoints for handling requests: a free service and a premium service.

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

<br>

#Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

<br>

## Further Help

This README should provide a comprehensive guide to getting your web app running and testing it effectively. If there are any specific details or configurations that differ for your setup, make sure to adjust the instructions accordingly.
If you encounter any further problems, contact us at
- hripsime_voskanyan@edu.aua.am
- kristine_manukyan@edu.aua.am
- laura_barseghyan@edu.aua.am
- ani_babayan2@edu.aua.am
- anna_stepanyan@edu.aua.am
