from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello to the World of Flask!'

@app.route('/teste')
def teste_de_rota():
	return 'Nova rota de teste!!!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
