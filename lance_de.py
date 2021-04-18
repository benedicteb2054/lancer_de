import random
print("1: Lancer le dé 0: Quitter le programme")
while True:
    #on demande a l'utilisateur de saisir un nombre
    x=int(input("cliquer sur un bouton "))
    if x==0:
        print('Bye, a la prochaine')
        break
    elif x==1:
        print(random.randint(1,6))
    else:
        print("je n'ai pas compris")