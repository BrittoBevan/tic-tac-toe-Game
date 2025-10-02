import random
def ifwin(a):
        if (a[0][1]!=0)and a[0][1]== a[1][1]==a[2][1]:
                if a[0][1]==c:
                    return "computer wins"
                else:
                    return "player wins"
        elif (a[0][0]!=0) and a[0][0]== a[1][1]==a[2][2]:
            if a[0][0]==c:
                return "computer wins"
            else:
                return "player wins"
        elif (a[0][2]!=0) and a[0][2]== a[1][1]==a[2][0]:
            if a[0][2]==c:
                return "computer wins"
            else:
                return "player wins"
        elif (a[0][0]!=0) and a[0][0]==a[0][1]==a[0][2]:
            if a[0][0]==c:
                return "computer wins"
            else:
                return "player wins"
        elif (a[1][0]!=0) and a[1][0]==a[1][1]==a[1][2]:
            if a[1][0]==c:
                return "computer wins"
            else:
                return "player wins"
        elif (a[2][0]!=0) and a[2][0]==a[2][1]==a[2][2]:
            if a[2][0]==c:
                return "computer wins"
            else:
                return "player wins"
        elif (a[0][1]!=0) and a[0][1]==a[1][0]==a[2][0]:
            if a[0][1]==c:
                return "computer wins"
            else:
                return "player wins"
        elif (a[0][1]!=0) and a[0][1]==a[1][1]==a[2][1]:
            if a[0][1]==c:
                return "computer wins"
            else:
                return "player wins"
        elif (a[0][2]!=0) and a[0][2]==a[1][2]==a[2][2]:
            if a[0][2]==c:
                return "computer wins"
            else:
                return "player wins"
        else:
            co=0
            for i in range(0,3):
                for j in range(0,3):
                    if a[i][j]==c or a[i][j]==w:
                        co+=1
                    else:
                        continue
            if co==9:
                return "Draw"
a=[[0,0,0],[0,0,0],[0,0,0]]
choice=int(input("Do you wanna play against a computer(1) or an offline game(2): "))
if (choice==1):
    while True:
        w=input("Do u want X/Q: ")
        if w=="x" or w=="X":
            c="Q"
            break
        elif w=="q" or w=="Q":
            c="X"
            break
        else:
            continue
    while True:
        x=int(input("Enter the row: "))
        y=int(input("Enter the column: "))
        if a[x-1][y-1]!=c:
            a[x-1][y-1]=w
        else:
            print("It is already full pick another cell")
            continue
        d=ifwin(a)
        if (d=="player wins" or d=="computer wins" or d=="Draw"):
            print(d)
            break
        #With Computer
        while True:
            c1=random.randint(0,2)
            c2=random.randint(0,2)
            if a[c1][c2]==w:
                continue
            elif a[c1][c2]==c:
                continue
            else:
                a[c1][c2]=c
                break
        for i in range(0,3):
            for j in range(0,3):
                print(a[i][j],end="_|")
                if j==2:
                    print("")
#2 Player 
else:
    while True:
        w=input("Player 1 u want X/Q: ")
        if w=="x" or w=="X":
            c="Q"
            print("Player 2 is ",c)
            break
        elif w=="q" or w=="Q":
            c="X"
            print("Player 2 is ",c)
            break
        else:
            continue
    while True:
        x=int(input("P1 Enter the row: "))
        y=int(input("P1 Enter the column: "))
        if a[x-1][y-1]!=c:
            a[x-1][y-1]=w
        else:
            print("It is already full pick another cell")
            continue
        for i in range(0,3):
            for j in range(0,3):
                print(a[i][j],end="_|")
                if j==2:
                    print("")
        d=ifwin(a)
        if (d=="player wins" or d=="computer wins" or d=="Draw"):
            if d=="player wins":
                print("Player 1 Wins")
                break
            else:
                print(d)
                break
        x1=int(input("P2 Enter the row: "))
        y1=int(input("P2 Enter the column: "))
        if a[x1-1][y1-1]!=w:
            a[x1-1][y1-1]=c
        else:
            print("It is already full pick another cell")
            continue
        for i in range(0,3):
            for j in range(0,3):
                print(a[i][j],end="_|")
                if j==2:
                    print("")
        d=ifwin(a)
        if (d=="player wins" or d=="computer wins" or d=="Draw"):
            if d=="computer wins":
                print("Player 2 wins")
                break
            else:
                print(d)
                break
