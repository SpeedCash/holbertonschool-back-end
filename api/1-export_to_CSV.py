#!/usr/bin/python3


"""
This script retrieves user and their tasks data from JSONPlaceholder API and saves it to a CSV file.
It uses user ID provided as a command-line argument to fetch and save the data.

"""


import urllib.request
import sys
import json
import csv


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

    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, user.get('username'),
                             task.get('completed'), task.get('title')])


if __name__ == "__main__":
    main()
