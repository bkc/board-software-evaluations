# activate each relay for 1 second
import digitalio
import time
import microcontroller

port_numbers = (
    microcontroller.pin.GPIO10,
    microcontroller.pin.GPIO11,
    microcontroller.pin.GPIO22,
    microcontroller.pin.GPIO23,
)
for relay_port in port_numbers:
    with digitalio.DigitalInOut(relay_port) as relay:
        relay.direction = digitalio.Direction.OUTPUT
        relay.value = True
        time.sleep(1)
        relay.value = False
