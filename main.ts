function checkPassword () {
    if (enteredPassword == PASSWORD) {
        basic.clearScreen()
        for (let index = 0; index < 3; index++) {
            basic.showLeds(`
                . . . . .
                . . . . #
                . . . # .
                # . # . .
                . # . . .
                `)
            basic.pause(150)
            basic.clearScreen()
            basic.pause(150)
        }
        playSuccessSound()
        basic.showString("GRANTED ACCESS")
        basic.showIcon(IconNames.Happy)
    } else {
        basic.clearScreen()
        for (let index = 0; index < 3; index++) {
            basic.showLeds(`
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                `)
            basic.pause(200)
            basic.clearScreen()
            basic.pause(200)
        }
        playErrorSound()
        basic.showString("INTRUDER ALERT")
        basic.showIcon(IconNames.Sad)
    }
    basic.pause(2000)
    resetInput()
}
input.onButtonPressed(Button.A, function () {
    currentDigit = (currentDigit + 1) % 10
    basic.showNumber(currentDigit)
})
function playErrorSound () {
    for (let index = 0; index < 3; index++) {
        music.playTone(196, music.beat(BeatFraction.Breve))
        music.rest(music.beat(BeatFraction.Eighth))
    }
}
input.onButtonPressed(Button.B, function () {
    enteredPassword = "" + enteredPassword + currentDigit.toString()
    inputCount += 1
    if (inputCount < 5) {
        currentDigit = 0
        basic.showNumber(currentDigit)
    } else {
        checkPassword()
    }
})
input.onGesture(Gesture.Shake, function () {
    resetInput()
})
function playSuccessSound () {
    music.playTone(262, music.beat(BeatFraction.Quarter))
    music.playTone(330, music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
}
function resetInput () {
    enteredPassword = ""
    currentDigit = 0
    inputCount = 0
    basic.clearScreen()
    basic.showNumber(currentDigit)
}
let inputCount = 0
let enteredPassword = ""
let PASSWORD = ""
let currentDigit = 0
PASSWORD = "70065"
basic.showString("PASS")
basic.showNumber(currentDigit)