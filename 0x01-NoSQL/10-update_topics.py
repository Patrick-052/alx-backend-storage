#!/usr/bin/env python3
""" Updating a document field """


def update_topics(mongo_collection, name, topics):
    """ Changing documents topics """
    mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})
