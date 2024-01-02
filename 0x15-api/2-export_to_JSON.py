#!/usr/bin/python3
"""
Returns to-do list information in JSON format for a given employee ID.
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    id_ = sys.argv[1]
    user = requests.get(f"{url}/users/{id_}").json()
    uname = user.get("username")
    todos = requests.get(f"{url}/todos", params={"userId": id_}).json()

    with open(f"{id_}.json", "w") as f:
        json.dump({id_: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": uname
            } for t in todos]}, f)
