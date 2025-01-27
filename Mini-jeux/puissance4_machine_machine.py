from score import *
from sauvegarde import *
from time import sleep
from pseudo import *
from random import randint
import random

bleu = "\033[34m"
rose = "\033[35m"
reset = "\033[0m"
jaune_clair = "\033[93m"
vert = "\033[32m"
cyan = "\033[36m"
violet = "\033[38;5;129m"

def afficher_grille(grille : list[list[str]]) -> None:
    '''
    Affiche la grille de jeu du Puissance 4

    Args:
        grille (list[list[str]]) : la grille de jeu
    '''
    i : int
    j : int 
    print(10*'\n')
    for i in range(6):
        print(f"{bleu}|{reset}", end='')
        for j in range(7):
            print(f' {grille[i][j]} ', end=f"{bleu}|{reset}")
        print()
    print('➖' * 18)
    print("   1    2    3    4    5    6    7 \n")

def verifier_victoire(grille : list[list[str]], joueur : str) -> bool:
    '''
    Vérifie si un joueur a gagné

    Args:
        grille (list[list[str]]) : la grille de jeu
        joueur (str) : le symbole du joueur

    Returns:
        bool : True si le joueur a gagné, False sinon
    '''
    for row in grille:
        for col in range(4):
            if row[col] == joueur and row[col + 1] == joueur and row[col + 2] == joueur and row[col + 3] == joueur:
                return True
    for col in range(7):
        for row in range(3):
            if grille[row][col] == joueur and grille[row + 1][col] == joueur and grille[row + 2][col] == joueur and grille[row + 3][col] == joueur:
                return True
    for row in range(3):
        for col in range(4):
            if grille[row][col] == joueur and grille[row + 1][col + 1] == joueur and grille[row + 2][col + 2] == joueur and grille[row + 3][col + 3] == joueur:
                return True
    for row in range(3, 6):
        for col in range(4):
            if grille[row][col] == joueur and grille[row - 1][col + 1] == joueur and grille[row - 2][col + 2] == joueur and grille[row - 3][col + 3] == joueur:
                return True
    return False

def verifier_match_nul(grille: list[list[str]]) -> bool:
    '''
    Vérifie si la partie est nulle

    Args:
        grille (list[list[str]]) : la grille de jeu

    Returns:
        bool : True si la partie est nulle, False sinon
    '''
    for row in grille:
        if '  ' in row:
            return False
    return True

def verifier_colonne_pleine(grille: list[list[str]], colonne: int) -> bool:
    """
    Vérifie si une colonne est pleine.

    Args:
        grille (list[list[str]]): La grille de jeu.
        colonne (int): L'indice de la colonne à vérifier.

    Returns:
        bool: True si la colonne est pleine, sinon False.
    """
    if grille[0][colonne] == '  ':
        return False
    return True

def trouver_ligne_vide(grille: list[list[str]], colonne: int) -> int:
    """
    Trouve la première ligne vide dans une colonne.

    Args:
        grille (list[list[str]]): La grille de jeu.
        colonne (int): L'indice de la colonne.

    Returns:
        int: L'indice de la première ligne vide.
    """
    for i in range(5, -1, -1):
        if grille[i][colonne] == '  ':
            return i
    return -1

def coup_machine(grille: list[list[str]]) -> int:
    """
    Fonction qui permet à l'ordinateur de jouer un coup.

    Args:
        grille (list[list[str]]): La grille de jeu.

    Returns:
        int: L'indice de la colonne choisie.
    """
    col : int
    ligne : int
    colonnes_valides : list[int]
    for col in range(7):
        if not verifier_colonne_pleine(grille, col):
            ligne = trouver_ligne_vide(grille, col)
            grille[ligne][col] = '🔴'
            if verifier_victoire(grille, '🔴'):
                grille[ligne][col] = '  '
                return col
            grille[ligne][col] = '  '
    for col in range(7):
        if not verifier_colonne_pleine(grille, col):
            ligne = trouver_ligne_vide(grille, col)
            grille[ligne][col] = '🟡'
            if verifier_victoire(grille, '🟡'):
                grille[ligne][col] = '  '
                return col
            grille[ligne][col] = '  '
    colonnes_valides = [col for col in range(7) if not verifier_colonne_pleine(grille, col)]
    return random.choice(colonnes_valides)

def puissance4_facile() -> None:
    '''
    Fonction qui permet de jouer au Puissance 4 en mode facile
    '''
    grille : list[list[str]]
    bot1 : str
    bot2 : str
    symbole_bot1 : str
    symbole_bot2 : str
    fin : bool
    j : int
    i : int
    grille = [["  " for _ in range(7)] for _ in range(6)]
    symbole_bot1 = "🔴"
    symbole_bot2 = "🟡"
    fin = False

    clear()
    bot1 = choisir_pseudo_bot()
    clear()
    bot2 = choisir_pseudo_bot()

    clear()
    print(f"\n\t1-{bot1} 🔴 VS 2-{bot2} 🟡\n")
    print()
    x = int(input("  Qui commence ? : "))
    print()
    match x:
        case 1:
            while not fin:
                clear()
                afficher_grille(grille)
                j = randint(0, 6)
                while j < 0 or j > 6 or grille[0][j] != '  ':
                    j = randint(0, 6)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '
                        grille[i][j] = symbole_bot1
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot1):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot1} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                clear()
                afficher_grille(grille)
                j = randint(0, 6)
                while j < 0 or j > 6 or grille[0][j] != '  ':
                    j = randint(0, 6)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '
                        grille[i][j] = symbole_bot2
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot2):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot2} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
        case 2:
            while not fin:
                clear()
                afficher_grille(grille)
                j = randint(0, 6)
                while j < 0 or j > 6 or grille[0][j] != '  ':
                    j = randint(0, 6)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '
                        grille[i][j] = symbole_bot2
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot2):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot2} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                clear()
                afficher_grille(grille)
                j = randint(0, 6)
                while j < 0 or j > 6 or grille[0][j] != '  ':
                    j = randint(0, 6)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '
                        grille[i][j] = symbole_bot1
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot1):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot1} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
        case _:
            print("  Erreur de choix")
            
def puissance4_intermediaire() -> None:
    '''
    Fonction qui permet de jouer au Puissance 4 en mode intermediaire
    '''
    grille : list[list[str]]
    bot1 : str
    bot2 : str
    symbole_bot1 : str
    symbole_bot2 : str
    fin : bool
    j : int
    i : int
    grille = [["  " for _ in range(7)] for _ in range(6)]
    symbole_bot1 = "🔴"
    symbole_bot2 = "🟡"
    fin = False

    clear()
    bot1 = choisir_pseudo_bot()
    clear()
    bot2 = choisir_pseudo_bot()

    clear()
    print(f"\n\t1-{bot1} 🔴 VS 2-{bot2} 🟡\n")
    print()
    x = int(input("  Qui commence ? : "))
    print()
    match x:
        case 1:
            while not fin:
                clear()
                afficher_grille(grille)
                if random.random() < 0.5:
                    j = coup_machine(grille)
                else:
                    j = randint(0, 6)
                    while j < 0 or j > 6 or grille[0][j] != '  ':
                        j = randint(0, 6)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '
                        grille[i][j] = symbole_bot1
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot1):  
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot1} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                clear()
                afficher_grille(grille)
                if random.random() < 0.5:
                    j = coup_machine(grille)
                else:
                    j = randint(0, 6)
                    while j < 0 or j > 6 or grille[0][j] != '  ':
                        j = randint(0, 6)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '  
                        grille[i][j] = symbole_bot2
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot2):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot2} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
        case 2:
            while not fin:
                clear()
                afficher_grille(grille)
                if random.random() < 0.5:
                    j = coup_machine(grille)
                else:
                    j = randint(0, 6)
                    while j < 0 or j > 6 or grille[0][j] != '  ':
                        j = randint(0, 6)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '  
                        grille[i][j] = symbole_bot2
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)                
                if verifier_victoire(grille, symbole_bot2):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot2} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                clear()
                afficher_grille(grille)
                if random.random() < 0.5:
                    j = coup_machine(grille)
                else:
                    j = randint(0, 6)
                    while j < 0 or j > 6 or grille[0][j] != '  ':
                        j = randint(0, 6)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '
                        grille[i][j] = symbole_bot1
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot1):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot1} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
        case _:
            print("  Erreur de choix")

def puissance4_difficile() -> None:
    '''
    Fonction qui permet de jouer au Puissance 4 en mode difficile
    '''
    grille : list[list[str]]
    fin : bool
    bot1 : str
    bot2 : str
    symbole_bot1 : str
    symbole_bot2 : str
    j : int
    i : int
    grille = [["  " for _ in range(7)] for _ in range(6)]
    symbole_bot1 = "🔴"
    symbole_bot2 = "🟡"
    fin = False

    clear()
    bot1 = choisir_pseudo_bot()
    clear()
    bot2 = choisir_pseudo_bot()

    clear()
    print(f"\n\t1-{bot1} 🔴 VS 2-{bot2} 🟡\n")
    print()
    x = int(input("  Qui commence ? : "))
    print()
    match x:
        case 1:
            while not fin:
                clear()
                afficher_grille(grille)
                j = coup_machine(grille)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '
                        grille[i][j] = symbole_bot1
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot1):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot1} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                clear()
                afficher_grille(grille)
                j = coup_machine(grille)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '  
                        grille[i][j] = symbole_bot2
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot2):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot2} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
        case 2:
            while not fin:
                clear()
                afficher_grille(grille)
                j = coup_machine(grille)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '  
                        grille[i][j] = symbole_bot2 
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot2):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot2} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                clear()
                afficher_grille(grille)
                j = coup_machine(grille)
                for i in range(6):
                    if grille[i][j] == '  ':
                        if i > 0:
                            grille[i-1][j] = '  '
                        grille[i][j] = symbole_bot1
                        clear()
                        afficher_grille(grille)
                        sleep(0.1)
                if verifier_victoire(grille, symbole_bot1):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert}  {bot1} a gagné ! 🥳{reset}\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
                elif verifier_match_nul(grille):
                    clear()
                    afficher_grille(grille)
                    print("  Match nul !\n")
                    fin = True
                    input("  Appuyez sur 'Entrée' pour continuer")
                    return None
        case _:
            print("  Erreur de choix")

def jeu_ordi_ordi() -> None:
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
                puissance4_facile()
            case 2 :
                puissance4_intermediaire()
            case 3 :
                puissance4_difficile()
            case 4:
                print("  Retour")
            case _ :
                print("  Erreur de choix")