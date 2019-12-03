import serial
import time

comport = serial.Serial("/dev/ttyACM0", 115200)
time.sleep(1.8) # Entre 1.5s a 2s
COMANDO = b"t"
comport.write(COMANDO)
#resultado = comport.read()
#print(resultado)
