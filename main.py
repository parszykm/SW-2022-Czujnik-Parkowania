import serial

uno_port = "COM5"
baud = 9600
file_name = "sensor_data.csv"
print_label = False

ser = serial.Serial(uno_port, baud)
print(f"Connected to Arduino Port {uno_port}")
file = open(file_name, "w")
print("File Created")
while True:
    getData = str(ser.readline())
    data = getData[2:][:-5]
    print(data)
    file = open(file_name, "a")

    file.write(data + "\n")
