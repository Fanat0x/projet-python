#DEBUT


#On admet une fonction random qui renvoie un chiffre entre 0 et 2
from random import*
#On admet une fonction input qui renvoie l'entrer du joueur

#Je definis la liste score qui comprend [0,0]
score=[0,0]

#Je definis une list coups qui comprend "Pierre", "Feuille", "Ciseau"
coups=["pierre","feuille","ciseau"]

#je definis un fonction machineAléatoire
def machineAleatoire():
    # je definis RandInt le retour de l'execution de la fonction random
    
    #Je définis et j'assigne a coupMachine un éléments de coups avet pour index randInt
    coupMachine=coups[randint(0,2)]
    #Je retourn coupMachine
    return coupMachine



#Je defninis PierreFeuilleCiseau avec deux argument coupMachine et score
def PierreFeuilleCiseau(coupMachine,score):

    #Je definis coupJoueur avec le retour de l'execution de la fonction input
    coupJoueur=input("Que voulez vous jouez ? exemple pierre, feuille, ciseau :")

    #Si coupJoueur est égal a coupMachine
    if coupJoueur==coupMachine:
        #alors ecrire"La machine a aussi jouer" coupMachine " c'est une egaliter."
        print("La machine a aussi jouer ",coupMachine," c'est une egaliter.")
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        rejouez=input("voulez vous rejouez ? [oui/non] : ")
        #Si rejouez est egal a "oui" 
        if rejouez=="oui":
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
            PierreFeuilleCiseau(machineAleatoire(),score)
        #Sinon 
        else:
            #alors ecrire "tu as "score[0] "la machine a " score[1]
            print("tu as ",score[0]," la machine a ",score[1])

    #Sinon si coupJoueur est egal a "Pierre" ET coupMachine est egal a "Ciseau"
    elif coupJoueur=="pierre" and coupMachine=="ciseau":
        #ALors ecrire"La machine a choisi" coupMachine "tu as gagner !"
        print("La machine a choisi",coupMachine,"tu as gagner !")
        #assigner a score[0] +1
        score[0]=score[0]+1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        rejouez=input("voulez vous rejouez ? [oui/non] : ")
        #Si rejouez est egal a "oui" 
        if rejouez=="oui":
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
            PierreFeuilleCiseau(machineAleatoire(),score)
        #Sinon 
        else:
            #alors ecrire "tu as "score[0] "la machine a " score[1]
            print("tu as ",score[0]," la machine a ",score[1])

    #Sinon si coupJoueur est egal a "Pierre" ET coupMachine est egal a "Ciseau"
    elif coupJoueur=="feuille" and coupMachine=="pierre":
        #ALors ecrire"La machine a choisi" coupMachine "tu as gagner !"
        print("La machine a choisi",coupMachine,"tu as gagner !")
        #assigner a score[0] +1
        score[0]=score[0]+1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        rejouez=input("voulez vous rejouez ? [oui/non] : ")
        #Si rejouez est egal a "oui" 
        if rejouez=="oui":
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
            PierreFeuilleCiseau(machineAleatoire(),score)
        #Sinon 
        else:
            #alors ecrire "tu as "score[0] "la machine a " score[1]
            print("tu as ",score[0]," la machine a ",score[1])

    #Sinon si coupJoueur est egal a "Pierre" ET coupMachine est egal a "Ciseau"
    elif coupJoueur=="ciseau" and coupMachine=="feuille":
        #ALors ecrire"La machine a choisi" coupMachine "tu as gagner !"
        print("La machine a choisi",coupMachine,"tu as gagner !")
        #assigner a score[0] +1
        score[0]=score[0]+1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        rejouez=input("voulez vous rejouez ? [oui/non] : ")
        #Si rejouez est egal a "oui" 
        if rejouez=="oui":
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
            PierreFeuilleCiseau(machineAleatoire(),score)
        #Sinon 
        else:
            #alors ecrire "tu as "score[0] "la machine a " score[1]
            print("tu as ",score[0]," la machine a ",score[1])


    #Sinon si coupJoueur est egal a "Pierre" ET coupMachine est egal a "Ciseau"
    elif coupMachine=="pierre" and coupJoueur=="ciseau":
        #ALors ecrire"La machine a choisi" coupMachine "tu as gagner !"
        print("La machine a choisi",coupMachine,"tu as perdu ...")
        #assigner a score[0] +1
        score[1]=score[1]+1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        rejouez=input("voulez vous rejouez ? [oui/non] : ")
        #Si rejouez est egal a "oui" 
        if rejouez=="oui":
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
            PierreFeuilleCiseau(machineAleatoire(),score)
        #Sinon 
        else:
            #alors ecrire "tu as "score[0] "la machine a " score[1]
            print("tu as ",score[0]," la machine a ",score[1])

    #Sinon si coupJoueur est egal a "Pierre" ET coupMachine est egal a "Ciseau"
    elif coupMachine=="feuille" and coupJoueur=="pierre":
        #ALors ecrire"La machine a choisi" coupMachine "tu as gagner !"
        print("La machine a choisi",coupMachine,"tu as perdu ...")
        #assigner a score[0] +1
        score[1]=score[1]+1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        rejouez=input("voulez vous rejouez ? [oui/non] : ")
        #Si rejouez est egal a "oui" 
        if rejouez=="oui":
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
            PierreFeuilleCiseau(machineAleatoire(),score)
        #Sinon 
        else:
            #alors ecrire "tu as "score[0] "la machine a " score[1]
            print("tu as ",score[0]," la machine a ",score[1])

    #Sinon si coupJoueur est egal a "Pierre" ET coupMachine est egal a "Ciseau"
    elif coupMachine=="ciseau" and coupJoueur=="feuille":
        #ALors ecrire"La machine a choisi" coupMachine "tu as gagner !"
        print("La machine a choisi",coupMachine,"tu as perdu ...")
        #assigner a score[0] +1
        score[1]=score[1]+1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        rejouez=input("voulez vous rejouez ? [oui/non] : ")
        #Si rejouez est egal a "oui" 
        if rejouez=="oui":
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
            PierreFeuilleCiseau(machineAleatoire(),score)
        #Sinon 
        else:
            #alors ecrire "tu as "score[0] "la machine a " score[1]
            print("tu as ",score[0]," la machine a ",score[1])

    #Sinon 
    else:
        #ecrire "verifie l'orthographe s'il te plait, il faut ecrire tel que" coups
        print("verifie l'orthographe s'il te plait, il faut ecrire tel que pierre, feuille ou ciseau ")
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        rejouez=input("voulez vous rejouez ? [oui/non] : ")
        #Si rejouez est egal a "oui" 
        if rejouez=="oui":
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
            PierreFeuilleCiseau(machineAleatoire(),score)
        #Sinon 
        else:
            #alors ecrire "tu as "score[0] "la machine a " score[1]
            print("tu as ",score[0]," la machine a ",score[1])

#J'execute la fonction PierreFeuilleCiseau avec le retour de la fonction machineAleatoire en premier argument et la list score en deuxieme argument 
PierreFeuilleCiseau(machineAleatoire(),score)



#FIN