from score import *
from sauvegarde import *
from morpion_machine import *
from morpion_machine_machine import *

vert = "\033[32m"
cyan = "\033[36m"
violet = "\033[38;5;129m"
reset = "\033[0m"
orange = "\033[91m"
rouge = "\033[38;5;196m"
rose = "\033[35m"
vert_clair = "\033[92m"


def regle_morpion() -> None:
    '''
    Affiche les règles du jeu du morpion
    '''
    clear()
    print("\n---------------------------",f"{rouge}Règles du jeu{reset}","--------------------------\n")
    print("  Bienvenue dans le jeu du morpion !!!")
    print("  A tour de rôle les joueurs placent une ✖️ ou un 🔴 sur une case.")
    print("  premier joueur à aligner 3 symboles a gagné.\n")
    print(f"{violet}  Que le meilleur gagne 😈{reset}\n")
    input("  Appuyez sur 'Entrée' pour continuer")

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
    for row in grille:
        if '  ' in row:
            return False
    return True

def jeu_principal(joueur1: str, joueur2: str, premier_joueur: str) -> tuple[int, str]:
    '''
    Fonction qui permet de jouer au morpion

    Args:
        joueur1 (str) : le pseudo du joueur 1
        joueur2 (str) : le pseudo du joueur 2
        premier_joueur (str) : le pseudo du joueur qui commence

    Returns:
        points (int) : le nombre de points gagnés
        joueur_actuel (str) : le pseudo du joueur qui a gagné
    '''
    grille : list[list[str]]
    joueur_actuel : str
    symbole : str
    fin : bool
    points : int
    i : int
    j : int
    points = 10
    grille = [['  ' for _ in range(3)] for _ in range(3)]
    joueur_actuel = premier_joueur
    fin = False

    while not fin:
        clear()
        afficher_grille(grille)
        if joueur_actuel == joueur1:
            print(f"  {joueur1} ✖️  , c'est à vous de jouer.\n")
            symbole = '✖️'
        else:
            print(f"  {joueur2} 🔴, c'est à vous de jouer.\n")
            symbole = '🔴'

        i = int(input("  Ligne (1-3) : ")) - 1
        j = int(input("  Colonne (1-3) : ")) - 1
        print()

        while i < 0 or i > 2 or j < 0 or j > 2 or grille[i][j] != '  ':
            print("  Erreur. Case déjà occupée ou hors de la grille.\n")
            i = int(input("  Ligne (1-3) : ")) - 1
            j = int(input("  Colonne (1-3) : ")) - 1

        grille[i][j] = symbole

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
    Fonction qui permet de jouer au morpion en choisissant qui commence
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
        print(f"\n\t  1-{joueur1} ✖️  vs  2-{joueur2} 🔴\n")
        print()
        x = int(input("  Qui commence ? (1 ou 2) : "))
        print()
        match x:
            case 1 :
                points,joueur_actuel = jeu_principal(joueur1,joueur2,joueur1)
                ajout_score_morpion(joueur_actuel, points)
                return
            case 2 :
                points,joueur_actuel = jeu_principal(joueur1,joueur2,joueur2)
                ajout_score_morpion(joueur_actuel, points)
                return
            case 3 :
                print("  Fin")
            case _ :
                print("  Erreur de choix")

def morpion_mode() -> None:
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

def morpion() -> None:
    '''
    Fonction qui permet de choisir les options du jeu du morpion
    '''
    choix : int
    choix = 0

    while choix != 3:
        clear()
        print("\n------------------",f"{rose}Morpion{reset}","------------------\n")
        print("\t", f"{gris}1 - Règles du jeu{reset}")
        print("\t", f"{bleu}2 - Jouer{reset}")
        print("\t", f"{vert_clair}3 - Quitter{reset}\n")
        print("------------------------------------------------\n")

        choix = int(input("  Choisissez une option : "))
        print()

        match choix:
            case 1 :
                regle_morpion()
            case 2 :
                morpion_mode()        
            case 3 :
                print("  Fin de la partie")
            case _ :
                print("  Erreur de choix")