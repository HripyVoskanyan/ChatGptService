from flask import Flask, request, render_template
from g4f.client import Client

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    user_input = list(request.form.values())
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input[0]}]
    )
    print('user_input: ', user_input)
    return render_template('index.html', prediction_text='Answer: {}'.format(response.choices[0].message.content))


if __name__ == "__main__":
    app.run()