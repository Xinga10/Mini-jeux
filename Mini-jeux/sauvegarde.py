from os import system, name
from time import sleep

def clear():
    '''
    Efface la console
    '''
    #windows
    if name == 'nt':
        _ = system('cls')
    #linux
    else:
        _ = system('clear')

reset = "\033[0m"
bleu = "\033[34m"
jaune = "\033[33m"
rouge = "\033[31m"

def supprimer_donnees() -> None:
    '''
    Supprime toutes les données enregistrées
    '''
    try:
        clear()
        with open("pseudo.dat", "wb"):
            pass
        print("\n  Données de pseudo supprimées\n")
        sleep(0.5)

        with open("pseudo_bot.dat", "wb"):
            pass
        print("  Données de pseudo bot supprimées\n")
        sleep(0.5)

        with open("score_devinettes.dat", "wb"):
            pass
        print("  Données de score devinettes supprimées\n")
        sleep(0.5)

        with open("score_allumettes.dat", "wb"):
            pass
        print("  Données de score allumettes supprimées\n")
        sleep(0.5)

        with open("score_morpion.dat", "wb"):
            pass
        print("  Données de score morpion supprimées\n")
        sleep(0.5)

        with open("score_puissance4.dat", "wb"):
            pass
        print("  Données de score puissance 4 supprimées\n")
        sleep(0.5)

        input("  Appuyez sur 'Entrée' pour continuer")
    except FileNotFoundError:
        print("  Aucune donnée enregistrée.")

def sauvegarde() -> None:
    '''
    Menu de sauvegarde
    '''
    choix : int
    choix = 0

    while choix != 2:
        clear()
        print("\n----------------",f"{bleu}Sauvegarde{reset}","----------------\n")
        print("\t", f"{jaune}1 - Supprimer toutes les données{reset}")
        print("\t", f"{rouge}2 - Quitter{reset}\n")
        print("--------------------------------------------\n")

        choix = int(input("  Choisissez une option : "))
        print()

        match choix:
            case 1 :
                supprimer_donnees()
                return
            case 2 :
                print("  Fin de sauvegarde")
            case _ :
                print("  Erreur de choix")