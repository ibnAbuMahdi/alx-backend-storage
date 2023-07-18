#!/usr/bin/env python3
""" update topics """


if __name__ != "__main__":
    def update_topics(c, n, t):
        """ update topics """
        c.update_many({'name': n}, {'$set': {'topics': t}})
