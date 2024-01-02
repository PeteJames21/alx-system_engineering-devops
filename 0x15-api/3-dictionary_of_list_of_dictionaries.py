#!/usr/bin/python3
"""
Exports the information of all employees to a JSON file.
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_response = requests.get(url + "users")
    users = users_response.json()

    data = {}
    for user in users:
        id_ = user.get("id")
        todos_response = requests.get(url + "todos", params={"userId": id_})
        todos = todos_response.json()

        user_data = []
        for todo in todos:
            task_data = {
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            user_data.append(task_data)

        data[id_] = user_data

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
