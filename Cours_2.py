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


rand=random.randint(0,30)
if rand >=0 and rand <=10:
    print("Cool")
elif rand>10 and rand<21:
    print("Tepid")
elif rand>20 and rand<31:
    print("warm")
print(rand)



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





#Ex4
def story_of_the_dwaf_socks() -> None:
    user_forced_aggreement = input("Do you wish to hear about the dwarf socks?")
    if user_forced_aggreement:
        print("It's about the fantastic story about some mithril socks")
        user_useless_input = input("Guess which material was used to make it?")
        if user_useless_input.lower() == "mithril":
            print("smarty pants are ya? Not that only but also some dragon nostril hair !")
            return
        
        print("Are you brain dead ? Mithril obviously ! Now drink with me !")
        print("The dwarf socks, the dwarf socks it's so good the song is already over")
        return
    
    print("Oya oya, we got some smartass who figured out the response to life, universe and the rest!")
    print("which is shutting the fuck up!")
    return

# story_of_the_dwaf_socks()


#Ex5
# wups_im_commented = "haha"
print(42 if "wups_im_commented" in locals() else "cette variable n'existe pas")


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