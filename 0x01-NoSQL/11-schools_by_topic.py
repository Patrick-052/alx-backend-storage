#!/usr/bin/env python3
""" Querying a specific field """


def schools_by_topic(mongo_collection, topic):
    """ Finds a list of schools having a specific topic """
    result = mongo_collection.find({"topics": topic})
    return result
