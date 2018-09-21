# Computer game!

#Ég byrjaði á að hugsa með mér hvernig ég gæti leyst þær kröfur sem þarf til að útbúa leikinn. Hugsaði með mér að best væri að byrja á að gera print fyrir hvern reit fyrir sig
#og fara síðan í það að skilgreina fyrir hvaða reiti er ekki hægt að velja hverja átt. 

# Í þessari útgáfu bý ég til föll fyrir þau skilyrði sem ég bjó tilí fyrra dæmi.

# https://github.com/wentzel16/CP-game.git



def printinstructions(x,y,printDirection): #Bý til fall fyrir prentunina fyrir hvern reit

    if printDirection==True:
        if (x==1 and y==1):
            print("You can travel: (N)orth.")                
        if (x==1 and y==2):
            print("You can travel: (N)orth or (E)ast or (S)outh.")     
        if (x==1 and y==3):
            print("You can travel: (E)ast or (S)outh.")
        if (x==2 and y == 1):
            print("You can travel: (N)orth.")
        if (x==2 and y==2):
            print("You can travel: (S)outh or (W)est.")     
        if (x==2 and y==3):
            print("You can travel: (E)ast or (W)est.")
        if (x==3 and y==1):
            print("Victory! ") 
            exit()                
        if (x==3 and y==2):
            print("You can travel: (N)orth or (S)outh.")
        if (x==3 and y==3):
            print("You can travel: (S)outh or (W)est.")
            return x,y 

def n(x,y,printDirection): #Bý til fall fyrir norður
    if (x==2 and y==2) or (x==1 and y==3) or (x==2 and y==3) or (x==3 and y==3): #Skilgreint hvað má ekki velja
        print("Not a valid direction!")
        printDirection=False
    
    elif y < 3:
        printDirection=True
        y+=1
        # print(x,y)
    else:
        print("Not a valid direction!")
        printDirection=False
    return x,y,printDirection

def s(x,y,printDirection): #Bý til fall fyrir suður
    if (x==1 and y==1) or (x==2 and y==1) or (x==2 and y==3): #Skilgreint hvað má ekki velja
        print("Not a valid direction!")
        printDirection=False
    elif y > 1:
        printDirection=True            
        y-=1
        # print(x,y)
    else:
        print("Not a valid direction!")
        printDirection=False
    return x,y,printDirection
    
def e(x,y,printDirection): #Bý til fall fyrir austur
    if (x==1 and y==1) or (x==2 and y==1) or (x==2 and y==2) or (x==3 and y==3) or (x==3 and y==2): #Skilgreint hvað má ekki velja
        print("Not a valid direction!")
        printDirection=False
    elif x < 3:
        printDirection=True
        x+=1
        # print(x,y)
    else:
        print("Not a valid direction!")
        printDirection=False
    return x,y,printDirection
    
def w(x,y,printDirection): #Bý til fall fyrir vestur
    if (x==1 and y==1) or (x==1 and y==2) or (x==1 and y==3) or (x==2 and y==1) or (x==3 and y==2): #Skilgreint hvað má ekki velja
        print("Not a valid direction!")
        printDirection=False
    elif x > 1:
        printDirection=True
        x-=1
        # print(x,y)
    else:
        print("Not a valid direction!")
        printDirection=False
    return x,y,printDirection

x = 1
y = 1
printDirection=True 
while True:
    
    printinstructions(x,y,printDirection)
    direction = (input("Direction: ")).lower()
    


    #Skigreini skilyrði ef input er (N)orth
    if direction == "n":
        x, y, printDirection = n(x,y,printDirection)
    # Skilgreini skilyrði ef input er (S)outh
    if direction == "s":
        x, y, printDirection = s(x,y,printDirection)
    # Skilgreini skilyrði ef input er (E)ast
    if direction == "e":
        x, y, printDirection = e(x,y,printDirection)
    # skilgreini skilyrði ef unput er (W)est
    if direction == "w":
        x, y, printDirection = w(x,y,printDirection) 












