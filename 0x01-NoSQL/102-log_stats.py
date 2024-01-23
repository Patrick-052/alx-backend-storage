#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')

    top_ips = nginx_collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")
    for top_ip in top_ips:
        ip = top_ip.get("ip")
        count = top_ip.get("count")
        print(f'\t{ip}: {count}')

# #!/usr/bin/env python3
# """ Providing logs stored in MongoDB """
# from pymongo import MongoClient


# if __name__ == "__main__":
#     """ Provides log stats, IP addresses and their count """
#     nginx = MongoClient(host='localhost', port=27017).logs.nginx

#     print(f"{nginx.estimated_document_count()} logs")
#     print("Methods:")
#     methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
#     for i in methods:
#         count = nginx.count_documents({'method': i})
#         print(f"\tmethod {i}: {count}")

#     print(f"{nginx.count_documents({'path': '/status'})}" +
#           " status check")

#     print("IPs:")
#     ip_counts = nginx.aggregate([
#         {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
#         {"$sort": {"count": -1}},
#         {"$limit": 10}
#     ])
#     for doc in ip_counts:
#         print(f"{doc['_id']}: {doc['count']}")
