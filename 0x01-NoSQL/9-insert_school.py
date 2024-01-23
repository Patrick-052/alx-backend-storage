#!/usr/bin/env python3
""" Inserting a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a document and returns an object id """
    coll_dict = {k: v for k, v in kwargs.items()}
    result = mongo_collection.insert_one(coll_dict)
    return result.inserted_id
