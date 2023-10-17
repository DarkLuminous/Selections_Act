import os
from time import sleep

def Chinese_Zodiac_Sign():
    Brt_year = input("Year of Birth:")

    base_year = 1990
    zodiac = str()
    z_pick = (int(Brt_year) - base_year) % 12 + 1

    if z_pick == 1:
        zodiac = ("Horse") 
    
    elif z_pick == 2:
        zodiac = ("Goat")  
    
    elif z_pick == 3:
        zodiac = ("Monkey")   
    
    elif z_pick == 4:
        zodiac = ("Rooster")  
    
    elif z_pick == 5:
        zodiac = ("Dog")  
    
    elif z_pick == 6:
        zodiac = ("Pig") 
    
    elif z_pick == 7:
        zodiac = ("Rat")
    
    elif z_pick == 8:
        zodiac = ("Ox") 
    
    elif z_pick == 9:
        zodiac = ("Tiger")
    
    elif z_pick == 10:
        zodiac = ("Rabit")
    
    elif z_pick == 11:
        zodiac = ("Dragon")
    
    elif z_pick == 12:
        zodiac = ("Snake")
    print("Your zodiac sign is", zodiac)
    input("Press any Key To CONTINUE . . .")
    sleep(2)
    os.system('cls')
    _Again()

def _Again():
    _again = input("Again? 1/YES|2/NO :")
 
    if int(_again) == 1:
     print("Wait for a seconds")
     sleep(2)
     os.system('cls')
     Chinese_Zodiac_Sign()
        
    elif int(_again) == 2:
     print("Thank You!")
        
Chinese_Zodiac_Sign()