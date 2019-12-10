import serial

class ConnectSerial:
  def __init__(self, port, baudrate):
    self.comport = serial.Serial(port, baudrate)
    
   
