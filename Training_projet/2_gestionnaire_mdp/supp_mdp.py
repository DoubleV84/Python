# -*- coding: utf-8 -*-
#Created by Willipatafoul at 16:59 on 21/06/2023
#
import time

def supprimer_mdp(mots_de_passe):
    time.sleep(0.5)
    supp_mdp = input("Mdp de quel service voulez vous supprimer ? ")
    time.sleep(0.5)
    
    for mot_de_passe in mots_de_passe:
        if mot_de_passe["Service"] == supp_mdp:
            choix_def = input(f"Etes-vous sur de vouloir supprimer le mot de passe pour le service {supp_mdp} ? (y/n) ").lower()
            time.sleep(0.5)

            if choix_def == "y":
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                mots_de_passe.remove(mot_de_passe)
                print("Mot de passe supprimé avec succès !")
                time.sleep(1)
                break
            else:
                time.sleep(0.5)
                print("La supprimation à été annulée.")
                time.sleep(1)
                break
        else:
            time.sleep(1)
            print("Aucun service correspondant n'a été trouvé.")
            time.sleep(1)
            