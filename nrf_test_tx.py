from RF24 import RF24, RF24_1MBPS, RF24_PA_LOW
import time

radio = RF24(22, 0)  # CE=GPIO22, CSN=CE0
radio.begin()
radio.setPALevel(RF24_PA_LOW)
radio.setChannel(0x4c)
radio.setDataRate(RF24_1MBPS)

radio.openWritingPipe(b'1Node')
radio.stopListening()

while True:
    message = b'HelloPi'
    result = radio.write(message)
    print("Sent:", message, "Success:", result)
    time.sleep(1)
