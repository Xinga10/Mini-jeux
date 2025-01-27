from score import *
from sauvegarde import *
from time import sleep
from puissance4_machine import *
from puissance4_machine_machine import *

bleu = "\033[34m"
rose = "\033[35m"
reset = "\033[0m"
jaune_clair = "\033[93m"
vert = "\033[32m"
cyan = "\033[36m"
violet = "\033[38;5;129m"

def regle_puissance4():
    '''
    Affiche les règles du jeu du Puissance 4
    '''
    clear()
    print("\n--------------------------------",f"{rouge}Règles du jeu{reset}","--------------------------------\n")
    print("  Bienvenue dans le jeu du Puissance 4 !!!")
    print("  A tour de rôle les joueurs placent un pion dans une colonne de leur choix.")
    print("  Le premier joueur à aligner 4 🔴 ou 🟡 gagne la partie.\n")
    print(f"{violet}  Que le meilleur gagne 😈{reset}\n")
    input("  Appuyez sur 'Entrée' pour continuer")

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

def verifier_match_nul(grille : list[list[str]]) -> bool:
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

def jeu_principal(joueur1 : str, joueur2 : str, joueur_premier : str) -> tuple[int, str]:
    '''
    Fonction qui permet de jouer au Puissance 4

    Args:
        joueur1 (str) : le pseudo du joueur 1
        joueur2 (str) : le pseudo du joueur 2
        joueur_premier (str) : le joueur qui commence

    Returns:
        tuple[int, str] : le nombre de points gagnés et le pseudo du joueur gagnant
    '''
    grille : list[list[str]]
    joueur_actuel : str
    symbole : str
    fin : bool
    points : int
    j : int
    i : int
    points = 50
    grille = [["  " for _ in range(7)] for _ in range(6)]
    symbole_joueur1 = "🔴"
    symbole_joueur2 = "🟡"
    joueur_actuel = joueur_premier
    fin = False

    while not fin:
        clear()
        afficher_grille(grille)
        if joueur_actuel == joueur1:
            symbole = symbole_joueur1
        else:
            symbole = symbole_joueur2

        print(f"  {joueur_actuel} {symbole}, c'est à vous de jouer.\n")
        j = int(input("  Colonne (1-7) : ")) - 1

        while j < 0 or j > 6 or grille[0][j] != '  ':
            print("  Erreur. Colonne déjà pleine ou hors de la grille.\n")
            j = int(input("  Colonne (1-7) : ")) - 1

        for i in range(6):
            if grille[i][j] == '  ':
                if i > 0:
                    grille[i-1][j] = '  '
                grille[i][j] = symbole
                clear()
                afficher_grille(grille)
                sleep(0.1)

        if verifier_victoire(grille, symbole):
            clear()
            afficher_grille(grille)
            print(f"{vert}  {joueur_actuel} a gagné ! 🥳{reset}\n")
            fin = True
        elif verifier_match_nul(grille):
            clear()
            afficher_grille(grille)
            print("  Match nul !\n")
            fin = True
            points = 0
        else:
            joueur_actuel = joueur2 if joueur_actuel == joueur1 else joueur1
    input("  Appuyez sur 'Entrée' pour continuer")
    return points, joueur_actuel

def jeu() -> None:
    '''
    Fonction qui permet de choisir qui commence la partie
    '''
    from pseudo import choisir_pseudo
    x : int
    x = 0
    points : int
    joueur_actuel : str
    joueur1 : str
    joueur2 : str
    clear()
    joueur1 = choisir_pseudo()
    clear()
    joueur2 = choisir_pseudo()

    while x != 3:
        clear()
        print(f"\n\t 1-{joueur1} vs 2-{joueur2}\n")
        print()
        x = int(input("  Qui commence ? (1 ou 2) : "))
        print()
        match x:
            case 1 :
                points,joueur_actuel = jeu_principal(joueur1,joueur2,joueur1)
                ajout_score_puissance4(joueur_actuel, points)
                return
            case 2 :
                points, joueur_actuel = jeu_principal(joueur1,joueur2,joueur2)
                ajout_score_puissance4(joueur_actuel, points)
                return
            case 3 :
                print("  Fin")
            case _ :
                print("  Erreur de choix")

def jeu_mode() -> None:
    '''
    Fonction qui permet de choisir le mode de jeu
    '''
    choix : int
    choix = 0

    while choix != 4:
        clear()
        print("\n------------------",f"{rouge}Morpion{reset}","------------------\n")
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

def puissance4() -> None:
    '''
    Fonction qui permet de choisir les options du jeu Puissance 4
    '''
    choix : int
    choix = 0

    while choix != 3:
        clear()
        print("\n------------------",f"{vert}Puissance 4{reset}","------------------\n")
        print("\t", f"{bleu}1 - Règles du jeu{reset}")
        print("\t", f"{jaune_clair}2 - Jouer{reset}")
        print("\t", f"{rose}3 - Quitter{reset}","\n")
        print("-------------------------------------------------\n")
        
        choix = int(input("  Choisissez une option : "))
        print()

        match choix:
            case 1 :
                regle_puissance4()
            case 2 :
                jeu_mode()
            case 3 :
                print("  Fin de la partie")
            case _ :
                print("  Erreur de choix")