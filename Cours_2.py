import random
from datetime import datetime


# Execrice 1 :

age = int(input("Quel est votre age ? "))

if age >=0 and age <= 17:
    print(f'Vous ne pouvez pas entrer vous n\’êtes pas majeur vous avez {age}')
elif age >17 and age <=41 :
    print(f'Vous pouvez entrer vous êtes majeur vous avez {age}')
elif age > 41 and age < 100 :
    print("Vous êtes patron de la boite de nuit")
else:
    print("Votre age n'est pas correct")

#Exercice 2:


a=random.randint(0,30)
if a >=0 and a <=10:
    print("Cool")
elif a>10 and a<21:
    print("Tepid")
elif a>20 and a<31:
    print("warm")
print(a)



#Exercice 3
jour = datetime.now().strftime("%w")

match jour:
    case '1':
        print(f'Nous sommes {jour}')
    case '2':
       print(f'Nous sommes {jour}')
    case '3':
       print(f'Nous sommes {jour}')
    case '4':
        print(f'Nous sommes {jour}')
    case '5':
       print(f'Nous sommes {jour}')
    case '6':
        print(f'Nous sommes {jour}')
    case '7':
        print(f'Nous sommes {jour}')
    case _:
        print(f'Nous sommes {jour}')




#Exercice 4
a=input("Entrer une valeur : ")

if type(a).__name__=='int':
    b=int(input("Entrez une valeur entière :"))
    if b < 50:
        print(f'A={a}')
    elif b == 42:
        print(f'La grande réponse sur la vie, l’univers et le reste ! {b}')
    elif b > 50:
        print(f'A={b}')

if type(a).__name__=='str':
    b=str(input("Entrez une chaine de caractère :"))
    if len(b)<30:
        print(f'Le mot contient {b} caractères')
    elif len(b) == 42:
        print(f'La grande réponse sur la vie, l’univers et le reste ! {b}')
    elif len(b)== 45 :
        print(f'Le mot est trop long. {b} caractères...')

if type(a).__name__=='float':
    b=float(input("Entrez un nombre décimale"))
    if b ==3.14:
        print(f'Vous vous rapprochez de la bonne réponse')
    elif b == 42.0:
        print(f'La grande réponse sur la vie, l’univers et le reste ! {b}')
    elif b > 50:
        print(f'A={b}')        


#Exercice 6
prix_initial=int(input("Entrez le prix de l'article : "))
remise=int(input("Entrez la remise souhaitée :"))
remise=(100-remise)/100
prix_final=prix_initial*remise

if prix_final*2>prix_initial:
        print(f'Le prix final est {prix_final}')
else:
    print('La remise est trop élevé')




#Exerice 7
nombre=int(input("Entrez un nombre "))

if nombre%2==0:
    print(f'Le nombre est pair : {nombre}')
else :
    print(f'Le nombre n\'est pas pair {nombre}')