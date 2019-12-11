import serial

class ConnectSerial:
  def __init__(self, port, baudrate):
    self.comport = serial.Serial(port, baudrate)
    self.comando_temperatura = b't'
  
  def send(self):
    self.comport.write(self.comando_temperatura)

  def read(self):
    return self.comport.readline()

   
