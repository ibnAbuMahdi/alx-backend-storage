#!/user/bin/env python3
""" 9 insert school """

if __name__ != "__main__":
    def insert_school(c, **kwargs):
        """ inserts a doc in cln """
        return c.insert_one(kwargs).inserted_id
