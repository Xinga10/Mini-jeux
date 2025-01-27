from typing import BinaryIO
import pickle
from sauvegarde import clear

jaune = "\033[33m"
reset = "\033[0m"
gris = "\033[90m"
magenta = "\033[35m"
bleu = "\033[34m"
vert = "\033[32m"

def ajouter_pseudo() -> None:
    '''
    Ajoute un pseudo dans le fichier pseudo.dat
    '''
    f : BinaryIO
    rep : str
    pseudo : str
    try:
        with open("pseudo.dat", "ab") as f:
            rep = 'oui'
            while rep.lower() == 'oui':
                pseudo = input("\n  Entrez un pseudo : ")
                pickle.dump(pseudo, f)
                rep = input("\n  Encore une personne (oui/non) ? : ")
    except FileNotFoundError:
        print("\n  Erreur lors de l'ouverture du fichier.")
        
def choisir_pseudo() -> str:
    '''
    Permet de choisir un pseudo parmi ceux enregistrés dans le fichier pseudo.dat

    return : str
    '''
    from mini_jeu import main_mini_jeu
    f : BinaryIO
    pseudos : list[str]
    pseudo : str
    joueur_actuel : int
    pseudox : str
    try:
        with open("pseudo.dat", "rb") as f:
            pseudos = []
            try:
                while True:
                    pseudo = pickle.load(f)
                    pseudos.append(pseudo)
            except EOFError:
                print()
            
            if not pseudos:
                print("\n  Aucun pseudo enregistré. Veuillez ajouter des pseudos d'abord.")
                main_mini_jeu()
                return ""
                        
            print("\n  Pseudos enregistés :\n")
            for i, pseudox in enumerate(pseudos):
                print(f"  {i + 1}. {pseudox}")
            print()
            while True:
                joueur_actuel = int(input("  Choisissez un pseudo (numéro) : "))
                if 1 <= joueur_actuel <= len(pseudos):
                    return pseudos[joueur_actuel - 1]
                else:
                    print("\n  Choix invalide. Veuillez réessayer.")
    except FileNotFoundError:
        print("\n  Aucun pseudo enregistré. Veuillez ajouter des pseudos d'abord.")
        ajouter_pseudo()
        return ""
    
def ajouter_pseudo_bot() -> None:
    '''
    Ajoute un pseudo pour le bot dans le fichier pseudo_bot.dat
    '''
    f : BinaryIO
    rep : str
    pseudo_bot : str
    try:
        with open("pseudo_bot.dat", "ab") as f:
            rep = 'oui'
            while rep.lower() == 'oui':
                pseudo_bot = input("\n  Entrez un pseudo_bot : ")
                pickle.dump(pseudo_bot, f)
                rep = input("\n  Encore un pseudo_bot (oui/non) ? : ")
    except FileNotFoundError:
        print("\n  Erreur lors de l'ouverture du fichier.")

def choisir_pseudo_bot() -> str:
    '''
    Permet de choisir un pseudo pour le bot parmi ceux enregistrés dans le fichier pseudo_bot.dat

    return : str
    '''
    from mini_jeu import main_mini_jeu
    f : BinaryIO
    pseudos_bot : list[str]
    pseudo_bot : str
    joueur_actuel : int
    pseudox : str
    try:
        with open("pseudo_bot.dat", "rb") as f:
            pseudos_bot = []
            try:
                while True:
                    pseudo_bot = pickle.load(f)
                    pseudos_bot.append(pseudo_bot)
            except EOFError:
                print()
            
            if not pseudos_bot:
                print("\n  Aucun pseudo_bot enregistré. Veuillez ajouter des pseudos_bot d'abord.")
                main_mini_jeu()
                return ""
                        
            print("\n  Pseudos_bot enregistés :\n")
            for i, pseudox in enumerate(pseudos_bot):
                print(f"  {i + 1}. {pseudox}")
            print()
            while True:
                joueur_actuel = int(input("  Choisissez un pseudo_bot (numéro) : "))
                if 1 <= joueur_actuel <= len(pseudos_bot):
                    return pseudos_bot[joueur_actuel - 1]
                else:
                    print("\n  Choix invalide. Veuillez réessayer.")
    except FileNotFoundError:
        print("\n  Aucun pseudo_bot enregistré. Veuillez ajouter des pseudos_bot d'abord.")
        ajouter_pseudo()
        return ""
    
def pseudo() -> None:
    '''
    Menu pour ajouter un pseudo
    '''
    choix = int
    choix = 0

    while choix != 2:
        clear()
        print("\n-----------------",f"{jaune}Pseudos{reset}","-----------------\n")
        print("\t", f"{gris}1 - Ajouter un pseudo{reset}")
        print("\t", f"{magenta}2 - Mettre un pseudo au bot{reset}","\n")
        print("\t", f"{bleu}3 - Quitter{reset}","\n")
        print("-------------------------------------------\n")

        choix = int(input("  Choisissez une option : "))
        print()

        match choix:
            case 1 :
                ajouter_pseudo()
                return
            case 2 :
                ajouter_pseudo_bot()
                return
            case 3 :
                print("\n  Quitter")
            case _ :
                print("\n  Erreur de choix")