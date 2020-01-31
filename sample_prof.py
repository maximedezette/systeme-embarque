import RPi.GPIO
import adafruit_charlcd

lcd = Adafruit_CharLCD.Adafruit_CharLCD(pin_rs=26, pin_e=19, pins_db=[13,6,5,11])
lcd.clear()
lcd.message("Hello world !!!")
