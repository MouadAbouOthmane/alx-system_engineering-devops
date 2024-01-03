#!/usr/bin/python3
"""0. Gather data from an API"""


if __name__ == "__main__":
    import requests
    from sys import argv

    id = argv[1]

    url_id = f'https://jsonplaceholder.typicode.com/users?id={id}'
    url_todo = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    user = requests.get(url_id)
    todo_list = requests.get(url_todo)

    user = user.json()
    todo_list = todo_list.json()

    user_name = user[0]['name']
    total_number = len(todo_list)
    num_task_done = 0
    task_title = ""
    for x in todo_list:
        if x['completed']:
            num_task_done += 1
            task_title += '\t '
            task_title += x['title']
            task_title += '\n'

    print(f"Employee {user_name} is done with tasks",
          f"({num_task_done}/{total_number}):", sep='')
    print(task_title, end='')
