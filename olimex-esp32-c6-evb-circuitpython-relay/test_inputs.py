# read each input and report when true
import digitalio
import time
import microcontroller

port_numbers = (
    microcontroller.pin.GPIO1,
    microcontroller.pin.GPIO2,
    microcontroller.pin.GPIO3,
    microcontroller.pin.GPIO15,
)

port_name_items = [
    (digitalio.DigitalInOut(port_number), port_number) for port_number in port_numbers
]

for port, port_name in port_name_items:
    port.direction = digitalio.Direction.INPUT

print("Polling inputs")
while True:
    for port, port_name in port_name_items:
        if not port.value:
            print(f"{port_name} is True")
            while not port.value:
                time.sleep(0.1)
            print(f"{port_name} is False")

    time.sleep(0.1)
