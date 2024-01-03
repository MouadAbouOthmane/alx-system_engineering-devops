#!/usr/bin/python3
"""3. Dictionary of list of dictionaries"""


if __name__ == "__main__":
    import json
    import requests

    name_file = 'todo_all_employees.json'

    url_id = f'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url_id)

    users = users.json()

    dicts = {}

    for user in users:
        id = user['id']
        username = user['username']

        dicts[id] = []

        url_todo = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
        todo_list = requests.get(url_todo)
        todo_list = todo_list.json()

        for x in todo_list:
            r = {}
            r['username'] = username
            r['task'] = x['title']
            r['completed'] = x['completed']
            dicts[id].append(r)

    with open(name_file, 'w') as f:
        json.dump(dicts, f)
