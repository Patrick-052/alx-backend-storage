#!/usr/bin/env python3
""" Using aggregate pipelines to arrange students
    by average score """


def top_students(mongo_collection):
    """ Arranging students by average score """
    result = mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
    return result
