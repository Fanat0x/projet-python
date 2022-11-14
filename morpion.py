#DEBUT

from random import*

matrix=[[0,0,0],[0,0,0],[0,0,0]]
player=["player","player_2"]

def draw(matrix):
    for i in range(len(matrix)):
        print (matrix[i])

def verify(matrix):
    board_full=False
    if matrix[0][0]==1 and matrix[0][1]==1 and matrix[0][2]==1:
        return player[0] , "winner"
    elif matrix[1][0]==1 and matrix[1][1]==1 and matrix[1][2]==1:
        return player[0] , "winner"
    elif matrix[2][0]==1 and matrix[2][1]==1 and matrix[2][2]==1:
        return player[0] , "winner"
    elif matrix[0][0]==1 and matrix[1][1]==1 and matrix[2][2]==1:
        return player[0] , "winner"
    elif matrix[2][0]==1 and matrix[1][1]==1 and matrix[0][2]==1:
        return player[0] , "winner"
    
    elif matrix[0][0]==2 and matrix[0][1]==2 and matrix[0][2]==2:
        return player[1] , "winner"
    elif matrix[1][0]==2 and matrix[1][1]==2 and matrix[1][2]==2:
        return player[1] , "winner"
    elif matrix[2][0]==2 and matrix[2][1]==2 and matrix[2][2]==2:
        return player[1] , "winner"
    elif matrix[0][0]==2 and matrix[1][1]==2 and matrix[2][2]==2:
        return player[1] , "winner"
    elif matrix[2][0]==2 and matrix[1][1]==2 and matrix[0][2]==2:
        return player[1] , "winner"

    elif board_full==True:
        reu    
    for i in range(matrix):
        if i==0:
            board_full=True
        
    

def morpion(matrix):
    game=False
    gamee=input("voulez-vous jouez ?(oui/non) : ")
    if gamee=="oui":
        game=True
    elif gamee=="non":
        print("appuyer sur F5 pour relancer le jeu")
    else:
        print("Veuillez verifiez l'orthographe")

    while game==True:
        pseudo_a=input("Veuillez inserer votre pseudo : ")
        player.append(pseudo_a)
        pseudo_b=input("Veuillez inserer votre pseudo : ")
        player.append(pseudo_b)
        random.shuffle(player)
        print("c'est a ",player[0],"de jouez ")
        coup=input ("veuillez rentrer la case ou vous voulez jouer (a1 à c3) : ")
        if coup != "a1" or "a2" or "a3" or "b1" or "b2" or "b3" or "c1" or "c2" or "c3":
            print("Veuillez verifiez l'orthographe, et la disponibilité du slot")
        elif coup == "a1" and matrix[0][0]==0 :
            matrix[0][0].append(1)
        elif coup == "a2" and matrix[0][1]==0 :
            matrix[0][1].append(1)
        elif coup == "a3" and matrix[0][2]==0 :
            matrix[0][2].append(1)
        elif coup == "b1" and matrix[1][0]==0 :
            matrix[1][0].append(1)
        elif coup == "b2" and matrix[1][1]==0 :
            matrix[1][1].append(1)
        elif coup == "b3" and matrix[1][2]==0 :
            matrix[1][2].append(1)
        elif coup == "c1" and matrix[2][0]==0 :
            matrix[2][0].append(1)
        elif coup == "c2" and matrix[2][1]==0 :
            matrix[2][1].append(1)
        elif coup == "c3" and matrix[2][2]==0 :
            matrix[2][2].append(1)
        draw(matrix)
        condition(matrix)




        




#FIN