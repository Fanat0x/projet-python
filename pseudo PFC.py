#DEBUT


#On admet une fonction random qui renvoie un chiffre entre 0 et 2
#On admet une fonction input qui renvoie l'entrer du joueur
#Je definis la liste score qui comprend [0,0]

#Je definis une list coups qui comprend "Pierre", "Feuille", "Ciseau"

#je definis un fonction machineAléatoire
    # je definis RandInt le retour de l'execution de la fonction random
    #Je définis et j'assigne a coupMachine un éléments de coups avet pour index randInt
    #Je retourn coupMachine



#Je defninis PierreFeuilleCiseau avec deux argument coupMachine et score

    #Je definis coupJoueur avec le retour de l'execution de la fonction input

    #Si coupJoueur est égal a coupMachine
        #alors ecrire"La machine a aussi jouer" coupMachine " c'est une egaliter."
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        #Si rejouez est egal a "oui" 
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
        #Sinon 
            #alors ecrire "tu as "score[0] "la machine a " score[1]

    #Si coupJoueur est egal a "Pierre" ET coupMachine est egal a "Ciseau"
        #ALors ecrire"La machine a choisi" coupMachine "tu as gagner !"
        #assigner a score[0] +1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        #Si rejouez est egal a "oui" 
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
        #Sinon 
            #alors ecrire "tu as "score[0] "la machine a " score[1]

    #Si coupJoueur est egal a "Feuille" ET coupMachine est egal a "Pierre"
        #ALors ecrire"La machine a choisi" coupMachine "tu as gagner !"
        #assigner a score[0] +1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        #Si rejouez est egal a "oui" 
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
        #Sinon 
            #alors ecrire "tu as "score[0] "la machine a " score[1]

    #Si coupJoueur est egal a "Ciseau" ET coupMachine est egal a "Feuille"
        #ALors ecrire"La machine a choisi" coupMachine "tu as gagner !"
        #assigner a score[0] +1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        #Si rejouez est egal a "oui" 
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
        #Sinon 
            #alors ecrire "tu as "score[0] "la machine a " score[1]


    #Si coupMachine est egal a "Pierre" ET coupJoueur est egal a "Ciseau"
        #ALors ecrire"La machine a choisi" coupMachine "tu as perdu ..."
        #assigner a score[1] +1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        #Si rejouez est egal a "oui" 
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
        #Sinon 
            #alors ecrire "tu as "score[0] "la machine a " score[1]

    #Si coupMachine est egal a "Feuille" ET coupJoueur est egal a "Pierre"
        #ALors ecrire"La machine a choisi" coupMachine "tu as perdu ..."
        #assigner a score[1] +1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        #Si rejouez est egal a "oui" 
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
        #Sinon 
            #alors ecrire "tu as "score[0] "la machine a " score[1]

    #Si coupMachine est egal a "Ciseau" ET coupJoueur est egal a "Feuille"
        #ALors ecrire"La machine a choisi" coupMachine "tu as perdu ..."
            #assigner a score[1] +1
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        #Si rejouez est egal a "oui" 
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
        #Sinon 
            #alors ecrire "tu as "score[0] "la machine a " score[1]

    #Sinon 
        #ecrire "verifie l'orthographe s'il te plait, il faut ecrire tel que" coups
        #assigner a rejouez l'execution de la fonction input "Voulez vous rejouez ? [oui/non] : "
        #Si rejouez est egal a "oui" 
            #alors j'execute PierreFeuilleCiseau en rappelant la fonction machineAléatoire et en utilisant le nouveau score
        #Sinon 
            #alors ecrire "tu as "score[0] "la machine a " score[1]





#FIN