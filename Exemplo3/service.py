from flask import Flask
from ArduinoSerial import ConnectSerial

app = Flask(__name__)

porta = "/dev/ttyUSB1"
arduino = ConnectSerial(porta, 115200)

@app.route('/')
def index():
  with open("static/index.html", "r") as file:
    return file.read()

@app.route('/ler_temperatura')
def ler_temperatura():
  arduino.send()
  return arduino.read()
    # return "24"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
