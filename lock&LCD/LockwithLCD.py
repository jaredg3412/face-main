import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# declare io for LCD pins 
lcd_rs = digitalio.DigitalInOut(board.GPIO_P37)
lcd_en = digitalio.DigitalInOut(board.GPIO_P36)
lcd_d7 = digitalio.DigitalInOut(board.GPIO_P16)
lcd_d6 = digitalio.DigitalInOut(board.GPIO_P18)
lcd_d5 = digitalio.DigitalInOut(board.GPIO_P29)
lcd_d4 = digitalio.DigitalInOut(board.GPIO_P31)

#declare io pin for com terminal of relay to unlock/lock and set as output
com = digitalio.DigitalInOut(board.GPIO_P13)
com.direction = digitalio.Direction.OUTPUT

#declare relevant info for LCD initialization
lcd_columns = 16
lcd_rows = 2
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, l$

#locking/unlocking basic logic
if True:        
        lcd.message = "Access Granted"
        com.value = True
else:   
        lcd.message = "Access Denied"
        com.value = False
