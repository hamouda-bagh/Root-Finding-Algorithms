import numpy as np
import matplotlib.pyplot as plt
import time

f=input("Donner l'expreesion de la fonction: ")
a=float(input("Donner le début de l'intervalle: "))
b=float(input("Donner la fin de l'intervalle: "))
e=float(input("Donner l'erreur"))

x = np.linspace(a, b, 100)

t1=time.time()
def fct(f,x):
    r = eval(f)
    return r #On définit la fonction qu'on souhaitera chercher la racine

if fct(f,a)*fct(f,b) < 0 :    

    if abs(fct(f,a))<abs(fct(f,b)) : #a est une meilleure aproximtion que b
        a,b=b,a

    c=a
    mflag=True
    i=0
    
    while fct(f,b)!=0 and abs(b-a)>e : #condition de convergence
        i+=1
        if fct(f,a)!=fct(f,c) and fct(f,b)!=fct(f,c) : #interpolation quadratique inverse
            s= (a*fct(f,b)*fct(f,c)) / ((fct(f,a)-fct(f,b))*(fct(f,a)-fct(f,c)))
            s+= (b*fct(f,a)*fct(f,c)) / ((fct(f,b)-fct(f,a))*(fct(f,b)-fct(f,c)))
            s+= (c*fct(f,a)*fct(f,b)) / ((fct(f,c)-fct(f,a))*(fct(f,c)-fct(f,b)))
                 
        else :
            s= b - fct(f,b)*(b-a)/(fct(f,b)-fct(f,a)) #méthode de la sécante
        
        if (s < min((3*a+b)/4,b) or s > max((3*a+b)/4,b)) or (mflag==True and abs(s-b)>=abs(b-c)/2) or (mflag==False and abs(s-b)>=abs(c-d)/2):
            #la condition pour accepter la valeur d'interpolation s 
            s=(a+b)/2 #méthode de la dichotomie
            mflag=True #on a utilisé la méthode de dichotomie
                 
        else:
            mflag=False #on n'a pas utilisé la méthode de dichotomie
                 
        print ("Affichage de l'itération",i,":")
        print (s,fct(f,s))
        plt.plot(s, fct(f,s), color='blue', marker='o')
        
        d=c
        c=b
                 
        if fct(f,a)*fct(f,s)<0 :
            b=s
        else:    
            a=s
                 
        if abs(fct(f,a))<abs(fct(f,b)): #a est une meilleure aproximtion que b
            a,b=b,a
            
    print ("Affichage du résultat :")
    print (b)
    print("Le nombre d'itérations final est:", i)
    
    plt.plot(x, fct(f,x), label='Courbe de f', linewidth=2, color='green')
    plt.plot(b,fct(f,b),color='red',marker='*', label='Point final')
    plt.legend()
    print("Temps d'exécution est " ,time.time()-t1)