#!/usr/bin/env python3
""" Providing logs stored in MongoDB """
from pymongo import MongoClient


def nginx_logs():
    """ providing nginx stored logs """
    client = MongoClient()
    db = client.logs
    nginx = db.nginx

    print(f"{nginx.estimated_document_count()} logs\nMethods:")
    print(f"\tmethod GET: {nginx.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {nginx.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {nginx.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {nginx.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {nginx.count_documents({'method': 'DELETE'})}")
    print(f"{nginx.count_documents({'method': 'GET', 'path': '/status'})}" +
          " status check")


nginx_logs()
