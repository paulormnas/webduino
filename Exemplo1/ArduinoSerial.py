import serial

class ConnectSerial:
  def __init__(self, port, baudrate):
    self.comport = serial.Serial(port, baudrate)
    self.COMANDO = b"t"
   
  def send(self):
    self.comport.write(self.COMANDO)
    
  def read(self):
    return self.comport.readline()
