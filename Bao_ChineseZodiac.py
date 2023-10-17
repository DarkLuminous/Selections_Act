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

Chinese_Zodiac_Sign()

"""
_again = input("Again? 1/YES|2/NO :")
 
if _again == 1:
    Chinese_Zodiac_Sign()
        
elif _again == 2:
    print("Thank You!")
"""                 #working in Progress