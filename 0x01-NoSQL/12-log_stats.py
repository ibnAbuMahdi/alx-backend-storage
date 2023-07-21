#!/usr/bin/env python3
""" log doc parsing """
from pymongo import MongoClient

if __name__ != '__main__':
    client = MongoClient("mongodb://127.0.0.1:27017")
    col = client.logs.nginx
    no = col.count_documents()

    get = col.count_documents({"method": "GET"})
    post = col.count_documents({"method": "POST"})
    put = col.count_documents({"method": "PUT"})
    patch = col.count_documents({"method": "PATCH"})
    delete = col.count_documents({"method": "DELETE"})

    get_path = col.count_documents({"path": "/status"})

    print(str(no) + " logs")
    print("Methods:")
    print("\t method GET: " + str(get))
    print("\t method POST: " + str(post))
    print("\t method PUT: " + str(put))
    print("\t method PATCH: " + str(patch))
    print("\t method DELETE: " + str(delete))
    print(str(get_path) + " status check")
