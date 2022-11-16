#DEBUT

import random

matrix=[[0,0,0],[0,0,0],[0,0,0]]
player=[]

def draw(matrix):
    print("---------")
    for i in range(len(matrix)):
        print (matrix[i])
    print("---------\n")

def is_board_filled(matrix):
    count=0
    for row in (matrix):
        for tile in row:    
            if tile==0:        
                count=count+1
    return count

def verify(matrix):

    allo = is_board_filled(matrix)
    if matrix[0][0]==1 and matrix[0][1]==1 and matrix[0][2]==1:
        return "win"
    elif matrix[1][0]==1 and matrix[1][1]==1 and matrix[1][2]==1:
        return "win"
    elif matrix[2][0]==1 and matrix[2][1]==1 and matrix[2][2]==1:
        return "win"
    elif matrix[0][0]==1 and matrix[1][0]==1 and matrix[2][0]==1:
        return "win"
    elif matrix[0][1]==1 and matrix[1][1]==1 and matrix[2][1]==1:
        return "win"
    elif matrix[0][2]==1 and matrix[1][2]==1 and matrix[2][2]==1:
        return "win"
    elif matrix[0][0]==1 and matrix[1][1]==1 and matrix[2][2]==1:
        return "win"
    elif matrix[2][0]==1 and matrix[1][1]==1 and matrix[0][2]==1:
        return "win"
    
    elif matrix[0][0]==2 and matrix[0][1]==2 and matrix[0][2]==2:
        return "win"
    elif matrix[1][0]==2 and matrix[1][1]==2 and matrix[1][2]==2:
        return "win"
    elif matrix[2][0]==2 and matrix[2][1]==2 and matrix[2][2]==2:
        return "win"
    elif matrix[0][0]==2 and matrix[1][0]==2 and matrix[2][0]==2:
        return "win"
    elif matrix[0][1]==2 and matrix[1][1]==2 and matrix[2][1]==2:
        return "win"
    elif matrix[0][2]==2 and matrix[1][2]==2 and matrix[2][2]==2:
        return "win"
    elif matrix[0][0]==2 and matrix[1][1]==2 and matrix[2][2]==2:
        return "win"
    elif matrix[2][0]==2 and matrix[1][1]==2 and matrix[0][2]==2:
        return "win"
    elif allo==9 :
        return "draw"

    else:
        return True

        
    
def action(player_type):
    coup=input ("veuillez rentrer la case ou vous voulez jouer (a1 à c3) : ")
    if coup not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"] :
            print("Veuillez verifiez l'orthographe")
            action(player_type)
    elif coup == "a1" and matrix[0][0]==0 :
            matrix[0][0]=player_type
    elif coup == "a2" and matrix[0][1]==0 :
            matrix[0][1]=player_type
    elif coup == "a3" and matrix[0][2]==0 :
            matrix[0][2]=player_type
    elif coup == "b1" and matrix[1][0]==0 :
            matrix[1][0]=player_type
    elif coup == "b2" and matrix[1][1]==0 :
            matrix[1][1]=player_type
    elif coup == "b3" and matrix[1][2]==0 :
            matrix[1][2]=player_type
    elif coup == "c1" and matrix[2][0]==0 :
            matrix[2][0]=player_type
    elif coup == "c2" and matrix[2][1]==0 :
            matrix[2][1]=player_type
    elif coup == "c3" and matrix[2][2]==0 :
            matrix[2][2]=player_type
    else:
        print("Verifier la disponibilité du slot")
        draw(matrix)
        action(player_type)



def morpion(matrix):
    game=False
    game_e=input("voulez-vous jouez ?(oui/non) : ")
    if game_e=="oui":
        game=True
        pseudo_a=input("Bonjour veuillez inserer le pseudo d'un premier joueur : ")
        player.append(pseudo_a)
        pseudo_b=input("Bonjour veuillez inserer le pseudo d'un deuxieme joueur : ")
        player.append(pseudo_b)
        print("\n")
        random.shuffle(player)
    elif game_e=="non":
        game=False
        print("appuyer sur F5 pour relancer le jeu")
    else:
        print("Veuillez verifiez l'orthographe")
        morpion(matrix)

    player_turn=0
    while game==True:
        player_turn=player_turn+1
        condition=""

        if (player_turn%2)==0:
            print("C'est a",player[0],"de jouez ")
            action(1)
            condition=verify(matrix)
            draw(matrix)
            if condition=="win":
                game=False
                print(player[0], "a gagner\n")

            elif condition=="draw":
                game=False
                print("c'est une egaliter le tableau est plein !\n")


        if (player_turn%2)==1:
            print("C'est a",player[1],"de jouez ")
            action(2)
            condition=verify(matrix)
            draw(matrix)
            if condition=="win":
                game=False
                print(player[1], "a gagner\n")

            elif condition=="draw":
                game=False
                print("c'est une egaliter le tableau est plein !\n")

    game_e=input("voulez-vous rejouez ?(oui/non) : ") 
    if game_e=="oui":
        morpion(matrix)
    else: 
        print("au revoir\n")
        



        



morpion(matrix)




#FIN