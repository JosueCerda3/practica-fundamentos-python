#Bibliotecas
import random
import matplotlib.pyplot as plt

#generar numeros aletorios 
print(random.randrange(10,100,2))

#reacomodar una lista al azar
lista=[1,2,3,4,5,6,7,8,9,10]
print('Lista original',lista)
random.shuffle(lista)
print('Lista mix',lista)

#generar un grafico de campana de gauss
#generar datos de la campana
campana= [random.gauss(1,0.5) for i in range(1000)]
#graficar
#arma la grafica
plt.hist(campana, bins=15)
#muestra la grafica
plt.show()