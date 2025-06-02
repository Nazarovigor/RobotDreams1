import requests
from faker import Faker
import os
import ast
from dotenv import load_dotenv

load_dotenv()
fake = Faker()


headers = ast.literal_eval(os.getenv("headers"))
base_url = os.getenv('base_url')

body = {"name": fake.name()}


def create_goal():

    return requests.post(base_url + "team/90131546371/goal", json=body, headers=headers)

def get_goals():

    return requests.get(base_url + "team/90131546371/goal", headers=headers)

def get_goal(id):

    return  requests.get(base_url + "goal/" + str(id), headers=headers)

def delete_goal(id):

    return requests.delete(base_url + "goal/" + str(id), headers=headers)


def update_goal(id, body):

    return requests.put('https://api.clickup.com/api/v2/goal/' + str(id), json=body, headers=headers)