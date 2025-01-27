from random import randint
from sauvegarde import *
from pseudo import *
import random
from time import sleep

cyan = "\033[36m"
magenta = "\033[95m"
rouge = "\033[91m"
reset = "\033[0m"

def afficher_grille(grille : list[list[str]]) -> None:
    '''
    Affiche la grille de jeu du morpion
    
    Args:
        grille (list[list[str]]) : la grille de jeu
    '''
    i : int
    j : int
    print(10*'\n')
    for i in range(3):
        for j in range(3):
            print(grille[i][j], end='  ')
            if j < 2:
                print('|', end='  ')
        print()
        if i < 2:
            print("----+------+-----")
    print()

def verifier_victoire(grille :list[list[str]], joueur : str) -> bool:
    '''
    Vérifie si un joueur a gagné

    Args:
        grille (list[list[str]]) : la grille de jeu
        joueur (str) : le symbole du joueur

    Returns:
        bool : True si le joueur a gagné, False sinon
    '''
    return ((grille[0][0] == joueur and grille[0][1] == joueur and grille[0][2] == joueur) or
            (grille[1][0] == joueur and grille[1][1] == joueur and grille[1][2] == joueur) or
            (grille[2][0] == joueur and grille[2][1] == joueur and grille[2][2] == joueur) or
            (grille[0][0] == joueur and grille[1][0] == joueur and grille[2][0] == joueur) or
            (grille[0][1] == joueur and grille[1][1] == joueur and grille[2][1] == joueur) or
            (grille[0][2] == joueur and grille[1][2] == joueur and grille[2][2] == joueur) or
            (grille[0][0] == joueur and grille[1][1] == joueur and grille[2][2] == joueur) or
            (grille[0][2] == joueur and grille[1][1] == joueur and grille[2][0] == joueur))

def verifier_match_nul(grille: list[list[str]]) -> bool:
    '''
    Vérifie si la partie est nulle

    Args:
        grille (list[list[str]]) : la grille de jeu

    Returns:
        bool : True si la partie est nulle, False sinon
    '''
    row : list[str]
    for row in grille:
        if '  ' in row:
            return False
    return True

def coups_disponibles(grille: list[list[str]]) -> list[tuple[int, int]]:
    '''
    Renvoie les coups disponibles

    Args:
        grille (list[list[str]]) : la grille de jeu

    Returns:
        list[tuple[int, int]] : la liste des coups disponibles
    '''
    return [(i, j) for i in range(3) for j in range(3) if grille[i][j] == '  ']

def minimax(grille: list[list[str]], profondeur: int, est_maximisant: bool, bot1: str, bot2: str) -> int:
    '''
    Fonction qui aide a calculer le meilleur coup

    Args:
        grille (list[list[str]]) : la grille de jeu
        profondeur (int) : la profondeur de l'arbre
        est_maximisant (bool) : True si c'est le tour du bot1, False sinon
        bot1 (str) : le symbole du bot1
        bot2 (str) : le symbole du bot2

    Returns:
        int : le score du meilleur coup
    '''
    i : int
    j : int
    meilleur_score : int
    score_actuel : int
    if verifier_victoire(grille, bot1):
        return 100 - profondeur
    elif verifier_victoire(grille, bot2):
        return -100 + profondeur
    elif verifier_match_nul(grille):
        return 0

    if est_maximisant:
        meilleur_score = -1000
        for i, j in coups_disponibles(grille):
            grille[i][j] = bot1
            score_actuel = minimax(grille, profondeur + 1, False, bot1, bot2)
            grille[i][j] = '  '
            meilleur_score = max(meilleur_score, score_actuel)
        return meilleur_score
    else:
        meilleur_score = 1000
        for i, j in coups_disponibles(grille):
            grille[i][j] = bot2
            score_actuel = minimax(grille, profondeur + 1, True, bot1, bot2)
            grille[i][j] = '  '
            meilleur_score = min(meilleur_score, score_actuel)
        return meilleur_score
    
def meilleur_coup(grille: list[list[str]], bot1: str, bot2: str) -> tuple[int, int]:
    '''
    Fonction qui permet de déterminer le meilleur coup à jouer

    Args:
        grille (list[list[str]]) : la grille de jeu
        bot1 (str) : le symbole du bot1
        bot2 (str) : le symbole du bot2

    Returns:
        tuple[int, int] : le meilleur coup à jouer
    '''
    meilleur_score : int
    score_actuel : int
    i : int
    j : int
    coup : tuple[int, int]
    meilleur_score = -1000

    coup = (-1, -1)
    for (i, j) in coups_disponibles(grille):
        grille[i][j] = bot1
        score_actuel = minimax(grille, 0, False, bot1, bot2)
        grille[i][j] = '  '
        if score_actuel > meilleur_score:
            meilleur_score = score_actuel
            coup = (i, j)
    return coup

def morpion_facile() -> None:
    '''
    Fonction qui permet de jouer au morpion en mode facile
    '''
    grille : list[list[str]]
    symbole : str
    fin : bool
    i : int
    j : int
    grille = [['  ' for _ in range(3)] for _ in range(3)]
    fin = False
    x : int
    x = 0
    bot1 : str
    bot2 : str

    clear()
    bot1 = choisir_pseudo_bot()
    clear()
    bot2 = choisir_pseudo_bot()

    clear()
    print(f"\n\t1-{bot1} 🔴 VS 2-{bot2} ✖️\n")
    print()
    x = int(input("  Qui commence ? : "))
    print()
    match x:
        case 1:
            while not fin:
                clear()
                afficher_grille(grille)
                print(f"  {bot1} 🔴, c'est à vous de jouer.\n")
                symbole = '🔴'
                i = randint(0,2)
                j = randint(0,2)
                while grille[i][j] != '  ':
                    i = randint(0,2)
                    j = randint(0,2)
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert} {bot1} a gagné ! 🥳{reset}\n")
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
                sleep(1)
                clear()
                afficher_grille(grille)

                print(f"  {bot2} ✖️  , c'est à vous de jouer.\n")
                symbole = '✖️'
                i = randint(0,2)
                j = randint(0,2)
                while grille[i][j] != '  ':
                    i = randint(0,2)
                    j = randint(0,2)
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
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
                sleep(1)
        case 2:
            while not fin:
                clear()
                afficher_grille(grille)
                print(f"  {bot2} ✖️ , c'est à vous de jouer.\n")
                symbole = '✖️'
                i = randint(0,2)
                j = randint(0,2)
                while grille[i][j] != '  ':
                    i = randint(0,2)
                    j = randint(0,2)
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert} {bot2} a gagné ! 🥳{reset}\n")
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
                sleep(1)
                clear()
                afficher_grille(grille)
                print(f"  {bot1} 🔴  , c'est à vous de jouer.\n")
                symbole = '🔴'
                i = randint(0,2)
                j = randint(0,2)
                while grille[i][j] != '  ':
                    i = randint(0,2)
                    j = randint(0,2)
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
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
                sleep(1)
        case _:
            print("  Erreur de choix")

def morpion_intermediaire() -> None:
    '''
    Fonction qui permet de jouer au morpion en mode intermédiaire
    '''
    grille : list[list[str]]
    symbole : str
    fin : bool
    i : int
    j : int
    grille = [['  ' for _ in range(3)] for _ in range(3)]
    fin = False
    x : int
    x = 0
    bot1 : str
    bot2 : str

    bot1 = choisir_pseudo_bot()
    bot2 = choisir_pseudo_bot()

    clear()
    print(f"\n\t1-{bot1} 🔴 VS 2-{bot2} ✖️\n")
    print()
    x = int(input("  Qui commence ? : "))
    print()
    match x:
        case 1:
            while not fin:
                clear()
                afficher_grille(grille)
                print(f"  {bot1} 🔴, c'est à vous de jouer.\n")
                symbole = '🔴'
                if random.random() > 0.5:
                    i = randint(0, 2)
                    j = randint(0, 2)
                    while grille[i][j] != '  ':
                        i = randint(0, 2)
                        j = randint(0, 2)
                else:
                    coup = meilleur_coup(grille, '🔴', '✖️')
                    if coup != (-1, -1):
                        i, j = coup
                    else:
                        i = randint(0, 2)
                        j = randint(0, 2)
                        while grille[i][j] != '  ':
                            i = randint(0, 2)
                            j = randint(0, 2)
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert} {bot1} a gagné ! 🥳{reset}\n")
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
                sleep(1)
                clear()
                afficher_grille(grille)

                print(f"  {bot2} ✖️  , c'est à vous de jouer.\n")
                symbole = '✖️'
                if random.random() > 0.5:
                    i = randint(0, 2)
                    j = randint(0, 2)
                    while grille[i][j] != '  ':
                        i = randint(0, 2)
                        j = randint(0, 2)
                else:
                    coup = meilleur_coup(grille, '✖️', '🔴')
                    if coup != (-1, -1):
                        i, j = coup
                    else:
                        i = randint(0, 2)
                        j = randint(0, 2)
                        while grille[i][j] != '  ':
                            i = randint(0, 2)
                            j = randint(0, 2)
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
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
                sleep(1)
        case 2:
            while not fin:
                clear()
                afficher_grille(grille)
                print(f"  {bot2} ✖️ , c'est à vous de jouer.\n")
                symbole = '✖️'
                if random.random() > 0.5:
                    i = randint(0, 2)
                    j = randint(0, 2)
                    while grille[i][j] != '  ':
                        i = randint(0, 2)
                        j = randint(0, 2)
                else:
                    coup = meilleur_coup(grille, '✖️', '🔴')
                    if coup != (-1, -1):
                        i, j = coup
                    else:
                        i = randint(0, 2)
                        j = randint(0, 2)
                        while grille[i][j] != '  ':
                            i = randint(0, 2)
                            j = randint(0, 2)
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert} {bot2} a gagné ! 🥳{reset}\n")
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
                sleep(1)
                clear()
                afficher_grille(grille)

                print("  {bot1} 🔴  , c'est à vous de jouer.\n")
                symbole = '🔴'
                if random.random() > 0.5:
                    i = randint(0, 2)
                    j = randint(0, 2)
                    while grille[i][j] != '  ':
                        i = randint(0, 2)
                        j = randint(0, 2)
                else:
                    coup = meilleur_coup(grille, '🔴', '✖️')
                    if coup != (-1, -1):
                        i, j = coup
                    else:
                        i = randint(0, 2)
                        j = randint(0, 2)
                        while grille[i][j] != '  ':
                            i = randint(0, 2)
                            j = randint(0, 2)
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
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
                sleep(1)
        case _:
            print("  Erreur de choix")

def morpion_difficile() -> None:
    '''
    Fonction qui permet de jouer au morpion en mode difficile
    '''
    grille : list[list[str]]
    symbole : str
    fin : bool
    i : int
    j : int
    grille = [['  ' for _ in range(3)] for _ in range(3)]
    fin = False
    x : int
    x = 0
    bot1 : str
    bot2 : str

    bot1 = choisir_pseudo_bot()
    bot2 = choisir_pseudo_bot()

    clear()
    print(f"\n\t1-{bot1} 🔴 VS 2-{bot2} ✖️\n")
    print()
    x = int(input("  Qui commence ? : "))
    print()
    match x:
        case 1:
            while not fin:
                clear()
                afficher_grille(grille)
                print(f"  {bot1} 🔴, c'est à vous de jouer.\n")
                symbole = '🔴'
                coup = meilleur_coup(grille, '🔴', '✖️')
                i, j = coup
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert} {bot1} a gagné ! 🥳{reset}\n")
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
                sleep(1)
                clear()
                afficher_grille(grille)

                print(f" {bot2} ✖️  , c'est à vous de jouer.\n")
                symbole = '✖️'
                coup = meilleur_coup(grille, '✖️', '🔴')
                i, j = coup
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
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
                sleep(1)
        case 2:
            while not fin:
                clear()
                afficher_grille(grille)
                print(f"  {bot2} ✖️ , c'est à vous de jouer.\n")
                symbole = '✖️'
                coup = meilleur_coup(grille, '✖️', '🔴')
                i, j = coup
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
                    clear()
                    afficher_grille(grille)
                    print(f"{vert} {bot2} a gagné ! 🥳{reset}\n")
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
                sleep(1)
                clear()
                afficher_grille(grille)

                print(f"  {bot1} 🔴  , c'est à vous de jouer.\n")
                symbole = '🔴'
                coup = meilleur_coup(grille, '🔴', '✖️')
                i, j = coup
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
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
                sleep(1)
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
                morpion_facile()
            case 2 :
                morpion_intermediaire()
            case 3 :
                morpion_difficile()
            case 4:
                print("  Retour")
            case _ :
                print("  Erreur de choix")