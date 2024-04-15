#!/usr/bin/python3


"""

This script fetches data on all users and their respective
tasks from JSONPlaceholder API.
It then organizes the tasks per user into a dictionary
and saves it as a JSON file.

"""


import json
import urllib.request


def main():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    with urllib.request.urlopen(users_url) as response:
        users = json.loads(response.read().decode())
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode())

    user_tasks_dict = {}
    for user in users:
        user_id = user.get('id')
        user_tasks = [
            {"username": user.get('username'), "task": todo.get('title'),
             "completed": todo.get('completed')}
            for todo in todos if todo.get('userId') == user_id
        ]
        user_tasks_dict[str(user_id)] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks_dict, json_file)


if __name__ == "__main__":
    main()
