# -*-coding:Latin-1 -*

import os

nb_u = input("Tapez un nombre pour obtenir sa table de multiplication")
nb = int(nb_u)
MAX_u = input("Tapez le chiffre maximal pour lequel vous voulez obtenir sa table de multiplication")
MAX = int(MAX_u)

def table_multiplication(nb, MAX):
    i = -1
    while i<MAX:
        print(nb,"*",(i+1),"=", nb*(i+1))
        i += 1
        
print (table_multiplication(nb,MAX))

os.system("pause")
