#!/usr/bin/python3
import urllib.request
import sys
import json


def main():
    if len(sys.argv) < 2:
        return
    user_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode())
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode())

    total_tasks = len(todos)
    done_tasks = sum(1 for task in todos if task.get('completed'))

    print(f"Employee {user.get('name')} is done with\
          tasks({done_tasks}/{total_tasks}):")
    for task in todos:
        if task.get('completed'):
            print(f"\t {task.get('title')}")


if __name__ == "__main__":
    main()
