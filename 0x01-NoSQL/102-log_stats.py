#!/usr/bin/env python3
""" Providing logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    """ Provides log stats, IP addresses and their count """
    nginx = MongoClient(host='localhost', port=27017).logs.nginx

    print(f"{nginx.estimated_document_count()} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for i in methods:
        count = nginx.count_documents({'method': i})
        print(f"\tmethod {i}: {count}")

    print(f"{nginx.count_documents({'path': '/status'})}" +
          " status check")

    print("IPs:")
    ip_counts = nginx.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {"_id": 0, "ip": "$_id", "count": 1}}
    ])
    for doc in ip_counts:
        doc_ip = doc.get("ip")
        doc_count = doc.get("count")
        print(f"{doc_ip}: {doc_count}")
