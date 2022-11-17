#DEBUT

import random

#Je définis une matrice en 3 par 3
matrix=[[0,0,0],[0,0,0],[0,0,0]]
#Je définis une liste pour stocker mes joueur
player=[]

#Je définis une fonction Draw qui a en argument la matrice
def draw(matrix):
    #Mise en forme
    print("---------")
    #Pour chaque lignes de ma matrice 
    for i in range(len(matrix)):
        #J'ecris la ligne
        print (matrix[i])
        #Mise en forme
    print("---------\n")

#Je definis une fonction qui vérifie si le le tableau est remplie
def is_board_filled(matrix):
    #Je créer un compteur
    count=0
    #Pour chaque ligne dans la matrice
    for row in (matrix):
        #Pour chaque parcele dans ces lignes 
        for tile in row:    
            #Si la parcele est different 0
            if tile!=0:        
                #Alors j'incrémente 1
                count=count+1
    return count

#Je definis la fonction verify
def verify(matrix):

    #Je definis la variable nb_0
    nb_0 = is_board_filled(matrix)
    #Si le joueur 1 a cocher chaque case de la ligne du haut
    if matrix[0][0]==1 and matrix[0][1]==1 and matrix[0][2]==1:
        return "win"
    #Sinon si le joueur 1 a cocher chaque case de la ligne du milieu
    elif matrix[1][0]==1 and matrix[1][1]==1 and matrix[1][2]==1:
        return "win"
    #Sinon si le joueur 1 a cocher chaque case de la ligne du bas
    elif matrix[2][0]==1 and matrix[2][1]==1 and matrix[2][2]==1:
        return "win"
    #Sinon si le joueur 1 a cocher chaque case de la colonne de gauche
    elif matrix[0][0]==1 and matrix[1][0]==1 and matrix[2][0]==1:
        return "win"
    #Sinon si le joueur 1 a cocher chaque case de la colonne du milieu
    elif matrix[0][1]==1 and matrix[1][1]==1 and matrix[2][1]==1:
        return "win"
    #Sinon si le joueur 1 a cocher chaque case de la colonne de droite
    elif matrix[0][2]==1 and matrix[1][2]==1 and matrix[2][2]==1:
        return "win"
    #Sinon si le joueur 1 a cocher chaque case de la diagonale de en haut gauche à en bas droite
    elif matrix[0][0]==1 and matrix[1][1]==1 and matrix[2][2]==1:
        return "win"
    #Sinon si le joueur 1 a cocher chaque case de la diagonale de en haut droite à en bas gauche
    elif matrix[2][0]==1 and matrix[1][1]==1 and matrix[0][2]==1:
        return "win"
    
    #Sinon si le joueur 2 a cocher chaque case de la ligne du haut
    elif matrix[0][0]==2 and matrix[0][1]==2 and matrix[0][2]==2:
        return "win"
    #Sinon si le joueur 2 a cocher chaque case de la ligne du milieu
    elif matrix[1][0]==2 and matrix[1][1]==2 and matrix[1][2]==2:
        return "win"
    #Sinon si le joueur 2 a cocher chaque case de la ligne du bas
    elif matrix[2][0]==2 and matrix[2][1]==2 and matrix[2][2]==2:
        return "win"
    #Sinon si le joueur 2 a cocher chaque case de la colonne de gauche
    elif matrix[0][0]==2 and matrix[1][0]==2 and matrix[2][0]==2:
        return "win"
    #Sinon si le joueur 2 a cocher chaque case de la colonne du milieu
    elif matrix[0][1]==2 and matrix[1][1]==2 and matrix[2][1]==2:
        return "win"
    #Sinon si le joueur 2 a cocher chaque case de la colonne de droite
    elif matrix[0][2]==2 and matrix[1][2]==2 and matrix[2][2]==2:
        return "win"
    #Sinon si le joueur 2 a cocher chaque case de la diagonale de en haut gauche à en bas droite
    elif matrix[0][0]==2 and matrix[1][1]==2 and matrix[2][2]==2:
        return "win"
    #Sinon si le joueur 2 a cocher chaque case de la diagonale de en haut droite à en bas gauche
    elif matrix[2][0]==2 and matrix[1][1]==2 and matrix[0][2]==2:
        return "win"
    #Sinon si toutes les cases du tableau sont remplise
    elif nb_0==9 :
        return "draw"
    #Sinon retourner Vrai
    else:
        return True

        
#Je definis la methode action
def action(player_type):
    #Je definis coup et lui attribut une entrer terminal
    coup=input ("veuillez rentrer la case ou vous voulez jouer (a1 à c3) : ")
    #Si coup n'est pas une "case"
    if coup not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"] :
        #imprimer ""
        print("Veuillez verifiez l'orthographe")
        #Je rappelle la fonction action avec en argument le meme player_type
        action(player_type)
    #Sinon si le coup est a1 et que la parcelle est vide 
    elif coup == "a1" and matrix[0][0]==0 :
        #alors je met un 1 dans la matrice
        matrix[0][0]=player_type
    #Sinon si le coup est a2 et que la parcelle est vide 
    elif coup == "a2" and matrix[0][1]==0 :
        #alors je met un 1 dans la matrice
        matrix[0][1]=player_type
    #Sinon si le coup est a3 et que la parcelle est vide 
    elif coup == "a3" and matrix[0][2]==0 :
        #alors je met un 1 dans la matrice
        matrix[0][2]=player_type
    #Sinon si le coup est b1 et que la parcelle est vide 
    elif coup == "b1" and matrix[1][0]==0 :
        #alors je met un 1 dans la matrice
        matrix[1][0]=player_type
    #Sinon si le coup est b2 et que la parcelle est vide 
    elif coup == "b2" and matrix[1][1]==0 :
        #alors je met un 1 dans la matrice
        matrix[1][1]=player_type
    #Sinon si le coup est b3 et que la parcelle est vide 
    elif coup == "b3" and matrix[1][2]==0 :
        #alors je met un 1 dans la matrice
        matrix[1][2]=player_type
    #Sinon si le coup est c1 et que la parcelle est vide 
    elif coup == "c1" and matrix[2][0]==0 :
        #alors je met un 1 dans la matrice
        matrix[2][0]=player_type
    #Sinon si le coup est c2 et que la parcelle est vide 
    elif coup == "c2" and matrix[2][1]==0 :
        #alors je met un 1 dans la matrice
        matrix[2][1]=player_type
    #Sinon si le coup est c3 et que la parcelle est vide 
    elif coup == "c3" and matrix[2][2]==0 :
        #alors je met un 1 dans la matrice
        matrix[2][2]=player_type
    #Sinon 
    else:
        #Je demande au joueur de verifier la disponibiliter du slot
        print("Verifier la disponibilité du slot")
        #J'appeller la fonction Draw avec matrice en argument
        draw(matrix)
        #Je re appeller la fonction action avec type_player en argument
        action(player_type)


#Je definis la fonction morpions qui prend 1 argument matrice. 
def morpion(matrix):
    #Je definis game un booleens qui est Faux 
    game=False
    #Je definis game_e une autre variable qui prend une entrer terminal 
    game_e=input("voulez-vous jouez ?(oui/non) : ")
    #Si l'entrer terminal est egal au str "oui"
    if game_e=="oui":
        #alors je definis mon booleens en Vrai
        game=True
        #Je definis une variable pseudo_a qui prend une entrer terminal
        pseudo_a=input("Bonjour veuillez inserer le pseudo d'un premier joueur : ")
        #J'ajoute a ma liste de joueur l'entrer terminal
        player.append(pseudo_a)
        #Je definis une autre variable pseudo_b qui prend une entrer terminal
        pseudo_b=input("Bonjour veuillez inserer le pseudo d'un deuxieme joueur : ")
        #J'ajoute a ma liste de joueur l'entrer terminal
        player.append(pseudo_b)
        #Mise en forme (je saute une ligne)
        print("\n")
        #J'appelle l'import random et je melange de maniere aleatoire ma liste player
        random.shuffle(player)
    #Sinon si l'entrer terminale game_e vaut "non" 
    elif game_e=="non":
        #Alors la variable game vaut Faux
        game=False
        #Et j'imprime un mesage 
        print("appuyer sur F5 pour relancer le jeu")
    #Sinon
    else:
        #Alors j'imprime un msg
        print("Veuillez verifiez l'orthographe")
        #Et je relance la faonctin morpion
        morpion(matrix)

    #Je definis une variable tour_joueur qui vaut 0
    player_turn=0
    #Tant que la variable game vaut Vrai 
    while game==True:
        #Alors j'incrémente player_turn
        player_turn=player_turn+1
        #je definis et redefinis condition
        condition=""

        #Si player turn est pair 
        if (player_turn%2)==0:
            #Alors j'ecrit ""
            print("C'est a",player[0],"de jouez ")
            #Je lance la fonction action avec le type 1 du joueur 1
            action(1)
            #Je donne a la variable condition le resultat de la fonction verify avec matrice en argument
            condition=verify(matrix)
            #J'apelle la fonction draw avec matrice en argument
            draw(matrix)
            #Si la variable condition est égale a "win"
            if condition=="win":
                #alors le booleens Game est egal a Faux
                game=False
                #Et j 'ecris ""
                print(player[0], "a gagner\n")
            
            #Sinon si condition est egal a "draw"
            elif condition=="draw":
                #alors le booleens game est aussi egal a Faux
                game=False
                #Et j'ecris ""
                print("c'est une egaliter le tableau est plein !\n")


        #Si player_turn est impair
        if (player_turn%2)==1:
            #alors j'ecris ""
            print("C'est a",player[1],"de jouez ")
            #Je lance la fonction action avec 2 comme player_type
            action(2)
            #Je donne a la variable condition le resultat de la fonction verify avec matrice en argument
            condition=verify(matrix)
            #J'apelle la fonction draw avec matrice en argument
            draw(matrix)
            #Si la variable condition est égale a "win"
            if condition=="win":
                #alors le booleens Game est egal a Faux
                game=False
                #Et j 'ecris ""
                print(player[1], "a gagner\n")

            #Sinon si condition est egal a "draw"
            elif condition=="draw":
                #alors le booleens game est aussi egal a Faux
                game=False
                #Et j'ecris ""
                print("c'est une egaliter le tableau est plein !\n")

    #Après la bocle tant que je donne a la variable game_e une entrer terminal
    game_e=input("voulez-vous rejouez ?(oui/non) : ") 
    #Si l'entrer terminal vaut "oui"
    if game_e=="oui":
        #alors je relance la fonction morpion avec matric en argument
        morpion(matrix)
    #sinon
    else: 
        #j'ecrit 
        print("au revoir\n")
        
#J'appelle la fonction matrice 
morpion(matrix)






#FIN