from score import *
from sauvegarde import *
from random import randint
import time
from pseudo import choisir_pseudo, choisir_pseudo_bot

rouge = "\033[31m"
magenta = "\033[35m"
jaune = "\033[38;5;226m"
bleu_clair = "\033[38;5;45m"
rouge_clair = "\033[38;5;196m"
violet = "\033[38;5;129m"
cyan = "\033[36m"
reset = "\033[0m"

def devinette_facile() -> None:
    '''
    Fonction qui permet de jouer contre un ordinateur en mode facile avec une recherche aleatoire
    '''
    n : int
    n = 0
    k : int
    k = -1
    debut : float
    fin : float
    temps : float
    limite : int
    limite = -1
    essais : int
    essais = 0
    x : int
    x = 0
    bot : str
    joueur : str
    
    clear()
    joueur = choisir_pseudo()
    clear()
    bot = choisir_pseudo_bot()

    while x != 3:
        clear()
        print(f"\n\t 1-{joueur} VS 2-{bot}")
        print()
        x = int(input("  Qui cherche ? : "))
        print()
        limite = int(input("  Choisissez une limite : "))
        match x:
            case 1:
                n = randint(1, limite)
                while n != k :
                    clear()
                    print()
                    print("  La limite est", limite)
                    print()
                    k = int(input(f"  {joueur}, a quel nombre pensez-vous ? : "))
                    print()
                    if n == k :
                        if essais > 2 :
                            print("\n ",joueur,"vous avez gagné !!! 🥳")
                            print("  Vous avez réussi en ", essais, "essais.\n")
                            input("  Appuyez sur 'Entrée' pour continuer")
                        else :
                            print("\n ",joueur,"vous avez gagné !!! 🥳")
                            print("  Vous avez réussi en ", essais, "essai.\n")
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
                        print()
                        input("  Appuyez sur 'Entrée' pour continuer")
                        x = 3
            case 2:
                n = int(input(f"  {joueur}, choisissez un nombre entre 1 et {limite} : "))
                debut = time.time()
                while n != k:
                    if n == k:
                        fin = time.time()
                        temps = fin - debut
                        print(f"Trouvé ! {bot} a trouvé le nombre {n} en {essais} essais.")
                        print(f"Reussi en {temps} secondes")
                        input("  Appuyez sur 'Entrée' pour continuer")
                    else:
                        k = randint(1, limite)
                        essais += 1
                        while time.time() - debut < 10:
                            print(f"  Trop long, {bot} est trop nul")
                            print("  Tu devrais changer le mode ou reduire le numero secret")
                            input("  Appuyez sur 'Entrée' pour continuer")
                            x = 3
            case _:
                print("  Erreur de choix")

def devinette_intermediaire() -> None:
    '''
    Fonction qui permet de jouer contre un ordinateur en mode intermediaire avec une recherche fractionnée
    '''
    n : int
    n = 0
    k : int
    k = -1
    debut : float
    fin : float
    temps : float
    max_val : int
    min_val : int
    limite : int
    limite = -1
    tier1 : int
    tier2 : int
    essais : int
    essais = 0
    x : int
    x = 0
    min_val : int
    max_val : int
    bot : str
    joueur : str

    clear()
    joueur = choisir_pseudo()
    clear()
    bot = choisir_pseudo_bot()

    while x != 3:
        clear()
        print(f"\n\t 1-{joueur} VS 2-{bot}")
        print()
        x = int(input("  Qui cherche ? : "))
        print()
        limite = int(input("  Choisissez une limite : "))
        match x:
            case 1:
                n = randint(1, limite)
                while n != k :
                    clear()
                    print()
                    print("  La limite est", limite)
                    print()
                    k = int(input(f"  {joueur}, a quel nombre pensez-vous ? : "))
                    print()
                    if n == k :
                        if essais > 2 :
                            print("\n ",joueur,"vous avez gagné !!! 🥳")
                            print("  Vous avez réussi en ", essais, "essais.\n")
                            input("  Appuyez sur 'Entrée' pour continuer")
                        else :
                            print("\n ",joueur,"vous avez gagné !!! 🥳")
                            print("  Vous avez réussi en ", essais, "essai.\n")
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
                        print()
                        input("  Appuyez sur 'Entrée' pour continuer")
                        x = 3
            case 2:
                min_val = 1
                max_val = limite
                tier1 = 0
                tier2 = 0
                n = int(input(f"  {joueur}, choisissez un nombre entre 1 et {limite} : "))
                debut = time.time()
                while n != k:
                    tier1 = min_val + (max_val - min_val) // 3
                    tier2 = min_val + 2 * (max_val - min_val) // 3
                    if n <= tier1:
                        k = (min_val + tier1) // 2 
                    elif n <= tier2:
                        k = (tier1 + tier2) // 2  
                    else:
                        k = (tier2 + max_val) // 2  
                    essais += 1
                    if k < n:
                        min_val = k + 1
                    else:
                        max_val = k - 1
                if n == k:
                    fin = time.time()
                    temps = fin - debut
                    print(f"Trouvé ! {bot} a trouvé le nombre {n} en {essais} essais.")
                    print(f"Reussi en {temps} secondes")
                    input("  Appuyez sur 'Entrée' pour continuer")
                    x = 3
            case _:
                print("  Erreur de choix")

def devinette_difficile() -> None:
    '''
    Fonction qui permet de jouer contre un ordinateur en mode difficile avec une recherche binaire
    '''
    n : int
    n = 0
    k : int
    k = -1
    debut : float
    fin : float
    temps : float
    limite : int
    limite = -1
    essais : int
    essais = 0
    x : int
    x = 0
    min_val : int
    max_val : int
    bot : str
    joueur : str

    clear()
    joueur = choisir_pseudo()
    clear()
    bot = choisir_pseudo_bot()

    while x != 3:
        clear()
        print(f"\n\t 1-{joueur} VS 2-{bot}")
        print()
        x = int(input("  Qui cherche ? : "))
        print()
        limite = int(input("  Choisissez une limite : "))
        match x:
            case 1:
                n = randint(1, limite)
                while n != k :
                    clear()
                    print()
                    print("  La limite est", limite)
                    print()
                    k = int(input(f"  {joueur}, a quel nombre pensez-vous ? : "))
                    print()
                    if n == k :
                        if essais > 2 :
                            print("\n ",joueur,"vous avez gagné !!! 🥳")
                            print("  Vous avez réussi en ", essais, "essais.\n")
                            input("  Appuyez sur 'Entrée' pour continuer")
                        else :
                            print("\n ",joueur,"vous avez gagné !!! 🥳")
                            print("  Vous avez réussi en ", essais, "essai.\n")
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
                        print()
                        input("  Appuyez sur 'Entrée' pour continuer")
                        x = 3
            case 2:
                min_val = 1
                max_val = limite
                n = int(input(f"  {joueur}, choisissez un nombre entre 1 et {limite} : "))
                debut = time.time()
                while n != k:
                    k = (min_val + max_val) // 2
                    essais += 1
                    if k < n:
                        min_val = k + 1
                    else:
                        max_val = k - 1
                if n == k:
                    fin = time.time()
                    temps = fin - debut
                    print(f"Trouvé ! {bot} a trouvé le nombre {n} en {essais} essais.")
                    print(f"Reussi en {temps} secondes")
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
                devinette_facile()
                return
            case 2 :
                devinette_intermediaire()
                return
            case 3 :
                devinette_difficile()
                return
            case 4:
                print("  Retour")
            case _ :
                print("  Erreur de choix")
