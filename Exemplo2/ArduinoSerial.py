import serial

class ConnectSerial:
  def __init__(self, port, baudrate):
    self.comport = serial.Serial(port, baudrate)
    
   
  def send(self):
    
    
  def read(self):
    return self.comport.readline()
