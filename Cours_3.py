from datetime import datetime


#Exercice 3:


# 1 avec MAP 

'''
nombres=[1,2,3,5,8]

def myfunc(a):
    return [a * i for i in range(11)]
 
print(list(map(myfunc, nombres)))



# 1 sans MAP 
liste=[]
list_nb=[1,2,3,5,8]
i=0
for i in range(0,5):
    for j in range(1,11):
        liste.append(list_nb[i]*j)

list_1=liste[:10]
list_2=liste[10:20]
list_3=liste[20:30]
list_5=liste[30:40]
list_8=liste[40:50]
print(list_3)

#2
liste_1_10=list(range(1,11))
liste_mult_5=[]
i=0
for i in range(0,10):
    b=str(liste_1_10[i])
    result=str(5*liste_1_10[i])
    ajout=str("5 * "+b+" = "+result)
    liste_mult_5.append(ajout)
print(liste_mult_5)

#3
liste_1_10=list(range(1,12))
test = False
i=0
while test !=True:
    print(f'{5} * {liste_1_10[i]} = {5*liste_1_10[i]}')
    i=i+1
    if 5*liste_1_10[i] >50:
        test=True


#Ex 4 :
i=1
dict ={'a': 42, 'b': 42, 'c': 42, 'd': 42}
for cle in dict.keys():
    if cle =='d':
        a=i-dict.get(cle)
    else:

        a=i*dict.get(cle)
        i=a
        print(a)
print(a)


m=[1,2,3,4,5]
def myfunc_2(a):
    return a*'*'

print(*list(map(myfunc_2,m)),sep=" ")

print(' '.join(list(map(lambda x : x *'*', range(1,6)))))

# Boucle pour chaque ligne
for i in range(1, n + 1):

    for j in range(i):

        print('*', end='')
    print(" ",end=" ")

    

#Ex 6 :

L=[5, 4, 3, 2, 1]
lg = len(L)
for i in range(lg-1):
    m = i
    for j in range(i+1, lg):
        if L[m] > L[j]:   m = j
    L[m], L[i] = L[i], L[m]

'''

#Ex  7:

starting_year=1980
current_year = datetime.now().year
l=[]
for i in range(starting_year-1,current_year):
    l.append(i+1)
print(l)


#Ex 8 :

for i in range(1,11):
    print(i*str(1),end='\n')



#Ex 9 :
n=11
for i in range(1,n):
    print(" "*(n-i)+"["*i+" "+"]"*i,end='\n')

