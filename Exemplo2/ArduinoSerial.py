import serial

class ConnectSerial:
  def __init__(self, port, baudrate):
    self.comport = serial.Serial(port, baudrate)
    self.comando_simples = b's'
    self.comando_historico = b'h'
   
  def leitura_simples(self):
    self.comport.write(self.comando_simples)
  
  def historico(self):
    self.comport.write(self.comando_historico)
  
  def read(self):
    return self.comport.readline()


if __name__ == "__main__":
 #### Teste dos métodos ####
  porta = "/dev/ttyUSB0"
  baudrate = 115200
  arduino = ConnectSerial(porta, baudrate) # Nova instancia da classe ConnectSerial

  arduino.leitura_simples() # Testa o método de leitura simples 
  print(arduino.read())            # Verifica o resultado

  arduino.historico()       # Testa o método de leitura do histórico
  print(arduino.read())            # Verifica o resultado
