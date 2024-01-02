#!/usr/bin/python3
"""
Returns to-do list information in CSV format for a given employee ID.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    id_ = sys.argv[1]
    user = requests.get(f"{url}/users/{id_}").json()
    uname = user.get("username")
    todos = requests.get(f"{url}/todos", params={"userId": id_}).json()

    with open(f"{id_}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow(
                [id_, uname, t.get("completed"), t.get("title")]
            )
