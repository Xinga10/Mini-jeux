from score import *
from sauvegarde import *
from devinette_machine import *
import getpass

rouge = "\033[31m"
magenta = "\033[35m"
jaune = "\033[38;5;226m"
bleu_clair = "\033[38;5;45m"
rouge_clair = "\033[38;5;196m"
violet = "\033[38;5;129m"
cyan = "\033[36m"
reset = "\033[0m"

def regle_devinette() -> None:
    '''
    Affiche les règles du jeu de la devinette
    '''
    clear()
    print("\n---------------------------------",f"{rouge}Règles du jeu{reset}","---------------------------------\n")
    print("  Bienvenue dans le jeu de la devinette !!!")
    print("  Le but du jeu est de deviner le nombre que l'autre joueur a choisi.")
    print("  Le joueur 1 choisit un nombre et le joueur 2 doit le deviner ou inversement.")
    print("  Le joueur qui devine le nombre gagne.")
    print("  A chaque essai raté, le joueur perd un point.\n")
    print(f"{violet}  Que le meilleur gagne 😈{reset}\n")
    input("  Appuyez sur 'Entrée' pour continuer")
    
def jeu_j1(joueur1 : str, joueur2 : str) -> int:
    '''
    Fonction qui permet de jouer à la devinette en laissant le joueur 1 choisir le nombre
    
    Args:
        joueur1 (str) : le pseudo du joueur 1
        joueur2 (str) : le pseudo du joueur 2

    Returns:
        points (int) : le nombre de points gagnés
    '''
    n : int
    n = 0
    k : int
    k = -1
    essais : int
    essais = 0
    points : int
    points = 20

    n = (int(getpass.getpass(prompt = f"  {joueur1}, quel nombre voulez-vous faire deviner ? : ", stream = None)))

    while n != k :
        clear()
        print()
        k = int(input(f"  {joueur2}, a quel nombre pensez-vous ? : "))
        print()
        if n == k :
            if essais > 1 :
                print("\n ",joueur2,"vous avez gagné !!! 🥳")
                print("  Vous avez réussi en ", essais, "essais.\n")
                print(f"  Vous avez gagner{rouge} {points}{reset}", "points.\n")
                input("  Appuyez sur 'Entrée' pour continuer")
            else :
                print("\n ",joueur2,"vous avez gagné !!! 🥳")
                print("  Vous avez réussi en ", essais, "essai.\n")
                print(f"  Vous avez gagner{rouge} {points}{reset}", "point.\n")
                input("  Appuyez sur 'Entrée' pour continuer")
        elif k < n :
            print(f"{bleu} ",k,"< n")
            if k <= n - 100:
                print("  T'es aussi proche que la Terre de Pluton\n")
            elif k <= n - 50:
                print("  T'es loooooooooooooooooooooooin\n")
            elif k <= n - 25:
                print("  T'es prooooooooche, non je rigole\n")
            elif k <= n - 10:
                print("  T'es au Sahara ou quoi ?!?!\n")
            elif k <= n - 5:
                print("  Tu crames !!!\n")
            elif k <= n - 1:
                print("  T'es sur le Soleil ou quoi ?!?!\n")
            print(f"{bleu_clair}  Trop petit !{reset}\n")
            essais += 1
            points -= 1
            input("  Appuyez sur 'Entrée' pour continuer")
        elif k > n :
            print(f"{rouge} ",k,"> n")
            if k >= n + 100:
                print("  T'es partis chez les Inuits ???\n")
            elif k >= n + 50:
                print("  Ça caille par ici\n")
            elif k >= n + 25:
                print("  Tu t'es perdu ouuuu ???\n")
            elif k >= n + 10:
                print("  Il fait aussi chaud que dans une soirée info\n")
            elif k >= n + 5:
                print("  C'est un sauna ouuuuu ?!?!\n")
            elif k >= n + 1:
                print("  Je crois t'es tombé dans un volcan\n")
            print(f"{rouge_clair}  Trop grand !{reset}\n")
            essais += 1
            points -= 1
            input("  Appuyez sur 'Entrée' pour continuer")
    return points

def jeu_j2(joueur1 : str, joueur2 : str) -> int:
    '''
    Fonction qui permet de jouer à la devinette en laissant le joueur 2 choisir le nombre

    Args:
        joueur1 (str) : le pseudo du joueur 1
        joueur2 (str) : le pseudo du joueur 2

    Returns:
        points (int) : le nombre de points gagnés
    '''
    n : int
    n = 0
    k : int 
    k = -1
    essais : int
    essais = 0
    points : int
    points = 20
    
    n = (int(getpass.getpass(prompt = f"  {joueur1}, quel nombre voulez-vous faire deviner ? : ", stream = None)))

    while n != k :
        clear()
        print()
        k = int(input(f"  {joueur2}, a quel nombre pensez-vous ? : "))
        print()
        if n == k :
            if essais > 2 :
                print("\n ",joueur2,"vous avez gagné !!! 🥳")
                print("  Vous avez réussi en ", essais, "essais.\n")
                print(f"  Vous avez gagner{rouge} {points}{reset}", "points.\n")
                input("  Appuyez sur 'Entrée' pour continuer")
            else :
                print("\n ",joueur2,"vous avez gagné !!! 🥳")
                print("  Vous avez réussi en ", essais, "essai.\n")
                print(f"  Vous avez gagner{rouge} {points}{reset}", "point.\n")
                input("  Appuyez sur 'Entrée' pour continuer")
        elif k < n :
            print(f"{bleu} ",k,"< n")
            if k <= n - 100:
                print("  T'es aussi proche que la Terre de Pluton\n")
            elif k <= n - 50:
                print("  T'es loooooooooooooooooooooooin\n")
            elif k <= n - 25:
                print("  T'es prooooooooche, non je rigole\n")
            elif k <= n - 10:
                print("  T'es au Sahara ou quoi ?!?!\n")
            elif k <= n - 5:
                print("  Tu crames !!!\n")
            elif k <= n - 1:
                print("  T'es sur le Soleil ou quoi ?!?!\n")
            print(f"{bleu_clair}  Trop petit !{reset}\n")
            essais += 1
            points -= 1
            input("  Appuyez sur 'Entrée' pour continuer")
        elif k > n :
            print(f"{rouge} ",k,"> n")
            if k >= n + 100:
                print("  T'es partis chez les Inuits ???\n")
            elif k >= n + 50:
                print("  Ça caille par ici\n")
            elif k >= n + 25:
                print("  Tu t'es perdu ouuuu ???\n")
            elif k >= n + 10:
                print("  Il fait aussi chaud que dans une soirée info\n")
            elif k >= n + 5:
                print("  C'est un sauna ouuuuu ?!?!\n")
            elif k >= n + 1:
                print("  Je crois t'es tombé dans un volcan\n")
            print(f"{rouge_clair}  Trop grand !{reset}\n")
            essais += 1
            points -= 1
            print()
            input("  Appuyez sur 'Entrée' pour continuer")
    return points

def jeu() -> None:
    '''
    Fonction qui permet de jouer à la devinette en choisissant qui commence
    '''
    from pseudo import choisir_pseudo
    x : int
    x = 0
    points : int
    joueur1 : str
    joueur2 : str

    clear()
    joueur1 = choisir_pseudo()
    clear()
    joueur2 = choisir_pseudo()

    while x != 3:
        clear()
        print(f"\n\t 1-{joueur1} VS 2-{joueur2}")
        print()
        x = int(input("  Qui fait deviner ? (1 ou 2) : "))
        print()
        match x:
            case 1 :
                points = jeu_j1(joueur1,joueur2)
                ajout_score_devinettes(joueur2, points)
                return
            case 2 :
                points = jeu_j2(joueur2,joueur1)
                ajout_score_devinettes(joueur1, points)
                return
            case 3 :
                print("  Fin")
            case _ :
                print("  Erreur de choix")

def devinette_mode() -> None:
    '''
    Fonction qui permet de choisir le mode de jeu de la devinette
    '''
    choix : int
    choix = 0

    while choix != 3:
        clear()
        print("\n------------------",f"{rouge}Devinettes{reset}","------------------\n")
        print("\t", f"{jaune}1 - Joueur contre Joueur{reset}")
        print("\t", f"{cyan}2 - Joueur contre Ordi{reset}")
        print("\t", f"{vert}3 - Quitter{reset}\n")
        print("------------------------------------------------\n")

        choix = int(input("  Choisissez une option : "))
        print()
        
        match choix:
            case 1 :
                jeu()
            case 2 :
                jeu_joueur_ordi()
            case 3 :
                print("  Fin de la partie")
            case _ :
                print("  Erreur de choix")

def devinette() -> None:
    '''
    Fonction qui permet de choisir les options du jeu de la devinette
    '''
    choix : int
    choix = 0

    while choix != 3:

        clear()
        print("\n------------------",f"{rouge}Devinettes{reset}","------------------\n")
        print("\t", f"{jaune}1 - Règles du jeu{reset}")
        print("\t", f"{cyan}2 - Jouer{reset}")
        print("\t", f"{magenta}3 - Quitter{reset}\n")
        print("------------------------------------------------\n")

        choix = int(input("  Choisissez une option : "))
        print()
        
        match choix:
            case 1 :
                regle_devinette()
            case 2 :
                devinette_mode()
            case 3 :
                print("  Fin de la partie")
            case _ :
                print("  Erreur de choix")
