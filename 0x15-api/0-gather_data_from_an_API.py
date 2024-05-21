#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID """
from re import fullmatch
from requests import get
from sys import argv


API_URL = "https://jsonplaceholder.typicode.com"
"""The RESTAPI's URL"""


if __name__ == "__main__":
    if len(argv) > 1:
        if fullmatch(r"\d+", argv[1]):
            empty_id = int(argv[1])
            empty_resp = get(f"{API_URL}/users/{empty_id}").json()
            tsk_rep = get(f"{API_URL}/todos").json()
            empty_name = empty_resp.get("name")
            task = list(filter(lambda k: k.get("userId") == empty_id, tsk_rep))
            comp_tasks = list(filter(lambda k: k.get("completed"), task))
            print(
                    f"Employee {empty_name} is done with "
                    f"task({len(comp_tasks)}/{len(task)}):"
            )
            for comp_task in comp_tasks:
                print(f"\t {comp_task.get('title')}")
