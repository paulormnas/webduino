from flask import Flask
from ArduinoSerial import ConnectSerial

app = Flask(__name__)

porta = "/dev/ttyUSB0"
baudrate = 115200
arduino = ConnectSerial(porta, baudrate)

@app.route('/')
def hello_world():
	return 'Hello to the World of Flask!'

@app.route('/leitura_simples')
def leitura_simples():
  arduino.leitura_simples()
  return arduino.read()

@app.route('/historico')
def historico():
  arduino.historico()
  return arduino.read()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
