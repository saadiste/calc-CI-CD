"""
Un script aaaaaaa python prenant 3 arguments dont le premier est l'opération voulue et les deux suivants 
les deuaaaa entierss 
"""

import calc
import sys

print("Bienvenue dans cette petite calculatrice sous Python pour entier.\n")


def run_calc():
    op = input("Choisissez une opération entre +, -, x , / et %      : \n")
    term_1 = input("Entrer votre premier entier \n")
    term_2 = input("Enter votre second entier \n")
    res = calc.ope(op, term_1, term_2)
    if res != None:
        print("{} {} {} = {}".format(term_1, op, term_2, res))
        keep_going = input(
            "Voulez-vous stopper le programme ? Écrivez Oui, dans ce cas\n"
        )
        if keep_going == "Oui":
            sys.exit(0)
    print("Nous allons recommencer le programme\n")
    run_calc()


run_calc()
