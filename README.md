# REIN
EPSEVG RECUPERACIÓ DE LA INFORMACIÓ Curs 2023-24

En aquest repositori, trobareu tots els fitxers necessaris utilitzats i creats per l'assignatura de Recuperació de la Informació al Curs 2023-24 a la Universitat UPC a EPSEVG.

## Fitxers
A continuació, es detallen els fitxers i projectes penjats en aquest repositori:

### Laboratori 1: Configuració d'ElasticSearch i Anàlisi de Text
L'Activitat 1 del laboratori implica la configuració d'ElasticSearch i la creació d'un índex per a la col·lecció de documents _20_newsgroups_. Realitzant consultes dins d'aquest índex, compten la freqüència de les paraules, i analitzen les dades segons les Lleis de Zipf i Heaps per comprendre la distribució de les paraules i l'expansió del vocabulari.

- Carpeta general: [lab1](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab1)
  - Enunciat: [1REIN-lab ](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab1/1REIN-lab.pdf)
  - Informe Final: [REIN_Activitat1](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab1/REIN_Activitat1.pdf)

Codis importants del laboratori:
  - Aplicació llei heaps: [llei_heaps.py](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab1/llei_heaps.py)
  - Aplicació llei zipf: [llei_zipf.py](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab1/llei_zipf.py)


### Laboratori 2: Tokenització i Filtres en ElasticSearch
A l'Activitat 2 de REIN, es configura l'ElasticSearch i modifiquen la tokenització i els filtres per observar com aquests canvis afecten la indexació d'un corpus de textos. Experimentant amb diferents tokens i filtres per a analitzar les variacions en el recompte i tipus de paraules indexades. També es calcula la similitud cosinus entre documents usant vectors tf-idf per a determinar la semblança entre textos.

- Carpeta general: [lab2](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab2)
  - Enunciat: [2REIN-lab](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab2/2REIN-lab.pdf)
  - Informe Final: [REIN_Activitat2](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab2/REIN_%20Activitat2.pdf)

Codis importants del laboratori:
  - Aplicació TF-IDF en documents: [TFIDFViewer.py](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab2/TFIDFViewer.py)


### Laboratori 3: Rastreig Web i Anàlisi de Tendències en Moda
A l'Activitat 3, desenvolupem "Vogue Inspector", un rastrejador web destinat a la pàgina de Vogue Espanya. Aquest rastrejador extreu dades d'articles de moda, com ara títols, contingut i enllaços relacionats, per analitzar tendències actuals. L'extensió del rastrejador permet navegar a través de sub-pàgines per recopilar informació més detallada, la qual s'emmagatzema en un fitxer JSON. Aquestes dades s'integren després amb ElasticSearch per a realitzar consultes.

- Carpeta general: [lab3](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab3)
  - Enunciat: [3REIN-lab](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab3/3REIN-lab.pdf)
  - Informe Final: [REIN_Activitat3](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab3/REIN_%20Activitat3.pdf)
 
Codis importants del laboratori:
- Carpeta del rastrejador: [vogue](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab3/vogue_lab3)


### Laboratori 4: Anàlisi de Xarxes amb PageRank
A l'Activitat 4, utilitzem fitxers de text per construir una xarxa d’aeroports i vols, sobre la qual calculen el [Page Rank](https://ca.wikipedia.org/wiki/PageRank), amb els fitxers [airports.txt](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab4/airports.txt) i [routes.txt](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab4/routes.txt), creem un graf on els nodes són els aeroports (utilitzant codis IATA) i les arestes són les rutes, amb pesos que representen el nombre de rutes entre cada parella d’aeroports. A continuació, apliquen l'algorisme de PageRank per determinar la importància relativa de cada aeroport dins de la xarxa. Els resultats es presenten en una llista ordenada decreixent segons el valor de PageRank de cada aeroport. Utilitzen el codi proporcionat [PageRank.py](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab4/PageRank.py) com a base per aquest càlcul.

- Carpeta general: [lab4](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab4)
  - Enunciat: [4REIN-lab](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab4/4REIN-lab.pdf)
  
Codis importants del laboratori:
- Script càlcul PageRank: [PageRank.py](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab4/PageRank.py)

### Laboratori 5: MapReduce i Anàlisi del SuperMercat
En l'Activitat 5 del laboratori de REIN, es realitzen experiments per determinar l'impacte del nombre de nuclis de processament en l'eficiència de l'execució d'scripts de MapReduce. Utilitzen la biblioteca mrjob de Python per processar dades i analitzar la relació entre els nuclis utilitzats i el temps d'execució, observant que no necessàriament més nuclis resulten en una major eficiència. En aquesta activitat amb la implementació correcta del script [MRMarketBasketAnalysis.py](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab5/MRMarketBasketAnalysis.py) de la lectura de parelles de dades i el càlcul de suport i confiança per a regles d'associació, utilitzant el fitxer [groceries.csv](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab5/groceries.csv) . Com a resultat dels experiments, determinen que l'ús de 2 nuclis és el més òptim per a les seves proves.

- Carpeta general: [lab5](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab5)
  - Enunciat: [5REIN-lab](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab5/5REIN-lab.pdf)
  - Informe Final: [REIN_Activitat5](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab5/REIN_Activitat5.pdf)
  
Codis importants del laboratori:
- Script càlcul Anàlisi del Súper: [MRMarketBasketAnalysis.py](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab5/MRMarketBasketAnalysis.py)

### Laboratori 6: Presentació de Temes Avançats
A l'Activitat 6 del laboratori de REIN, haviem de fer una presentació relacionada amb el temari de l'assignatura, el tema triat és **l'estudi de la indexació en galeries de dispositius mòbils**. La presentació aborda com la proliferació de fotos digitals ha creat la necessitat d'una organització més eficient. S'explora la transició de la indexació tradicional a mètodes avançats com el reconeixement facial i l'ús de la intel·ligència artificial (IA) i l'aprenentatge automàtic per millorar la cerca i organització de fotos. També es discuteixen les implicacions de la privacitat i seguretat que comporta l'emmagatzematge de dades personals i com les noves tecnologies poden afectar aquests aspectes. Conclou destacant els beneficis d'aquests avanços alhora que manté la consciència de la importància de la protecció de dades.

- Carpeta general: [lab6](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab6)
  - Presentació: [La indexació a les galeries dels dispositius mòbils](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab6/REIN_Activitat6.pdf)


## Autors

Aquesta repositori ha estat creat per [Mariona Farré](https://github.com/Mariona-FT) i els laboratoris han estat creats amb la col·laboració de [Marc Pérez](https://github.com/marcperezg)


Gràcies per visitar aquest repositori :)

