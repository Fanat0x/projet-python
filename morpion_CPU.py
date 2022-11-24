#DEBUT

import random
import tkinter

#Je définis une matrice en 3 par 3
matrix = [[0,0,0],[0,0,0],[0,0,0]]
#Je définis une liste pour stocker mes joueur
player = []

global CPU_possibility, playerName
CPU_possibility = 1
playerName = ""

def reinit_matrix(matrix):
    for i in range(3):
        for y in range(3):
            matrix[i][y]=0

def bot(grille,bot_type,human_type):
    #Je met le renvoie de la fonction gagner dans idxBotWin
    idxBotWin = gagner(grille, bot_type)
    #Je met le renvoie de la fonction gagner dans idxPlayerWin
    idxPlayerWin = gagner(grille, human_type)
    #Je met le renvoie de la fonction pasGagner dans idxBotCoup
    idxBotCoup = pasGagner(grille, human_type)
    #Je definie CPU-pissobility comme variable globale
    global CPU_possibility 
    #Si CPU_possibility est égale à 1
    if CPU_possibility == 1:
        #Si le milieu est vide
        if grille[1][1] == 0:
            #Alors prendre le milieu
            grille[1][1] = bot_type
            #CPU_possibility = 2
            CPU_possibility = 2
        #Sinon
        else:
            #Alors prendre la case en haut à gauche
            grille[0][0] = bot_type
            #CPU_possibility = 3
            CPU_possibility = 3
    #Sinon si idxBotWin est different d'une liste vide
    elif idxBotWin != []:
        #Ecrire "bot win"
        print("bot win")
        #jouer au rang idxBotWin (que renvoie la fonction gagner)
        grille[idxBotWin[0]][idxBotWin[1]] = bot_type
    #Sinon si idxPlayerWin est different d'une liste vide
    elif idxPlayerWin != []:
        #jouer au rang idxBotWin (que renvoie la fonction gagner)
        grille[idxPlayerWin[0]][idxPlayerWin[1]] = bot_type
    #Si CPU_possibility est égale à 1
    elif CPU_possibility == 2:
        #Si deuxParmiQuatre est égale à vrai
        if deuxParmiQuatre(grille, human_type) == True:
            grille[0][2] = bot_type
        #Sinon si la case du haut est vide
        elif grille[0][1] == 0:
            #Alors jouer en haut
            grille[0][1] = bot_type
        #Sinon
        else:
            #Alors jouer en haut
            grille[1][0] = bot_type
        #CPU_possibility = 3
        CPU_possibility = 3
    #Sinon si idxBotCoup est different d'une liste vide
    elif idxBotCoup != []:
        #jouer au rang idxBotCoup (que renvoie la fonction gagner)
        grille[idxBotCoup[0]][idxBotCoup[1]] = bot_type
    #Sinon
    else:
        #Si la case du haut est vide
        if grille[0][1] == 0:
            #Alors jouer en haut
            grille[0][1] = bot_type
        #Sinon si la case de gauche est vide
        elif grille[1][0] == 0:
            #Alors jouer à gauche
            grille[1][0] = bot_type
        #Sinon si la case de droite est vide
        elif grille[1][2] == 0:
            #Alors jouer à droite
            grille[1][2] = bot_type
        #Sinon
        else:
            #Alors jouer en bas
            grille[2][1] = bot_type
    
    return grille

#Je définis une fonction pasGagner qui a en argument la matrice et la forme (X-O)
def deuxParmiQuatre(grille, frm):
    #Si deux aretes non opposé sont prises et que les deux autres sont vides
    if grille[0][1] == grille[1][2] == frm and grille[2][1] == grille[1][0] == 0:
        #Je renvoie vrai
        return True
    #Sinon si deux aretes non opposé sont prises et que les deux autres sont vides
    elif grille[1][2] == grille[2][1] == frm and grille[1][0] == grille[0][1] == 0:
        #Je renvoie vrai
        return True
    #Sinon si deux aretes non opposé sont prises et que les deux autres sont vides
    elif grille[2][1] == grille[1][0] == frm and grille[0][1] == grille[1][2] == 0:
        #Je renvoie vrai
        return True
    #Sinon si deux aretes non opposé sont prises et que les deux autres sont vides
    elif grille[1][0] == grille[0][1] == frm and grille[1][2] == grille[2][1] == 0:
        #Je renvoie vrai
        return True
    #Je renvoie faux
    return False

#Je définis une fonction unParmiTrois qui a en argument 3 cases de la matrice et la forme (X-O)
def deuxParmiTrois(a, b, c, player):
    #Si a et b sont prises ET que c est vide
    if a == b == player and c == 0:
        #Alors je renvoie l'index de la case qu'il faut remplir 
        return[True, 2]
    #Sinon si c et b sont prises ET que b est vide
    elif c == a == player and b == 0:
        #Alors je renvoie l'index de la case qu'il faut remplir 
        return[True, 1]
    #Sinon si a et b sont prises ET que c est vide
    elif b == c == player and a == 0:
        #Alors je renvoie l'index de la case qu'il faut remplir 
        return[True, 0]
    #Sinon
    else:
        #Alors je renvoie faux
        return[False]

#Je définis une fonction unParmiTrois qui a en argument 3 cases de la matrice et la forme (X-O)
def unParmiTrois(a, b, c, player):
    #Si a est prise ET que b et c sont vides
    if a == player and b == c == 0:
        #Alors je renvoie l'index de la case qu'il faut remplir 
        return[True, 2]
    #Sinon si c est prise ET que a et b sont vides OU b est pris ET que c et a sont vides
    elif (c == player and a == b == 0) or (b == player and c == a == 0):
        #Alors je renvoie l'index de la case qu'il faut remplir 
        return[True, 0]
    #Sinon
    else:
        #Alors je renvoie faux
        return[False]

#Je définis une fonction pasGagner qui a en argument la matrice et la forme (X-O)
def gagner(grille, player):
    #Tant que i<3
    for i in range(3):
        #Je met le renvoie de la fonction deuxParmiTrois dans ligne
        ligne = deuxParmiTrois(grille[i][0], grille[i][1], grille[i][2], player)
        #Si ligne d'index 0 est égale à Vrai
        if ligne[0] == True:
            #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
            return i, ligne[1]
        #Je met le renvoie de la fonction deuxParmiTrois dans colone
        colone = deuxParmiTrois(grille[0][i], grille[1][i], grille[2][i], player)
        #Si ligne d'index 0 est égale à Vrai
        if colone[0] == True:
            #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
            return colone[1], i
    #Je met le renvoie de la fonction unParmiTrois dans diagoUn
    diagoUn = deuxParmiTrois(grille[0][0], grille[1][1], grille[2][2], player)
    #Je met le renvoie de la fonction unParmiTrois dans diagoDeux
    diagoDeux = deuxParmiTrois(grille[0][2], grille[1][1], grille[2][0], player)
    #Si ligne d'index 0 est égale à Vrai
    if diagoUn[0] == True:
        #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
        return diagoUn[1], diagoUn[1]
    #Si ligne d'index 0 est égale à Vrai
    if diagoDeux[0] == True:
        #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
        return diagoDeux[1], 2-diagoDeux[1]
    #Renvoyer liste vide si il n'y a pas d'index
    return []

#Je définis une fonction pasGagner qui a en argument la matrice et la forme (X-O)
def pasGagner(grille, player):
    #Je met le renvoie de la fonction unParmiTrois dans ligne
    ligne = unParmiTrois(grille[0][0], grille[0][1], grille[0][2], player)
    #Si ligne d'index 0 est égale à Vrai
    if ligne[0] == True:
        #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
        return 0, ligne[1]
    #Je met le renvoie de la fonction unParmiTrois dans ligne
    ligne = unParmiTrois(grille[2][0], grille[2][1], grille[2][2], player)
    #Si ligne d'index 0 est égale à Vrai
    if ligne[0] == True:
        #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
        return 2, ligne[1]
    #Je met le renvoie de la fonction unParmiTrois dans colone
    colone = unParmiTrois(grille[0][0], grille[1][0], grille[2][0], player)
    #Si ligne d'index 0 est égale à Vrai
    if colone[0] == True:
        #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
        return colone[1], 0
    #Je met le renvoie de la fonction unParmiTrois dans colone
    colone = unParmiTrois(grille[0][2], grille[1][2], grille[2][2], player)
    #Si ligne d'index 0 est égale à Vrai
    if colone[0] == True:
        #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
        return colone[1], 2
    #Je met le renvoie de la fonction unParmiTrois dans diagoUn
    diagoUn = unParmiTrois(grille[0][0], grille[1][1], grille[2][2], player)
    #Je met le renvoie de la fonction unParmiTrois dans diagoDeux
    diagoDeux = unParmiTrois(grille[0][2], grille[1][1], grille[2][0], player)
    #Si ligne d'index 0 est égale à Vrai
    if diagoUn[0] == True:
        #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
        return diagoUn[1], diagoUn[1]
    #Si ligne d'index 0 est égale à Vrai
    if diagoDeux[0] == True:
        #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
        return diagoDeux[1], diagoDeux[1]
    #Renvoyer liste vide si il n'y a pas d'index
    return []

#Je définis une fonction pasGagnerCote qui a en argument la matrice
def pasGagnerCote(grille, player):
    #Je met le renvoie de la fonction unParmiTrois dans ligne
    ligne = unParmiTrois(grille[1][0], grille[1][1], grille[1][2], player)
    #Si ligne d'index 0 est égale à Vrai
    if ligne[0] == True:
        #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
        return 1, ligne[1]
    #Je met le renvoie de la fonction unParmiTrois dans ligne
    colone = unParmiTrois(grille[0][1], grille[1][1], grille[2][1], player)
    #Si colone d'index 0 est égale à Vrai
    if colone[0] == True:
        #Alors je renvoie l'index de la case de la matrice que me renvoie la fonction
        return colone[1], 1
    #Renvoyer liste vide si il n'y a pas d'index
    return []


#Je définis une fonction Draw qui a en argument la matrice
def draw(matrix):
    leStrr = "   1  2  3\n"
    lettre = ["A" , "B", "C"]
    for i in range(3):
        ligne = lettre[i] + " "
        for y in range(3):
            if matrix[i][y] == 1:
                ligne += " X "
            elif matrix[i][y] == 2:
                ligne += " O "
            else:
                ligne += " _ "
        leStrr += ligne + "\n"
    print(leStrr[:-1])


    

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
    global playerName
    #Je definis coup et lui attribut une entrer terminal
    coup=input ("veuillez rentrer la case ou vous voulez jouer (a1 à c3) : ")
    #Si coup n'est pas une "case"
    if coup not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"] :
        #imprimer ""
        print("Veuillez verifiez l'orthographe")
        #Je rappelle la fonction action avec en argument le meme player_type
        action(player_type)
    #Sinon si le coup est a1 et que la parcelle est vide 
    elif (coup == "a1" and matrix[0][0]==0) or (coup == "a1" and playerName == "Dieu"):
        #alors je met un 1 dans la matrice
        matrix[0][0]=player_type
    #Sinon si le coup est a2 et que la parcelle est vide 
    elif (coup == "a2" and matrix[0][1]==0) or (coup == "a2" and playerName == "Dieu"):
        #alors je met un 1 dans la matrice
        matrix[0][1]=player_type
    #Sinon si le coup est a3 et que la parcelle est vide 
    elif (coup == "a3" and matrix[0][2]==0) or (coup == "a3" and playerName == "Dieu"):
        #alors je met un 1 dans la matrice
        matrix[0][2]=player_type
    #Sinon si le coup est b1 et que la parcelle est vide 
    elif (coup == "b1" and matrix[1][0]==0) or (coup == "b1" and playerName == "Dieu"):
        #alors je met un 1 dans la matrice
        matrix[1][0]=player_type
    #Sinon si le coup est b2 et que la parcelle est vide 
    elif (coup == "b2" and matrix[1][1]==0) or (coup == "b2" and playerName == "Dieu"):
        #alors je met un 1 dans la matrice
        matrix[1][1]=player_type
    #Sinon si le coup est b3 et que la parcelle est vide 
    elif (coup == "b3" and matrix[1][2]==0) or (coup == "b3" and playerName == "Dieu"):
        #alors je met un 1 dans la matrice
        matrix[1][2]=player_type
    #Sinon si le coup est c1 et que la parcelle est vide 
    elif (coup == "c1" and matrix[2][0]==0) or (coup == "c1" and playerName == "Dieu"):
        #alors je met un 1 dans la matrice
        matrix[2][0]=player_type
    #Sinon si le coup est c2 et que la parcelle est vide 
    elif (coup == "c2" and matrix[2][1]==0) or (coup == "c2" and playerName == "Dieu"):
        #alors je met un 1 dans la matrice
        matrix[2][1]=player_type
    #Sinon si le coup est c3 et que la parcelle est vide 
    elif (coup == "c3" and matrix[2][2]==0) or (coup == "c3" and playerName == "Dieu"):
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

def action_CPU(player_type,coup):
    #Je definis coup et lui attribut une entrer terminal
    #Si coup n'est pas une "case"
    if coup not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"] :
    #imprimer ""
        print("(CPU) Probleme orthographe sale con")
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
        print("(CPU) Probleme disponibiliter du slot gros noob")
    #J'appeller la fonction Draw avec matrice en argument
        draw(matrix)
    #Je re appeller la fonction action avec type_player en argument
        action(player_type)


#Je definis la fonction morpions qui prend 1 argument matrice. 
def morpion(matrix):
    global CPU_possibility, playerName
    reinit_matrix(matrix)
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
        playerName = pseudo_b
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
    round=0
    #Tant que la variable game vaut Vrai 
    while game==True:
        #Alors j'incrémente player_turn
        round=round+1
        #je definis et redefinis condition
        condition=""

        #Si player turn est pair 
        if (round%2)==0 and player[0]!="CPU":
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
        elif (round%2)==0 and player[0]=="CPU" :
            print("C'est au",player[0],"de jouez /n")
            #action_CPU(1,bot(matrix,CPU_possibility))
            matrix = bot(matrix,1,2)
            draw(matrix)
            condition=verify(matrix)
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
        elif (round%2)==1 and player[1]!="CPU":
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
        else :
            print("C'est au",player[1],"de jouez \n")
            matrix = bot(matrix,2,1)
            draw(matrix)
            condition=verify(matrix)
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

    #Après la bocle tant que je donne a la variable game_e une entrer terminal
    game_e=input("voulez-vous rejouez ?(oui/non) : ") 
    #Si l'entrer terminal vaut "oui"
    if game_e=="oui":
        reinit_matrix(matrix)
        CPU_possibility = 1
        random.shuffle(player)
        #alors je relance la fonction morpion avec matric en argument
        morpion(matrix)
    #sinon
    else: 
        #j'ecrit 
        print("au revoir\n")
        
#J'appelle la fonction morpion avec la matrice en argument 
morpion(matrix)



#FIN
