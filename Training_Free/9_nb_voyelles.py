# -*- coding: utf-8 -*-
#Created by Willipatafoul at 12:03 on 05/06/2023
#

def nb_voyelles(chaine):
    voyelles = ["a","e","i","o","u","y"]
    compteur = 0
    
    for i in chaine:
        if i.lower() in voyelles:
            compteur += 1
    print(f"Votre chaine '{chaine}' contient {compteur} voyelles")

def main():
    chaine = input("Entrez une chaine de caractères : ")
    nb_voyelles(chaine)

if __name__ == '__main__':
    main()