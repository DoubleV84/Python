# -*- coding: utf-8 -*-
#Created by Willipatafoul at 16:52 on 21/06/2023
#
import time

def afficher_mdp(mots_de_passe):
    if mots_de_passe:
        time.sleep(1)
        print("\nListe des mots de passe :\n")
        time.sleep(1)
        
        for i, mot_de_passe in enumerate(mots_de_passe, start=1):
            print(f"{i}. Service : {mot_de_passe['Service']}")
            print(f"   Mot de passe : {mot_de_passe['Mot_de_passe']}")
            print() 
        time.sleep(1)
    else:
        time.sleep(2)
        print("Désolé, il n'y a aucun mots de passe..")
        time.sleep(2)