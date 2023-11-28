import csv
import numpy as np
from scipy.optimize import curve_fit

# Inicialitzar varialbes
_numOfDocs = 5
_globatTotalWords = []
_globalDifferentWords = []

def HEAPS(n, k, b):
    return k * (n ** b)


for i in range(1,_numOfDocs+1):
    _totalWords = 0
    _difWords = 0
    final = False
    # Num dels arxius de text
    archivo_csv = "textos" + str(i) + ".csv"

    # Obrir el arxiu CSV 
    with open(archivo_csv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        # Recorrer cada fila del CSV
        for row in csvreader:
        # obtenir el primer valor de la columna(suposant que la primera columna es la que contiene las palabras)
            palabra = row[0]

            if final: # Guardar ultim valor primera columna
                palabra = palabra.split(" ")
                _difWords = int(palabra[0])
            else:
                try: # Sumar el valor a _totalWords
                    _totalWords += int(palabra)
                except:
                    final = True
    
    _globatTotalWords.append(_totalWords)
    _globalDifferentWords.append(_difWords)

# Imprimir els resultats
print("Total de paraules:", _globatTotalWords)
print("Última paraula diferent:", _globalDifferentWords)

_globatTotalWords = np.array(_globatTotalWords)
_globalDifferentWords = np.array(_globalDifferentWords)

estimated, cov = curve_fit(HEAPS, _globatTotalWords, _globalDifferentWords)
_k, _b = estimated

print("Estimat per K: " + str(_k) + " //Estimat per  B: " + str(_b))
