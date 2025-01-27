from random import randint
from sauvegarde import *
from pseudo import *
import random

cyan = "\033[36m"
magenta = "\033[35m"
reset = "\033[0m"

def allumette_facile() -> None:
    '''
    Fonction qui permet de jouer aux allumettes en mode facile avec un ordinateur aléatoire
    '''
    baton : str
    nb_batons : int
    k : int
    k = 0
    baton = '┃'
    nb_batons = 20
    fin : bool
    fin = False
    x : int
    x = 0
    joueur : str
    bot : str

    clear()
    joueur = choisir_pseudo()
    clear()
    bot = choisir_pseudo_bot()

    while x != 3:
        clear()
        print(f"\n\t 1-{joueur} VS 2-{bot}\n")
        print()
        x = int(input("  Qui commence ? : "))
        print()
        match x:
            case 1:
                print("\n  ",nb_batons * baton)
                print(f"\n    Il y a {rouge}{nb_batons}{reset} batons\n")
                while not fin:
                    print("\n  ________________________________________________________________________\n")
                    k = int(input(f"\n  {joueur}, combien de batons enlevez-vous ? (1-3) : "))
                    while k < 1 or k > 3:
                        k = int(input(f"\n  Erreur. {joueur}, choisissez un nombre entre 1 et 3 : "))
                    nb_batons -= k
                    if nb_batons <= 0:
                        clear()
                        print(f"\n  {joueur} a perdu! 🤡")
                        print(f"\n{vert}  {bot} a gagné! 🥳{reset}\n")
                        fin = True
                    else:
                        print("\n  ", nb_batons * baton)
                        print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                    if not fin:
                        print("\n  ________________________________________________________________________\n")
                        k = randint(1,3)
                        nb_batons -= k
                        if nb_batons <= 0:
                            clear()
                            print("\n  {bot} a perdu! 🤡")
                            print(f"\n{vert}  {joueur} a gagné! 🥳{reset}\n")
                            fin = True
                        else:
                            print("\n  ", nb_batons * baton)
                            print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                input("  Appuyez sur 'Entrée' pour continuer")
                x = 3
            case 2:
                print("\n  ",nb_batons * baton)
                print(f"\n    Il y a {rouge}{nb_batons}{reset} batons\n")
                while not fin:
                    print("\n  ________________________________________________________________________\n")
                    k = randint(1,3)
                    nb_batons -= k
                    if nb_batons <= 0:
                        clear()
                        print("\n  {bot} a perdu! 🤡")
                        print(f"\n{vert}  {joueur} a gagné! 🥳{reset}\n")
                        fin = True
                    else:
                        print("\n  ", nb_batons * baton)
                        print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                    if not fin:
                        print("\n  ________________________________________________________________________\n")
                        k = int(input(f"\n  {joueur}, combien de batons enlevez-vous ? (1-3) : "))
                        while k < 1 or k > 3:
                            k = int(input(f"\n  Erreur. {joueur}, choisissez un nombre entre 1 et 3 : "))
                        nb_batons -= k
                        if nb_batons <= 0:
                            clear()
                            print(f"\n  {joueur} a perdu! 🤡")
                            print(f"\n{vert}  {bot} a gagné! 🥳{reset}\n")
                            fin = True
                        else:
                            print("\n  ", nb_batons * baton)
                            print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                input("  Appuyez sur 'Entrée' pour continuer")
                x = 3
            case _:
                print("  Erreur de choix")

def allumette_intermediaire() -> None:
    '''
    Fonction qui permet de jouer aux allumettes en mode intermédiaire avec un ordinateur mi-aleatoire et mi-stratégique
    '''
    baton : str
    nb_batons : int
    k : int
    k = 0
    baton = '┃'
    nb_batons = 20
    fin : bool
    fin = False
    x : int
    x = 0
    joueur : str
    bot : str

    clear()
    joueur = choisir_pseudo()
    clear()
    bot = choisir_pseudo_bot()

    while x != 3:
        clear()
        print(f"\n\t 1-{joueur} VS 2-{bot}\n")
        print()
        x = int(input("  Qui commence ? : "))
        print()
        match x:
            case 1:
                print("\n  ",nb_batons * baton)
                print(f"\n    Il y a {rouge}{nb_batons}{reset} batons\n")
                while not fin:
                    print("\n  ________________________________________________________________________\n")
                    k = int(input("Combien de batons voulez-vous retirer (1-3) ? "))
                    nb_batons -= k
                    if nb_batons <= 0:
                        clear()
                        print(f"\n  {joueur} a perdu! 🤡")
                        print(f"\n{vert}  {bot} a gagné! 🥳{reset}\n")
                        fin = True
                    else:
                        print("\n  ", nb_batons * baton)
                        print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                    if not fin:
                        print("\n  ________________________________________________________________________\n")
                        if random.random() < 0.5:
                            k = random.randint(1, 3)
                        else:
                            k = (nb_batons - 1) % 4
                            if k == 0:
                                k = random.randint(1, 3)
                        nb_batons -= k
                        if nb_batons <= 0:
                            clear()
                            print("\n  {bot} a perdu! 🤡")
                            print(f"\n{vert}  {joueur} a gagné! 🥳{reset}\n")
                            fin = True
                        else:
                            print("\n  ", nb_batons * baton)
                            print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                input("  Appuyez sur 'Entrée' pour continuer")
                x = 3
            case 2:
                print("\n  ",nb_batons * baton)
                print(f"\n    Il y a {rouge}{nb_batons}{reset} batons\n")
                while not fin:
                    print("\n  ________________________________________________________________________\n")
                    if random.random() < 0.5:
                        k = random.randint(1, 3)
                    else:
                        k = (nb_batons - 1) % 4
                        if k == 0:
                            k = random.randint(1, 3)
                    nb_batons -= k
                    if nb_batons <= 0:
                        clear()
                        print("\n  {bot} a perdu! 🤡")
                        print(f"\n{vert}  {joueur} a gagné! 🥳{reset}\n")
                        fin = True
                    else:
                        print("\n  ", nb_batons * baton)
                        print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                    if not fin:
                        print("\n  ________________________________________________________________________\n")
                        k = int(input("Combien de batons voulez-vous retirer (1-3) ? "))
                        nb_batons -= k
                        if nb_batons <= 0:
                            clear()
                            print(f"\n  {joueur} a perdu! 🤡")
                            print(f"\n{vert}  {bot} a gagné! 🥳{reset}\n")
                            fin = True
                        else:
                            print("\n  ", nb_batons * baton)
                            print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                input("  Appuyez sur 'Entrée' pour continuer")
                x = 3
            case _:
                print("  Erreur de choix")
                        
def allumette_difficile() -> None:
    '''
    Fonction qui permet de jouer aux allumettes en mode difficile avec un ordinateur stratégique
    '''
    baton : str
    nb_batons : int
    k : int
    k = 0
    baton = '┃'
    nb_batons = 20
    fin : bool
    fin = False
    x : int
    x = 0
    joueur : str
    bot : str

    clear()
    joueur = choisir_pseudo()
    clear()
    bot = choisir_pseudo_bot()

    while x != 3:
        clear()
        print(f"\n\t 1-{joueur} VS 2-{bot}\n")
        print()
        x = int(input("  Qui commence ? : "))
        print()
        match x:
            case 1:
                print("\n  ",nb_batons * baton)
                print(f"\n    Il y a {rouge}{nb_batons}{reset} batons\n")
                while not fin:
                    print("\n  ________________________________________________________________________\n")
                    k = int(input("Combien de batons voulez-vous retirer (1-3) ? "))
                    nb_batons -= k
                    if nb_batons <= 0:
                        clear()
                        print(f"\n  {joueur} a perdu! 🤡")
                        print(f"\n{vert}  {bot} a gagné! 🥳{reset}\n")
                        fin = True
                    else:
                        print("\n  ", nb_batons * baton)
                        print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                    if not fin:
                        print("\n  ________________________________________________________________________\n")
                        k = (nb_batons - 1) % 4
                        if k == 0:
                            k = random.randint(1, 3)
                        nb_batons -= k
                        if nb_batons <= 0:
                            clear()
                            print("\n  {bot} a perdu! 🤡")
                            print(f"\n{vert}  {joueur} a gagné! 🥳{reset}\n")
                            fin = True
                        else:
                            print("\n  ", nb_batons * baton)
                            print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                input("  Appuyez sur 'Entrée' pour continuer")
                x = 3
            case 2:
                print("\n  ",nb_batons * baton)
                print(f"\n    Il y a {rouge}{nb_batons}{reset} batons\n")
                while not fin:
                    print("\n  ________________________________________________________________________\n")
                    k = (nb_batons - 1) % 4
                    if k == 0:
                        k = random.randint(1, 3)
                    nb_batons -= k
                    if nb_batons <= 0:
                        clear()
                        print("\n  L'ordinateur a perdu! 🤡")
                        print(f"\n{vert}  {joueur} a gagné! 🥳{reset}\n")
                        fin = True
                    else:
                        print("\n  ", nb_batons * baton)
                        print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                    if not fin:
                        print("\n  ________________________________________________________________________\n")
                        k = int(input("Combien de batons voulez-vous retirer (1-3) ? "))
                        nb_batons -= k
                        if nb_batons <= 0:
                            clear()
                            print(f"\n  {joueur} a perdu! 🤡")
                            print(f"\n{vert}  {bot} a gagné! 🥳{reset}\n")
                            fin = True
                        else:
                            print("\n  ", nb_batons * baton)
                            print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
                input("  Appuyez sur 'Entrée' pour continuer")
                x = 3
            case _:
                print("  Erreur de choix")

def jeu_joueur_ordi() -> None:
    '''
    Fonction qui permet de choisir la difficulté
    '''
    choix : int
    choix = 0

    while choix != 4:

        clear()
        print("\n------------------",f"{rouge}Difficultés de jeu{reset}","------------------\n")
        print("\t", f"{cyan}1 - Facile{reset}")
        print("\t", f"{vert}2 - Intermediaire{reset}")
        print("\t", f"{gris}3 - Difficile{reset}")
        print("\t", f"{magenta}4 - Retour{reset}\n")
        print("------------------------------------------------\n")

        choix = int(input("  Choisissez une option : "))
        print()
        
        match choix:
            case 1 :
                allumette_facile()
            case 2 :
                allumette_intermediaire()
            case 3 :
                allumette_difficile()
            case 4:
                print("  Retour")
            case _ :
                print("  Erreur de choix")