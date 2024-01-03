#!/usr/bin/python3
"""1. Export to CSV"""


if __name__ == "__main__":
    import requests
    from sys import argv

    id = argv[1]
    name_file = '{}.csv'.format(id)
    url_todo = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    todo_list = requests.get(url_todo)

    todo_list = todo_list.json()

    with open(name_file, 'w') as f:
        for x in todo_list:
            line = '"{0}","{2}","{1}"\n'.format(x['userId'], x['title'],
                                                x['completed'])
            f.write(line)
