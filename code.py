# Originally coded by Novaspirit Tech
# Copy this code into your code.py file.
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

# Add consumer control for media keys
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)


# These are the corresponding GPIOs on the Pi Pico
# that you soldered
btn1_pin = board.GP1
btn2_pin = board.GP2
btn3_pin = board.GP3
btn4_pin = board.GP4
btn5_pin = board.GP5
btn6_pin = board.GP6
btn7_pin = board.GP7
btn8_pin = board.GP8
btn9_pin = board.GP9

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN
btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN
btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN
btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN
btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN
keyboard = Keyboard(usb_hid.devices)

# below are the key values that you can change to
# fit your preferences.
#
# ORDER IN KEYBOARD:
# btn3 btn2 btn1
# btn6 btn5 btn4
# btn9 btn8 btn7


while True:
    if btn1.value:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.075)
    if btn2.value:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.075)
    if btn3.value:
        cc.send(ConsumerControlCode.MUTE)
        time.sleep(0.075)
    if btn4.value:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.075)
    if btn5.value:
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        time.sleep(0.075)
    if btn6.value:
        cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        time.sleep(0.075)
    if btn7.value:
        keyboard.send(Keycode.F15)
        time.sleep(0.075)
    if btn8.value:
        keyboard.send(Keycode.CONTROL, Keycode.RIGHT_ARROW)
        time.sleep(0.075)
    if btn9.value:
        keyboard.send(Keycode.CONTROL, Keycode.LEFT_ARROW)
        time.sleep(0.075)
    time.sleep(0.075)
