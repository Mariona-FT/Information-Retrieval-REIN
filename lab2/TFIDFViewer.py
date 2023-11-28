"""
.. module:: TFIDFViewer

TFIDFViewer
***********

    Receives two paths of files to compare 
    (the paths have to be the ones used when 
    indexing the files)


:Date:  04/09/2023
"""

from __future__ import print_function, division
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from elasticsearch.client import CatClient
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Q

import argparse

import numpy as np

def search_file_by_path(client, index, path):
    """
    Search for a file using its path

    :param client:
    :param index:
    :param path:
    :return:
    """
    s = Search(using=client, index=index)
    q = Q('match', path=path)  # exact search in the path field
    s = s.query(q)
    result = s.execute()

    lfiles = [r for r in result]
    if len(lfiles) == 0:
        raise NameError(f'File [{path}] not found')
    else:
        return lfiles[0].meta.id
        
        
def doc_count(client, index):
    """
    Returns the number of documents in an index

    :param client:
    :param index:
    :return:
    """
    return int(CatClient(client).count(index=[index], format='json')[0]['count'])


def document_term_vector(client, index, id):
    """
    Returns the term vector of a document 
    and its statistics as two sorted list
    of pairs (word, count)
    The first one is the frequency of the term 
    in the document, the second one is the number
    of documents that contain the term

    :param client:
    :param index:
    :param id:
    :return:
    """
    termvector = client.termvectors(index=index, id=id, fields=['text'],
                                    positions=False, term_statistics=True)

    file_tf = {}
    file_df = {}

    if 'text' in termvector['term_vectors']:
        for t in termvector['term_vectors']['text']['terms']:
            file_tf[t] = termvector['term_vectors']['text']['terms'][t]['term_freq']
            file_df[t] = termvector['term_vectors']['text']['terms'][t]['doc_freq']
    return sorted(file_tf.items()), sorted(file_df.items())


def toTFIDF(client, index, file_id):
    # Obtenemos el vector de términos y el df (frecuencia de documentos) de los términos
    file_tf, file_df = document_term_vector(client, index, file_id)

    # Calculamos el número de documentos en el índice
    dcount = doc_count(client, index)

    # Calculamos el máximo valor de frecuencia en el documento
    max_freq = max([f for _, f in file_tf])

    # Inicializamos una lista para almacenar los pesos TF-IDF
    tfidfw = []

    for (t, w), (_, df) in zip(file_tf, file_df):
        # Calculamos el TF-IDF para cada término
        tf = w / max_freq  # TF (frecuencia de término)
        idf = np.log(dcount / df)  # IDF (frecuencia inversa de documento)
        tfidf = tf * idf  # TF-IDF

        # Agregamos el término y su peso TF-IDF a la lista
        tfidfw.append((t, tfidf))

    # Normalizamos el vector de peso TF-IDF usando NumPy
    tfidfw_array = np.array([w for _, w in tfidfw])
    magnitude = np.linalg.norm(tfidfw_array)
    normalized_tfidfw = [(t, w / magnitude) for t, w in tfidfw]

    return normalized_tfidfw


def normalize(tw):
    # Extraemos los pesos del vector en un array NumPy
    weights = np.array([w for _, w in tw])

    # Calculamos la magnitud del vector utilizando NumPy
    magnitude = np.linalg.norm(weights)

    # Verificamos que la magnitud no sea cero para evitar divisiones por cero
    if magnitude != 0:
        # Normalizamos cada peso dividiéndolo por la magnitud utilizando NumPy
        normalized_weights = weights / magnitude
    else:
        # Si la magnitud es cero (todos los pesos son cero), devolvemos el vector original
        normalized_weights = weights

    # Combinamos los términos con los pesos normalizados en una lista de tuplas
    normalized = [(t, w) for t, w in zip([t for t, _ in tw], normalized_weights)]

    return normalized


def print_term_weight_vector(twv):
    for term, weight in twv:
        print(f"{term}: {weight}")


def cosine_similarity(tw1, tw2):

    # Obtener los términos comunes entre tw1 y tw2
    common_terms = set([t for t, _ in tw1]) & set([t for t, _ in tw2])

    # Crear listas para almacenar los valores de los términos comunes en tw1 y tw2
    values_tw1 = []
    values_tw2 = []

    # Obtener los valores de los términos comunes y guardarlos en las listas
    for term in common_terms:
        values_tw1.append([w for t, w in tw1 if t == term][0])  # Buscar el valor correspondiente en tw1
        values_tw2.append([w for t, w in tw2 if t == term][0])  # Buscar el valor correspondiente en tw2

    # Calcular el producto escalar entre los vectores normalizados
    dot_product = np.dot(values_tw1, values_tw2)

    return dot_product



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', default=None, required=True, help='Index to search')
    parser.add_argument('--files', default=None, required=True, nargs=2, help='Paths of the files to compare')
    parser.add_argument('--print', default=False, action='store_true', help='Print TFIDF vectors')

    args = parser.parse_args()


    index = args.index

    file1 = args.files[0]
    file2 = args.files[1]

    client = Elasticsearch()

    try:
        # Get the files ids
        file1_id = search_file_by_path(client, index, file1)
        file2_id = search_file_by_path(client, index, file2)
        
        # Compute the TF-IDF vectors
        file1_tw = toTFIDF(client, index, file1_id)
        file2_tw = toTFIDF(client, index, file2_id)

        if args.print:
            print(f'TFIDF FILE {file1}')
            print_term_weight_vector(file1_tw)
            print ('---------------------')
            print(f'TFIDF FILE {file2}')
            print_term_weight_vector(file2_tw)
            print ('---------------------')

        print(f"Similarity = {cosine_similarity(file1_tw, file2_tw):3.5f}")

    except NotFoundError:
        print(f'Index {index} does not exist')
