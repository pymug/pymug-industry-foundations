from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return '<h1>HELLO WORLD</h1> folks'


@app.route('/multiply/<number1>/<number2>')
def calculator(number1, number2):
	result = int(number1)*int(number2)
	return f'The number is: {result}'