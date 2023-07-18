#!/usr/bin/env python3
""" school with a topic """


if __name__ != '__main__':
    def schools_by_topic(c, t):
        """ return list of schools with topic """
        return list(c.find({'topics': t}))
