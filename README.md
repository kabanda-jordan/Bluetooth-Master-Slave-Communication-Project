# Bluetooth-Master-Slave-Communication-Project

Bluetooth Master–Slave LED Control Project
Project Overview

This project demonstrates wireless communication between two Arduino boards using HC-05 Bluetooth modules. The setup allows a Master device (Arduino or Python script) to control an LED connected to a Slave Arduino wirelessly.

Master device: Sends commands (1 for ON, 0 for OFF).

Slave device: Receives commands and controls the LED.

Communication uses UART protocol via SoftwareSerial.

This project can be used as a foundation for remote device control, home automation, or IoT prototypes.

Components Required

2 × Arduino UNO

2 × HC-05 Bluetooth modules

1 × LED

1 × 220Ω resistor

Jumper wires

Breadboard

Optional for Python control:

PC with Bluetooth

Python 3 installed

PySerial library (pip install pyserial)

Circuit Diagram

Slave Arduino:

HC-05 TX → Arduino D10 (RX)

HC-05 RX → Arduino D11 (TX, use voltage divider if 5V)

LED → Arduino D7 → 220Ω → GND

Master Arduino (optional buttons):

HC-05 TX → Arduino D10 (RX)

HC-05 RX → Arduino D11 (TX, use voltage divider if 5V)

Button 1 → D2 (turn LED ON)

Button 2 → D3 (turn LED OFF)

HC-05 Configuration (AT Mode)

Enter AT mode: Power cycle the module while holding the KEY/EN button.

Set roles:

AT+ROLE=0 → Slave

AT+ROLE=1 → Master

Bind Master to Slave:

AT+BIND=0021,07,002889  # Replace with Slave HC-05 address


Make discoverable (if needed):

AT+INQM=0,5,9

Arduino Code

Slave Arduino: Reads commands from HC-05 and controls LED.

Master Arduino: Sends commands to Slave when buttons are pressed.

(Refer to Slave.ino and Master.ino in the repository.)
