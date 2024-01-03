#!/usr/bin/python3
"""2. Export to JSON"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    id = argv[1]
    name_file = '{}.json'.format(id)

    url_id = f'https://jsonplaceholder.typicode.com/users?id={id}'
    url_todo = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    user = requests.get(url_id)
    todo_list = requests.get(url_todo)

    user = user.json()
    todo_list = todo_list.json()

    user_name = user[0]['username']

    dic = {id: []}

    for x in todo_list:
        r = {}
        r['task'] = x['title']
        r['completed'] = x['completed']
        r['username'] = user_name
        dic[id].append(r)

    with open(name_file, 'w') as f:
        json.dump(dic, f)
