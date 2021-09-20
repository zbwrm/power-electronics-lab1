import serial, os
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
start_time = datetime.now()

device = "/dev/cu.usbmodem14101"
baud   = "9600"
filename = os.path.join(HERE, "temp_log.csv")
rolling_1 = [0, 0, 0, 0, 0]
rolling_2 = [0, 0, 0, 0, 0]

def array_rotate(in_array, new_val):
    out_array = in_array[1::]
    out_array.append(new_val)

    return out_array

def avg(in_array):
    return sum(in_array)/len(in_array)

with serial.Serial(device,baud) as serial_port:
    with open(filename, 'w') as log_file:
        while 1:
            line = serial_port.readline()
            new_data = line.split()

            input_1 = int(new_data[0]) / 1024.0
            rolling_1 = array_rotate(rolling_1, input_1)
            rolling_1_avg = avg(rolling_1)

            input_2 = int(new_data[1]) / 1024.0
            rolling_2 = array_rotate(rolling_2, input_2)
            rolling_2_avg = avg(rolling_2)

            timediff = (datetime.now() - start_time).total_seconds()

            outstring = f"{timediff},{rolling_1_avg},{rolling_2_avg}\n"
            log_file.write(outstring)
            print(outstring)
            log_file.flush()