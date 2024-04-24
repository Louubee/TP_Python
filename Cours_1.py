from random import randrange
import numpy as np

#Exercice 1 :
print('My Python Code Forever')

print('My Python \nCode \nForever')

int_type=1
float_type=1.5
string_type = 'STRING'
boolean_type=bool(True) 
list_type=[1,2,3]
tupl_type=(1,3)
ens_type={1,2,3}
dictionnaire_type={'name':'Alice', 'age' : 30, 'city': 'wonderland'}
null_type=None


my42count='quarante-deux'
print(len(my42count))






#10
my42Type=print(type(boolean_type).__name__)

#11
compute42=str(21*2)
print(type(compute42))


#12
ex_12="42424242"
ex_12 = ex_12.replace("42", "quarante-deux")
print(ex_12)


#13
a = 24
b = 42
a = a + b
b = a - b
a = a - b
print(a,b)


a = 24
b = 42
c=b
b=a
a=c
print(a,b)

