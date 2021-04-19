#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pymongo
from pymongo import MongoClient

def main():

    url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = MongoClient(url)
    db = client["test_db"]
    collection = db.tokens_database

    readDB = collection.find_one({}, {"_id": 0})
    print(readDB)

    # Read the values from whitelist, code
    for elem in readDB["whitelist"]:
        print(elem["code"])



if __name__ == "__main__":
    main()
