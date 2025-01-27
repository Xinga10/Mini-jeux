from devinette import *
from allumette import *
from morpion import morpion
from puissance4 import *
from pseudo import *
from score import *
from sauvegarde import *

vert = "\033[32m"
cyan = "\033[36m"
reset = "\033[0m"
gris = "\033[90m"
orange = "\033[91m"
magenta = "\033[95m"
jaune_clair = "\033[93m"
rose = "\033[38;5;206m"
rouge = "\033[38;5;196m"
bleu = "\033[38;5;27m"

def main_mini_jeu() -> None:
    '''
    Fonction principale du mini jeu
    '''
    choix : int
    choix = 0

    clear()
    print(f"{rouge}\n  🚨 Pensez à ajouter des pseudos avant de jouer ! 🚨\n{reset}")
    print("\n  A chaque fin de partie les scores sont sauvegardés\n")
    input("  Appuyez sur 'Entrée' pour continuer")

    while choix != 8:
        clear()
        print("\n----------------",f"{magenta}Menu{reset}","----------------","\n")
        print("\t", f"{rouge}1 - Devinettes{reset}")
        print("\t", f"{jaune_clair}2 - Allumettes{reset}")
        print("\t", f"{cyan}3 - Morpion{reset}")
        print("\t", f"{vert}4 - Puissance 4{reset}")
        print("\t", f"{rose}5 - Score et Classement{reset}")
        print("\t", f"{gris}6 - Pseudo{reset}")
        print("\t", f"{bleu}7 - Sauvegarde{reset}")
        print("\t", f"{orange}8 - Quitter{reset}","\n")
        print("---------------------------------------","\n")

        choix = int(input("  Choisissez un jeu ou une option : "))
        print()
        
        match choix:
            case 1 :
                devinette()            
            case 2 :
                allumette()
            case 3 :
                morpion()
            case 4 :
                puissance4()
            case 5 :
                score()
            case 6 :
                pseudo()
            case 7 :
                sauvegarde()
            case 8 :
                print("  Fin de session de jeu")
            case _ :
                print("  Erreur de choix")

if __name__ == "__main__" :
    '''
    Lancement du mini jeu
    '''
    main_mini_jeu()