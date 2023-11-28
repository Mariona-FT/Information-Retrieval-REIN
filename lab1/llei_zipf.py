import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def llei_zipf(r,k,a):
	return k/(r**a)

def crear_grafics(k,alpha):	
	#recalcular la frequencia trobada -segons alpha i k
	z=[0]*size
	for i in range(len(z)):
		z[i]=llei_zipf(rang[i],k,alpha)
		
	#grafic llei de zipf
	plt.figure(figsize=(10,6))
	plt.scatter(rang,z,marker="s",color='black') 	#frequencia trobada
	plt.scatter(rang,freq,marker="s",color='blue') #frequencia real index
	plt.title("Llei Zipf: power laws ?")
	plt.xlabel("Rang de paraules")
	plt.ylabel("Frequencia de paraules")
	plt.show()

	#grafic log-log
	plt.figure(figsize=(10,6))
	plt.loglog(rang,z,marker="s",color='black') 	#frequencia trobada
	plt.loglog(rang,freq,marker="s",color='blue') #frequencia real index
	plt.title("Llei Zipf: ajustada en log-log")
	plt.xlabel("Rang de paraules")
	plt.ylabel("Frequencia de paraules")
	plt.show()


#llegir el .csv
with open(sys.argv[1],newline='') as File:
	reader=csv.reader(File)
	rows=list(reader)
	rows.pop() #primeres files treure - no info necessaria
	rows.pop()
	
#guardar frequencia i rang de cada paraula
	freq=[]
	rang=[]	
	size=len(rows)
	freq=[0]*size 
	rang=[0]*size

n=1
for row in reversed(rows):
	freq[n-1]=int (row[0])
	rang[n-1]=int(n)
	n=n+1
freq.reverse()
rang.reverse()

#Crear els grafics 
	#retorna parametres k i alpha trobats
param,corv=curve_fit(llei_zipf,rang,freq) 
k,alpha=param
print("Amb els valors donats crea els grafics amb alpha: ",alpha, "i k:",k)
crear_grafics(k,alpha)

	#Usuari donar k i alpha
input_alpha=float(input("Entra un valor per alpha: "))
input_k= float(input("Entra un valor per k: "))

print("Amb els valors donats per L'USUARI crea els grafics amb alpha: ",input_alpha,"i k:" ,input_k)
crear_grafics(input_k,input_alpha)
