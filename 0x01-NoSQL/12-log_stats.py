#!/usr/bin/env python3
""" log doc parsing """
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("mongodb://127.0.0.1:27017")
    col = client.logs.nginx
    no = col.count_documents({})

    get = col.count_documents({"method": "GET"})
    post = col.count_documents({"method": "POST"})
    put = col.count_documents({"method": "PUT"})
    patch = col.count_documents({"method": "PATCH"})
    delete = col.count_documents({"method": "DELETE"})

    get_path = col.count_documents({"path": "/status"})

    print(str(no) + " logs")
    print("Methods:")
    print("\tmethod GET: " + str(get))
    print("\tmethod POST: " + str(post))
    print("\tmethod PUT: " + str(put))
    print("\tmethod PATCH: " + str(patch))
    print("\tmethod DELETE: " + str(delete))
    print(str(get_path) + " status check")
