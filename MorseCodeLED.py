import RPi.GPIO as GPIO #adds Raspberry pi GPIO library (may need to install this on pi)
import time

#Morse Code Rules
#1 dash = 3 dots (1 dot being .2 seconds)
#space between parts of same letter = 1 dot
#space between letters = 3 dots
#space between words = 7 dots

#configure Pi to use the BCM (Broadcom) pin names
GPIO.setmode(GPIO.BCM)

led_pin = 18 #set which pin program will be activating
GPIO.setup(led_pin, GPIO.OUT) #sets led as output or input

try:
    while True:
        sentence = str(input("Enter a word or sentence you would like to translate into morse code:\n"))
        sentence = sentence.lower() # converts input to lowercase
        n = len(sentence)
        i = 0
        for letter in sentence:
            if sentence[i] == "a":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "b":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False) 
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "c":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "d":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "e":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "f":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "g":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "h":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "i":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "j":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "k":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "l":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "m":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "n":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "o":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "p":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "q":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "r":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "s":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "t":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "u":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "v":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "w":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "x":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "y":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "z":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == ".":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == ",":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "?":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "/":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "@":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "1":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "2":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "3":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "4":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "5":
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "6":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "7":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "8":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "9":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dot
                time.sleep(0.2) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "0":
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6)
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.2)
                GPIO.output(led_pin, True) #dash
                time.sleep(0.6) 
                GPIO.output(led_pin, False)
                time.sleep(0.6)
            elif sentence[i] == "'":
                continue
            elif sentence[i] == " ":
                GPIO.output(led_pin, False)
                time.sleep(0.8)
            i += 1
            print("running...") #indicate if program is running without led
            if i >= n + 1:
                break
finally:
    print("cleaning up")
    GPIO.cleanup()
                
            
            
                
                
            
