# Computer game!

x = 1
y = 1
printDirection=True 

while True:

    if printDirection==True:
        if (x==1 and y==1):
            print("You can travel: (N)orth.")                      #þarf að reyna að losa mig við að þetta prenti alltaf. Á bara að prentast í byrjun
        if (x==1 and y==2):
            print("You can travel: (N)orth or (E)ast or (S)outh.")     
        if (x==1 and y==3):
            print("You can travel: (E)ast or (S)outh.")
        if (x==2 and y == 1):
            print("You can travel: (N)orth.")
        if (x==2 and y==2):
            print("You can travel: (W)est or (S)outh.")     
        if (x==2 and y==3):
            print("You can travel: (E)ast or (W)est.")
        if (x==3 and y==1):
            print("Victory! ") #Þarf að finna út hvernig forritið getur hætt keyrslu eftir þessa prentun
            exit()                
        if (x==3 and y==2):
            print("You can travel: (N)orth or (S)outh.")
        if (x==3 and y==3):
            print("You can travel: (W)est or (S)outh.")          




    direction = (input("Direction: ")).lower()

    #Skigreini skilyrði ef input er (N)orth

    if direction == "n":
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


    # Skilgreini skilyrði ef input er (S)outh

    if direction == "s":
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
    # Skilgreini skilyrði ef input er (E)ast

    if direction == "e":
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
    # skilgreini skilyrði ef unput er (W)est

    if direction == "w":
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












