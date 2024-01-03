#!/usr/bin/python3
"""1. Export to CSV"""


if __name__ == "__main__":
    import requests
    from sys import argv

    id = argv[1]
    name_file = '{}.csv'.format(id)

    url_id = f'https://jsonplaceholder.typicode.com/users?id={id}'
    url_todo = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    todo_list = requests.get(url_todo)
    user = requests.get(url_id)

    user = user.json()
    todo_list = todo_list.json()

    user_name = user[0]['username']

    with open(name_file, 'w') as f:
        for x in todo_list:
            line = '"{0}","{3}","{2}","{1}"\n'.format(
                x['userId'], x['title'],
                x['completed'], user_name)
            f.write(line)
