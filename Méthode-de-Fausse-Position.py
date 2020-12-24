import numpy as np 
import matplotlib.pyplot as plt
from scipy import misc
import time 

def f(x):
    return x**2-4*x+3
def g(x): #Dérivée seconde de la fonction
    return misc.derivative(f, x, n=2)

def concave(a ,b): #Vérification de la concavité de f
    return (g(a) < 0)

a=float(input("Donner le début de l'intervalle: "))
b=float(input("Donner la fin de l'intervalle: "))
e=float(input("Donner l'erreur"))
t1=time.time()

xx = np.linspace(a, b, 100)

croissante=(f(a)<f(b)) #Vérification de la croissance de f

if (concave == True and croissante == True) or (concave == False and croissante == False):
    x = b
else:
    x = a

i=0    
while True:
    i+=1
    if (concave == True and croissante == True) or (concave == False and croissante == False):
        rslt = a - ( x - a ) * f(a) / ( f(x) - f(a) )
    else:
        rslt = b - (b - x) * f(b) / ( f(b) - f(x) )
    
    print ("Affichage de l'itération",i,":")
    print (rslt,f(rslt))
    plt.plot(rslt, f(rslt), color='blue', marker='o')        
    
    if abs (x - rslt) <= e:
        break
    else:
        x = rslt

print ("Affichage du résultat :")
print (rslt)
print("Le nombre d'itérations final est:", i)
print('temps d exécution est ' ,time.time()-t1)

plt.xlabel('Axe des abscisses') 
plt.ylabel('Axe des ordonnées') 
plt.title('Méthode de Fausse Position')
plt.plot(rslt,f(rslt),color='red',marker='*', label='Point final')
plt.plot(xx, f(xx), label='Courbe de f', linewidth=2, color='green')
plt.legend()