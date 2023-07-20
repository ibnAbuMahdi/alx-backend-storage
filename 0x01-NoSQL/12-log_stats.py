#!/usr/bin/env python3
""" log doc parsing """
from pymongo import MongoClient

if __name__ != '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    col = client.logs.nginx
    no = col.find().count()

    get = col.find({'method': 'GET'}).count()
    post = col.find({'method': 'POST'}).count()
    put = col.find({'method': 'PUT'}).count()
    patch = col.find({'method': 'PATCH'}).count()
    delete = col.find({'method': 'DELETE'}).count()

    get_path = col.find({'method': 'GET', 'path': '/status'}).count()

    print(str(no) + ' logs')
    print('Methods:')
    print('\t method GET: ' + str(get))
    print('\t method POST: ' + str(post))
    print('\t method PUT: ' + str(put))
    print('\t method PATCH: ' + str(patch))
    print('\t method DELETE: ' + str(delete))
    print(str(get_path) + ' status check')
