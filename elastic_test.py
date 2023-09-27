"""
.. module:: elastictest

elastictest
***********

:Description: elastictest

    Queries Elasticsearch to see if it is up


:Version: 

:Date:  1/09/2023
"""

from __future__ import print_function
import requests

__author__ = 'neus'

if __name__ == '__main__':
    try:
        resp = requests.get('http://localhost:9200/?pretty')
        print(resp.content)
    except Exception:
        print('Elastic search is not running')
