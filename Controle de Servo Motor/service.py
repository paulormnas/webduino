from flask import Flask
from ArduinoSerial import ConnectSerial

app = Flask(__name__)

porta = "/dev/ttyUSB0"
#arduino = ConnectSerial(porta, 115200)

@app.route('/')
def teste_de_rota():
 with open("static/index.html", "r") as file:
  return file.read()


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
