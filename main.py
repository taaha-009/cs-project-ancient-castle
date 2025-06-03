def checkPassword():
    if enteredPassword == PASSWORD:
        basic.clear_screen()
        for index in range(3):
            basic.show_leds("""
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                """)
            basic.pause(150)
            basic.clear_screen()
            basic.pause(150)
        playSuccessSound()
        basic.show_string("GRANTED ACCESS")
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.clear_screen()
        for index2 in range(3):
            basic.show_leds("""
                # . # . #
                . # . # .
                # . # . #
                . # . # .
                # . # . #
                """)
            basic.pause(200)
            basic.clear_screen()
            basic.pause(200)
        playErrorSound()
        basic.show_string("INTRUDER ALERT")
        basic.show_icon(IconNames.SAD)
    basic.pause(2000)
    resetInput()

def on_button_pressed_a():
    global currentDigit
    currentDigit = (currentDigit + 1) % 10
    basic.show_number(currentDigit)
input.on_button_pressed(Button.A, on_button_pressed_a)

def playErrorSound():
    for index3 in range(3):
        music.play_tone(196, music.beat(BeatFraction.EIGHTH))
        music.rest(music.beat(BeatFraction.EIGHTH))

def on_button_pressed_b():
    global enteredPassword, inputCount, currentDigit
    enteredPassword = "" + enteredPassword + str(currentDigit)
    inputCount += 1
    if inputCount < 5:
        currentDigit = 0
        basic.show_number(currentDigit)
    else:
        checkPassword()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    resetInput()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def playSuccessSound():
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(330, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
def resetInput():
    global enteredPassword, currentDigit, inputCount
    enteredPassword = ""
    currentDigit = 0
    inputCount = 0
    basic.clear_screen()
    basic.show_number(currentDigit)
inputCount = 0
enteredPassword = ""
PASSWORD = ""
currentDigit = 0
PASSWORD = "70065"
basic.show_string("PASS")
basic.show_number(currentDigit)