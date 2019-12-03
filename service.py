from flask import Flask
from ArduinoSerial import ConnectSerial

app = Flask(__name__)

porta = "/dev/ttyACM0"
arduino = ConnectSerial(porta, 115200)

@app.route('/')
def hello_world():
	return 'Hello to the World of Flask!'

@app.route('/teste')
def teste_de_rota():
 with open("static/index.html", "r") as file:
  return file.read()

# Rota para interação com o Arduino. Através desta rota são enviados comandos para o Arduino 
@app.route('/arduino')
def enviar_para_arduino():
  arduino.send()
  return arduino.read()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
