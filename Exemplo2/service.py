from flask import Flask
from ArduinoSerial import ConnectSerial

app = Flask(__name__)

porta = "/dev/ttyUSB0"
baudrate = 115200
arduino = ConnectSerial(porta, baudrate)l

@app.route('/')
def hello_world():
	return 'Hello to the World of Flask!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
