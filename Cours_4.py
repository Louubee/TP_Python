from datetime import datetime
import time
#1
'''

def myPutStr():
    b=input("Entrez du texte : ")
    if type(b) is str:
        b=f'Vous avez bien entrer un string'
    b="Et pourquoi pas 42 ? "
    return b





def computeSurfaceM2():
    a=int(input("Quelle est la longueur de votre piece en m2 : "))
    b=int(input("Quelle est la largeur  de votre piece en m2 : "))
    c=a*b
    return (print(f'Votre surface et de {c} m2'))




def detectMyAgeByNight(age):
    

    if age >=0 and age <= 17:
        return f'Vous ne pouvez pas entrer vous n\’êtes pas majeur vous avez {age}'
    elif age >17 and age <=41 :
        return f'Vous pouvez entrer vous êtes majeur vous avez {age}'
    elif age > 41 and age < 100 :
        return "Vous êtes patron de la boite de nuit"
    else:
        return "Votre age n'est pas correct"

detectMyAgeByNight(int(input("Donnez votre age : ")))


    
def tableGenerator(liste):
    for i in range(0,len(liste)):
        print('')
        if i ==0:
            mot_long=max(liste[i], key=len)
            len_mot_long=len(mot_long)

        elif i ==1:
            for k in range(0,len(liste)-1):
                print(' | ',(1+len_mot_long)*'-', end=' ')
            print(' | ')

        for j in range(0,len(liste[i])):
    
            b=len(str(liste[i][j]))
            a=len_mot_long-b
            print(' | ',liste[i][j],a*' ', end=' ')
        print(' | ',end='')




liste=[['pommade','test1','test2','test3'],['Data1',15689,2,3],['Data2',10,45,89],['Data3',78,123,56],[0,2,6978841,6]]
print(len(liste))
tableGenerator(liste)





test=True

while test == True:
    now = datetime.now()
    formatted = now.strftime("%H:%M:%S")
    print(formatted)
    time.sleep(1)
'''


    

def is_palindrome(a):
    l=[]
    N=len(a)
    for i in range(0,N):
        if a[i]==a[N-1-i]:
            l.append("Oui")
        else:
            l.append("Non")
    if "Non" in l:
        return False
    else:
        return True

'''
def FibRec(a):  

   if a <= 1:  

       return a  

   else:  

       return(FibRec(a-1) + FibRec(a-2))  

aterms = int(input("Enter the terms? ")) 

l=[]
if aterms <= 0:  

   print("Please enter a positive integer")  

else:  

   print("Fibonacci :")  

   for z in range(aterms):  
    l.append(FibRec(z))
print(l)



'''