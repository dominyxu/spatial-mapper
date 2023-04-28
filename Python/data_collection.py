'''
  This code collects data sent by the microcontroller over UART.
  It calculates Y and Z components of the vector and append the data into distance_data.txt file in X Y Z format.
'''

import math
import serial

SETS = 3
RESOLUTION = 32
ANGLE = 2 * math.pi / RESOLUTION

def main():
  #uart port initialization,  BAUD rate
  ser = serial.Serial('COM3', 115200)

  while (True):
    try:
      line = ser.readline().decode("utf-8").rstrip()
      print(line)

      if (line == "start"):
        for i in range(SETS):
          #for each measurement, append to distance_data
          file = open("distance_data.txt", "a")
          print(f'set-{i + 1}')
          for j in range(RESOLUTION):
            line = ser.readline().decode("utf-8").rstrip()
            print(line)
            y = (int(line) / SETS) * math.sin(ANGLE * j);
            z = (int(line) / SETS) * math.cos(ANGLE * j);
            file.write(f"{i * 50} {y} {z}\n")
          file.close()
        break
    except KeyboardInterrupt:
      exit()

if __name__ == "__main__":
  main()
