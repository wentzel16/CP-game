# Computer game

x = 1
y = 1

while True:
    if (x==1 and y==1):
         print("You can travel (N)orth:")                      #þarf að reyna að losa mig við að þetta prenti alltaf. Á bara að prentast í byrjun
    if (x==1 and y==2):
         print("You can travel (N)orth or (E)ast or (S)outh")     
    if (x==1 and y==3):
        print("You can travel (E)ast or (S)outh")
    if (x==2 and y == 1):
        print("You can travel (N)orth")
    if (x==2 and y==2):
        print("You can travel (W)est or (S)outh")     
    if (x==2 and y==3):
        print("You can travel (E)ast or (W)est")
    if (x==3 and y==1):
        print("Victory!")
        exit                         
    if (x==3 and y==2):
        print("You can travel (N)orth or (S)outh")
    if (x==3 and y==3):
        print("You can travel (W)est or (S)outh")          




    direction = (input("Direction: "))

    #Skigreini skilyrði ef input er (N)orth

    if direction == "n":
        if y < 3:
            y+=1
            print(x,y)
            # print("You can travel")


    # Skilgreini skilyrði ef input er (S)outh

    if direction == "s":
        if y > 1:
            y-=1
            print(x,y)
            # print("You can travel")

    # Skilgreini skilyrði ef input er (E)ast

    if direction == "e":
        if x < 3:
            x+=1
            print(x,y)
            # print("You can travel")

    # skilgreini skilyrði ef unput er (W)est

    if direction == "w":
        if x > 1:
            x-=1
            print(x,y)
            # print("You can travel")













