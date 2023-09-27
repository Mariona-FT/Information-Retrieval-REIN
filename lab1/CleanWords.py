"""
.. module:: CleanWords

Cleanwords
**********

:Description: CleanWord

:Version: 

:Date:  1/09/2023

"""

from __future__ import print_function
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from elasticsearch.exceptions import NotFoundError, TransportError

import argparse

## funció CLEAN
##
## borrar les paraules que tinguin un index molt alt i molt baix 1-5

str.isalnum()
str.isascii()
str.isdigit()
str.isnumeric()
str.isspace()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', default=None, required=True, help='Index to search')
 #  parser.add_argument('--alpha', action='store_true', default=False, help='Sort words alphabetically')
    args = parser.parse_args()

    index = args.index

    try:
        client = Elasticsearch(timeout=1000)
        voc = {}
        sc = scan(client, index=index, query={"query" : {"match_all": {}}})
        for s in sc:
            try:
                tv = client.termvectors(index=index, id=s['_id'], fields=['text'])
                if 'text' in tv['term_vectors']:
                    for t in tv['term_vectors']['text']['terms']:
                        if t in voc:
                            voc[t] += tv['term_vectors']['text']['terms'][t]['term_freq']
                        else:
                            voc[t] = tv['term_vectors']['text']['terms'][t]['term_freq']
            except TransportError:
                pass
        lpal = []

        for v in voc:
            lpal.append((v.encode("utf-8", "ignore"), voc[v]))


       #for pal, cnt in sorted(lpal, key=lambda x: x[0 if args.alpha else 1]):
       #     print(f'{cnt}, {pal.decode("utf-8")}')
            
            
        print('--------------------')
        print(f'{len(lpal)} Words')
    except NotFoundError:
        print(f'Index {index} does not exist')
        
        
