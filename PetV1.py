from microbit import *
import speech
import random
import music
import radio

# Servo control:
# 100 = 1 millisecond pulse all right
# 200 = 2 millisecond pulse all left
# 150 = 1.5 millisecond pulse center
# 10 is 10 milliseconds for period 1/100 Hz

pin0.set_analog_period(10)
radio.on()

happy = Image("00099:00900:00900:00900:00099")
sad = Image("09000:00900:00900:00900:09000")
angry = Image("09000:00900:00900:00900:00090")
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]
data = ['None', 'None']
speech.say("Hello, World")
names = ['sam', 'chris', 'stuart']


while True:
    gesture = accelerometer.current_gesture()
    incoming = radio.receive()
    if incoming:
        data = incoming.split("#")
    else:
        data[0] = "none"

    if gesture == "face up":
        pin1.write_analog(70)
        speech.say("zzz")
        display.scroll("NNN")
        sleep(3000)
    elif data[0] == 'flash':
    # If there's an incoming "flash" message display
    # the firefly flash animation after a random short
    # pause.
        sleep(random.randint(50, 350))
        display.show(flash, delay=100, wait=False)
        speech.pronounce("AE/H", pitch=200, speed=100)
        sleep(500)
    elif data[0] == 'name':
    # If there's an incoming "flash" message display
    # the firefly flash animation after a random short
    # pause.
        sleep(random.randint(50, 350))
        speech.say("Hello", pitch=200, speed=100)
        speech.say(data[1], pitch=200, speed=100)
        sleep(500)
    elif gesture == "shake":
        display.show(angry)
        speech.say("stop it")
    elif button_a.is_pressed():
        display.show(sad)
        pin1.write_analog(100)
        sleep(500)
    elif button_b.is_pressed():
        speech.say("Exterminate")
    elif random.randint(0, 9) == 0:
        pin1.write_analog(70)
        sleep(200)
        pin1.write_analog(150)
        sleep(500)

    elif random.randint(0, 20) == 0:
        speech.say("play with me")
    elif random.randint(0, 20) == 0:
        radio.send('flash#all')
        display.show(flash, delay=100, wait=False)
        sleep(1000)
    elif random.randint(0, 20) == 0:
        radio.send('name#Sam')
        display.show(flash, delay=100, wait=False)
        speech.say("My name is Sam", pitch=200, speed=200)
        sleep(1000)

    else:
        display.show(happy)
        pin1.write_analog(150)
        sleep(500)

display.clear()
