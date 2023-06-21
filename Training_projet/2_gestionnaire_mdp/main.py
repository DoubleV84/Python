# -*- coding: utf-8 -*-
#Created by Willipatafoul at 15:54 on 21/06/2023
#
from menu import menu_principal
from ajout_mdp import ajout_mdp
from supp_mdp import supprimer_mdp
from afficher_mdp import afficher_mdp
from recherche_mdp import recherche_mdp
import time

def main():

    mots_de_passe = []
    
    while True:
        choix = menu_principal()
        
        if choix == "1":
            ajout_mdp(mots_de_passe)
        elif choix == "2":
            supprimer_mdp(mots_de_passe)
        elif choix == "3":
            afficher_mdp(mots_de_passe)
        elif choix == "4":
            recherche_mdp(mots_de_passe)
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Erreur veuillez entrer une valeur correcte !")
            time.sleep(1)
            

if __name__ == '__main__':
    main()