#!/usr/bin/env python3
""" Providing logs stored in MongoDB """
from pymongo import MongoClient


def nginx_logs(mongo_collection):
    """ providing nginx stored logs """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{mongo_collection.estimated_document_count()} logs")
    print("Methods:")
    for i in methods:
        count = mongo_collection.count_documents({'method': i})
        print(f"\tmethod {i}: {count}")

    print(f"{mongo_collection.count_documents({'path': '/status'})}" +
          " status check")

    print("IPs:")
    ip_counts = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for doc in ip_counts:
        print(f"{doc['_id']}: {doc['count']}")


if __name__ == "__main__":
    nginx = MongoClient(host='localhost', port=27017).logs.nginx
    nginx_logs(nginx)
