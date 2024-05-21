#!/usr/bin/python3
"""Python script that uses REST API for a given employee ID"""
from json import dump
from requests import get


API_URL = "https://jsonplaceholder.typicode.com"
"""The RESTAPI's URL"""


if __name__ == "__main__":
    empy_resp = get(f"{API_URL}/users").json()
    tsk_rep = get(f"{API_URL}/todos").json()
    empys_data = {}
    for empy in empy_resp:
        empy_id = empy.get("id")
        empy_name = empy.get("username")
        tasks = list(filter(lambda k: k.get("userId") == empy_id, tsk_rep))
        empy_data = list(
                map(lambda k: {"username": empy_name,
                               "task": k.get("title"),
                               "completed": k.get("completed")}, tasks)
        )
        empys_data[f"{empy_id}"] = empy_data
    with open("todo_all_employees.json", "w") as fl:
        dump(empys_data, fl)
