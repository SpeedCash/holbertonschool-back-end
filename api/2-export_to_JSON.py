# This script retrieves data about a user and their tasks from JSONPlaceholder API based on a user ID.
# The data is then saved into a JSON file, with each task's details including completion status and user info.

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

    user_tasks = []
    for task in todos:
        task_info = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        }
        user_tasks.append(task_info)

    tasks_dict = {str(user_id): user_tasks}

    file_name = f"{user_id}.json"
    with open(file_name, 'w') as json_file:
        json.dump(tasks_dict, json_file)


if __name__ == "__main__":
    main()
