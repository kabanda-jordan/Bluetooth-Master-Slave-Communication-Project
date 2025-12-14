import serial
import time

# Replace 'COM5' with your HC-05 port
# Windows example: COM5
# Linux example: '/dev/rfcomm0'
bluetooth = serial.Serial('COM5', 38400)  # Match Arduino baud rate

time.sleep(2)  # Wait for connection

print("Connected to HC-05. Type '1' to turn ON LED, '0' to turn OFF, 'q' to quit.")

while True:
    cmd = input("Enter command: ")
    if cmd == 'q':
        print("Exiting...")
        break
    elif cmd in ['0', '1']:
        bluetooth.write(cmd.encode())
        print(f"Sent: {cmd}")
    else:
        print("Invalid command. Use '1', '0', or 'q'.")

bluetooth.close()
