from typing import BinaryIO
import pickle
from sauvegarde import *

vert = "\033[32m"
bleu = "\033[34m"
magenta = "\033[35m"
orange = "\033[91m"
violet_fonce = "\033[38;5;57m"
gris = "\033[90m"
reset = "\033[0m"

def ajout_score_devinettes(pseudo : str, points : int) -> None:
    '''
    Ajoute un score dans le fichier score_devinettes.dat
    
    Args:
        pseudo (str) : le pseudo du joueur
        points (int) : le nombre de points gagnés
    '''
    f : BinaryIO
    try:
        with open("score_devinettes.dat", "ab") as f:
            pickle.dump((pseudo, points), f)
    except FileNotFoundError:
        with open("score_devinettes.dat", "wb") as f:
            pickle.dump((pseudo, points), f)
        
def afficher_score_devinettes() -> None:
    '''
    Affiche le classement des scores des devinettes
    '''
    f : BinaryIO
    score : list[tuple[str, int]]
    score_list : list[tuple[str, int]]
    score_general : list[tuple[str, int]]
    score : list[tuple[str, int]]
    i : int
    scorex : tuple[str, int]
    mpseudo : str
    mpoints : int

    try:
        clear()
        with open("score_devinettes.dat", "rb") as f:
            score_list = []
            while True:
                try:
                    score = pickle.load(f)
                    if isinstance(score, tuple) and len(score) == 2:
                        score_list.append(score)
                except EOFError:
                    break
            if len(score_list) == 0:
                print("\n  Aucun score enregistré.\n")
                input("  Appuyez sur 'Entrée' pour continuer")
                return
            print("\n  Classement Devinettes :\n")
            score_general = []
            for pseudo, points in score_list:
                for i, (mpseudo, mpoints) in enumerate(score_general):
                    if mpseudo == pseudo:
                        score_general[i] = (mpseudo, mpoints + points)
                        break
                else:
                    score_general.append((pseudo, points))
            
            score_general.sort(key=lambda x: x[1], reverse=True)
            for i, scorex in enumerate(score_general):
                print(f"\t{i + 1}. {scorex[0]} : {scorex[1]} points")
        print()
        input("  Appuyez sur 'Entrée' pour continuer")
    except FileNotFoundError:
        print("  Aucun score enregistré.")

def ajout_score_allumettes(pseudo : str, points : int) -> None:
    '''
    Ajoute un score dans le fichier score_allumettes.dat

    Args:
        pseudo (str) : le pseudo du joueur
        points (int) : le nombre de points gagnés
    '''
    f : BinaryIO
    try:
        with open("score_allumettes.dat", "ab") as f:
            pickle.dump((pseudo, points), f)
    except FileNotFoundError:
        with open("score_allumettes.dat", "wb") as f:
            pickle.dump((pseudo, points), f)

def afficher_score_allumettes() -> None:
    '''
    Affiche le classement des scores des allumettes
    '''
    f : BinaryIO
    score : list[tuple[str, int]]
    score_list : list[tuple[str, int]]
    score_general : list[tuple[str, int]]
    score : list[tuple[str, int]]
    i : int
    scorex : tuple[str, int]
    mpseudo : str
    mpoints : int

    try:
        clear()
        with open("score_allumettes.dat", "rb") as f:
            score_list = []
            while True:
                try:
                    score = pickle.load(f)
                    if isinstance(score, tuple) and len(score) == 2:
                        score_list.append(score)
                except EOFError:
                    break
            if len(score_list) == 0:
                print("\n  Aucun score enregistré.\n")
                input("  Appuyez sur 'Entrée' pour continuer")
                return
            print("\n  Classement Allumettes :\n")
            score_general = []
            for pseudo, points in score_list:
                for i, (mpseudo, mpoints) in enumerate(score_general):
                    if mpseudo == pseudo:
                        score_general[i] = (mpseudo, mpoints + points)
                        break
                else:
                    score_general.append((pseudo, points))
            
            score_general.sort(key=lambda x: x[1], reverse=True)
            for i, scorex in enumerate(score_general):
                print(f"\t{i + 1}. {scorex[0]} : {scorex[1]} points")
        print()
        input("  Appuyez sur 'Entrée' pour continuer")
    except FileNotFoundError:
        print("  Aucun score enregistré.")

def ajout_score_morpion(pseudo : str, points : int) -> None:
    '''
    Ajoute un score dans le fichier score_morpion.dat

    Args:
        pseudo (str) : le pseudo du joueur
        points (int) : le nombre de points gagnés
    '''
    f : BinaryIO
    try:
        with open("score_morpion.dat", "ab") as f:
            pickle.dump((pseudo, points), f)
    except FileNotFoundError:
        with open("score_morpion.dat", "wb") as f:
            pickle.dump((pseudo, points), f)

def afficher_score_morpion() -> None:
    '''
    Affiche le classement des scores du morpion
    '''
    f : BinaryIO
    score : list[tuple[str, int]]
    score_list : list[tuple[str, int]]
    score_general : list[tuple[str, int]]
    score : list[tuple[str, int]]
    i : int
    scorex : tuple[str, int]
    mpseudo : str
    mpoints : int

    try:
        clear()
        with open("score_morpion.dat", "rb") as f:
            score_list = []
            while True:
                try:
                    score = pickle.load(f)
                    if isinstance(score, tuple) and len(score) == 2:
                        score_list.append(score)
                except EOFError:
                    break
            if len(score_list) == 0:
                print("\n  Aucun score enregistré.\n")
                input("  Appuyez sur 'Entrée' pour continuer")
                return
            print("\n  Classement Morpion :\n")
            score_general = []
            for pseudo, points in score_list:
                for i, (mpseudo, mpoints) in enumerate(score_general):
                    if mpseudo == pseudo:
                        score_general[i] = (mpseudo, mpoints + points)
                        break
                else:
                    score_general.append((pseudo, points))
            
            score_general.sort(key=lambda x: x[1], reverse=True)
            for i, scorex in enumerate(score_general):
                print(f"\t{i + 1}. {scorex[0]} : {scorex[1]} points")
        print()
        input("  Appuyez sur 'Entrée' pour continuer")
    except FileNotFoundError:
        print("  Aucun score enregistré.")

def ajout_score_puissance4(pseudo : str, points : int) -> None:
    '''
    Ajoute un score dans le fichier score_puissance4.dat

    Args:
        pseudo (str) : le pseudo du joueur
        points (int) : le nombre de points gagnés
    '''
    f : BinaryIO
    try:
        with open("score_puissance4.dat", "ab") as f:
            pickle.dump((pseudo, points), f)
    except FileNotFoundError:
        with open("score_puissance4.dat", "wb") as f:
            pickle.dump((pseudo, points), f)

def afficher_score_puissance4() -> None:
    '''
    Affiche le classement des scores du Puissance 4
    '''
    f : BinaryIO
    score : list[tuple[str, int]]
    score_list : list[tuple[str, int]]
    score_general : list[tuple[str, int]]
    score : list[tuple[str, int]]
    i : int
    scorex : tuple[str, int]
    mpseudo : str
    mpoints : int

    try:
        clear()
        with open("score_puissance4.dat", "rb") as f:
            score_list = []
            while True:
                try:
                    score = pickle.load(f)
                    if isinstance(score, tuple) and len(score) == 2:
                        score_list.append(score)
                except EOFError:
                    break
            if len(score_list) == 0:
                print("\n  Aucun score enregistré.\n")
                input("  Appuyez sur 'Entrée' pour continuer")
                return
            print("\n  Classement Puissance4 :\n")
            score_general = []
            for pseudo, points in score_list:
                for i, (mpseudo, mpoints) in enumerate(score_general):
                    if mpseudo == pseudo:
                        score_general[i] = (mpseudo, mpoints + points)
                        break
                else:
                    score_general.append((pseudo, points))
            
            score_general.sort(key=lambda x: x[1], reverse=True)
            for i, scorex in enumerate(score_general):
                print(f"\t {i + 1}. {scorex[0]} : {scorex[1]} points")
        print()
        input("  Appuyez sur 'Entrée' pour continuer")
    except FileNotFoundError:
        print("  Aucun score enregistré.")

def score() -> None:
    '''
    Menu pour afficher les scores
    '''
    choix = int
    choix = 0

    while choix != 5:
        clear()
        print("\n----------------",f"{magenta}Score et Classement{reset}","----------------","\n")
        print("\t", f"{violet_fonce}1 - Classement Devinettes{reset}")
        print("\t", f"{orange}2 - Classement Allumettes{reset}")
        print("\t", f"{gris}3 - Classement Morpion{reset}")
        print("\t", f"{bleu}4 - Classement Puissance 4{reset}")
        print("\t", f"{vert}5 - Quitter{reset}","\n")
        print("-----------------------------------------------------","\n")

        choix = int(input("  Choisissez une option : "))
        print()

        match choix:
            case 1 :
                afficher_score_devinettes()
            case 2 :
                afficher_score_allumettes()
            case 3 :
                afficher_score_morpion()
            case 4 :
                afficher_score_puissance4()
            case 5 :
                print("  Quitter")
            case _ :
                print("  Erreur de choix")
