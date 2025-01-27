from score import *
from sauvegarde import *
from allumette_machine import *
from allumette_machine_machine import *

bleu = "\033[34m"
rose = "\033[35m"
cyan = "\033[36m"
gris = "\033[90m"
vert_clair = "\033[92m"
violet = "\033[38;5;129m"
reset = "\033[0m"

def regle_allumette() -> None:
    '''
    Affiche les règles du jeu des allumettes
    '''
    clear()
    print("\n-----------------------",f"{rouge}Règles du jeu{reset}","-----------------------\n")
    print("  Bienvenue dans le jeu des allumettes !!!")
    print("  Il y a 20 allumettes.")
    print("  Chaque joueur à tour de rôle enlève 1, 2 ou 3 allumettes.")
    print("  Le joueur qui prend la dernière allumette a perdu.\n")
    print(f"{violet}  Que le meilleur gagne 😈{reset}\n")
    input("  Appuyez sur 'Entrée' pour continuer")

def jeu_j1(joueur1 : str, joueur2 : str) -> int:
    '''
    Fonction qui permet de jouer aux allumettes en commencant par le joueur 1
    
    Args:
        joueur1 (str) : le pseudo du joueur 1
        joueur2 (str) : le pseudo du joueur 2
        
    Returns:
        points (int) : le nombre de points gagnés
    '''
    baton : str
    nb_batons : int
    k : int
    k = 0
    baton = '┃'
    nb_batons = 20
    points : int
    points = 10
    fin : bool
    fin = False

    print("\n  ",nb_batons * baton)
    print(f"\n    Il y a {rouge}{nb_batons}{reset} batons\n")
    while not fin:
        print("\n  ________________________________________________________________________\n")
        k = int(input(f"\n  {joueur1}, combien de batons enlevez-vous ? (1-3) : "))
        while k < 1 or k > 3:
            k = int(input(f"\n  Erreur. {joueur1}, choisissez un nombre entre 1 et 3 : "))
        nb_batons -= k
        if nb_batons <= 0:
            clear()
            print(f"\n  {joueur2} a perdu! 🤡")
            print(f"\n{vert}  {joueur1} a gagné! 🥳{reset}\n")
            fin = True
        else:
            print("\n  ", nb_batons * baton)
            print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
        if not fin:
            print("\n  ________________________________________________________________________\n")
            k = int(input(f"\n  {joueur2}, combien de batons enlevez-vous ? (1-3) : "))
            while k < 1 or k > 3:
                k = int(input(f"\n  Erreur. {joueur2}, choisissez un nombre entre 1 et 3 : "))
            nb_batons -= k
            if nb_batons <= 0:
                clear()
                print(f"\n  {joueur2} a perdu! 🤡")
                print(f"\n{vert}  {joueur1} a gagné! 🥳{reset}\n")
                fin = True
            else:
                print("\n  ", nb_batons * baton)
                print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
    input("  Appuyez sur 'Entrée' pour continuer")
    return points
            
def jeu_j2(joueur1 : str, joueur2 : str) -> int:
    '''
    Fonction qui permet de jouer aux allumettes en commencant par le joueur 2

    Args:
        joueur1 (str) : le pseudo du joueur 1
        joueur2 (str) : le pseudo du joueur 2

    Returns:
        points (int) : le nombre de points gagnés
    '''
    baton : str
    nb_batons : int
    k : int
    k = 0
    points : int
    points = 10
    baton = '┃'
    nb_batons = 20
    fin : bool
    fin = False

    print("\n  ",nb_batons * baton)
    print(f"\n    Il y a {rouge}{nb_batons}{reset} batons\n")

    while not fin:
        print("\n  ________________________________________________________________________\n")
        k = int(input(f"\n  {joueur2}, combien de batons enlevez-vous ? (1-3) : "))
        while k < 1 or k > 3:
            k = int(input(f"\n  Erreur. {joueur2}, choisissez un nombre entre 1 et 3 : "))
        nb_batons -= k
        if nb_batons <= 0:
            clear()
            print(f"\n  {joueur2} a perdu! 🤡")
            print(f"\n{vert}  {joueur1} a gagné! 🥳{reset}\n")
            fin = True
        else:
            print("\n  ", nb_batons * baton)
            print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
        if not fin:
            print("\n  ________________________________________________________________________\n")
            k = int(input(f"\n  {joueur1}, combien de batons enlevez-vous ? (1-3) : "))
            while k < 1 or k > 3:
                k = int(input(f"\n  Erreur. {joueur1}, choisissez un nombre entre 1 et 3 : "))
            nb_batons -= k
            if nb_batons <= 0:
                clear()
                print(f"\n  {joueur1} a perdu! 🤡")
                print(f"\n{vert}  {joueur2} a gagné! 🥳{reset}\n")
                fin = True
            else:
                print("\n  ", nb_batons * baton)
                print(f"\n    Il reste {rouge}{nb_batons}{reset} batons\n")
    input("  Appuyez sur 'Entrée' pour continuer")
    return points

def jeu() -> None:
    '''
    Fonction qui permet de jouer aux allumettes en choisissant qui commence
    '''
    from pseudo import choisir_pseudo
    x : int
    x = 0
    joueur1 : str
    joueur2 : str
    points : int

    clear()
    joueur1 = choisir_pseudo()
    clear()
    joueur2 = choisir_pseudo()

    while x != 3:
        clear()
        print(f"\n\t  1-{joueur1} vs 2-{joueur2}\n")
        print()
        x = int(input("  Qui commence ? (1 ou 2) : "))
        print()
        match x:
            case 1 :
                points = jeu_j1(joueur1,joueur2)
                ajout_score_allumettes(joueur1, points)
                return
            case 2 :
                points = jeu_j2(joueur1,joueur2)
                ajout_score_allumettes(joueur2, points)
                return
            case 3 :
                print("  Fin")
            case _ :
                print("  Erreur de choix")

def allumette_mode() -> None:
    '''
    Fonction qui permet de choisir le mode de jeu
    '''
    choix : int
    choix = 0

    while choix != 4:
        clear()
        print("\n------------------",f"{rouge}Allumettes{reset}","------------------\n")
        print("\t", f"{jaune}1 - Joueur contre Joueur{reset}")
        print("\t", f"{cyan}2 - Joueur contre Ordi{reset}")
        print("\t", f"{magenta}3 - Ordi contre Ordi{reset}")
        print("\t", f"{vert}4 - Quitter{reset}\n")
        print("------------------------------------------------\n")

        choix = int(input("  Choisissez une option : "))
        print()
        
        match choix:
            case 1 :
                jeu()
            case 2 :
                jeu_joueur_ordi()
            case 3 :
                jeu_ordi_ordi()
            case 4 :
                print("  Fin de la partie")
            case _ :
                print("  Erreur de choix")

def allumette() -> None:
    '''
    Fonction qui permet de choisir les options du jeu des allumettes
    '''
    choix : int
    choix = 0

    while choix != 3:
        clear()
        print("\n------------------",f"{rose}Allumettes{reset}","------------------\n")
        print("\t", f"{gris}1 - Règles du jeu{reset}")
        print("\t", f"{bleu}2 - Jouer{reset}")
        print("\t", f"{vert_clair}3 - Quitter{reset}\n")
        print("------------------------------------------------\n")

        choix = int(input("  Choisissez une option : "))
        print()

        match choix:
            case 1 :
                regle_allumette()
            case 2 :
                allumette_mode()        
            case 3 :
                print("  Fin de la partie")
            case _ :
                print("  Erreur de choix")
