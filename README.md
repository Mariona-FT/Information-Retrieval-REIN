# REIN
EPSEVG RECUPERACIÓ DE LA INFORMACIÓ Curs 2023-24

En aquest repositori, trobareu tots els fitxers necessaris utilitzats i creats per l'assignatura de Recuperació de la Informació al Curs 2023-24 a la Universitat UPC a EPSEVG.

## Fitxers
A continuació, es detallen els fitxers i projectes penjats en aquest repositori:

### Laboratori 1:
L'Activitat 1 del laboratori implica la configuració d'ElasticSearch i la creació d'un índex per a la col·lecció de documents _20_newsgroups_. Realitzant consultes dins d'aquest índex, compten la freqüència de les paraules, i analitzen les dades segons les Lleis de Zipf i Heaps per comprendre la distribució de les paraules i l'expansió del vocabulari.

- Carpeta general: [lab1](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab1)
  - Enunciat: [1REIN-lab ](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab1/1REIN-lab.pdf)
  - Informe Final: [REIN_Activitat1](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab1/REIN_Activitat1.pdf)

Codis importants del laboratori:
  - Aplicació llei heaps: [llei_heaps.py](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab1/llei_heaps.py)
  - Aplicació llei zipf: [llei_zipf.py](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab1/llei_zipf.py)


### Laboratori 2:
A l'Activitat 2 de REIN, es configura l'ElasticSearch i modifiquen la tokenització i els filtres per observar com aquests canvis afecten la indexació d'un corpus de textos. Experimentant amb diferents tokens i filtres per a analitzar les variacions en el recompte i tipus de paraules indexades. També es calcula la similitud cosinus entre documents usant vectors tf-idf per a determinar la semblança entre textos.

- Carpeta general: [lab2](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab2)
  - Enunciat: [2REIN-lab](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab2/2REIN-lab.pdf)
  - Informe Final: [REIN_Activitat2](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab2/REIN_%20Activitat2.pdf)

Codis importants del laboratori:
  - Aplicació TF-IDF en documents: [TFIDFViewer.py](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab2/TFIDFViewer.py)


### Laboratori 3:
A l'Activitat 3, desenvolupem "Vogue Inspector", un rastrejador web destinat a la pàgina de Vogue Espanya. Aquest rastrejador extreu dades d'articles de moda, com ara títols, contingut i enllaços relacionats, per analitzar tendències actuals. L'extensió del rastrejador permet navegar a través de sub-pàgines per recopilar informació més detallada, la qual s'emmagatzema en un fitxer JSON. Aquestes dades s'integren després amb ElasticSearch per a realitzar consultes.

- Carpeta general: [lab3](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab3)
  - Enunciat: [3REIN-lab](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab3/3REIN-lab.pdf)
  - Informe Final: [REIN_Activitat3](https://github.com/Mariona-FT/Information-Retrieval-REIN/blob/main/lab3/REIN_%20Activitat3.pdf)
 
Codis importants del laboratori:
- Carpeta del rastrejador: [vogue](https://github.com/Mariona-FT/Information-Retrieval-REIN/tree/main/lab3/vogue_lab3)

------------
### Projecte Final: Predicció de l'èxit o l'abandonament acadèmic dels estudiants
Aquest projecte explica la predicció de l'èxit o l'abandonament acadèmic dels estudiants mitjançant l'anàlisi de dades i l'aplicació d'algoritmes predictius. Els materials proporcionats inclouen els informes, la presentació, els scripts de codi font i les dades utilitzades en el projecte.
- Carpeta general: [projecte_Prediccio_Exit_Academic](https://github.com/Mariona-FT/Data-Mining-MIDA/tree/main/projecte_Prediccio_Exit_Academic)
- Informe Final: [Predicció de l'èxit o abandonament acadèmic dels estudiants](https://github.com/Mariona-FT/Data-Mining-MIDA/blob/main/projecte_Prediccio_Exit_Academic/Predicci%C3%B3%20l%E2%80%99%C3%A8xit%20abandonament%20acad%C3%A8mic%20estudiants.pdf)
- Presentació Final: [Presentacio-Predicció de l'èxit o abandonament acadèmic dels estudiants](https://github.com/Mariona-FT/Data-Mining-MIDA/blob/main/projecte_Prediccio_Exit_Academic/Presentacio_Predicci%C3%B3%20de%20l%E2%80%99%C3%A8xit%20o%20abandonament%20acad%C3%A8mic%20dels%20estudiants_Mariona_Farr%C3%A9.pdf)
- Scripts de l'activitat:
  -  [prediccio_exit_academic.ipynb](https://github.com/Mariona-FT/Data-Mining-MIDA/blob/main/projecte_Prediccio_Exit_Academic/prediccio_exit_academic.ipynb) - Jupyter Notebook 
  -  [prediccio_exit_academic.py](https://github.com/Mariona-FT/Data-Mining-MIDA/blob/main/projecte_Prediccio_Exit_Academic/prediccio_exit_academic.py) - Python
- Dades: [predicció academic ](https://github.com/Mariona-FT/Data-Mining-MIDA/blob/main/projecte_Prediccio_Exit_Academic/data.csv)

    Extretes de la web: [archive.ics](https://archive.ics.uci.edu/) sota el nom [Predict Students' Dropout and Academic Success ](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

