
from faker import Faker
fake = Faker()
from modules.list_methods import create_goal, get_goal
from modules.list_methods import body
from modules.list_methods import delete_goal
from modules.list_methods import get_goals
from modules.list_methods import update_goal


def test_get_goal():
    response = create_goal()
    my_name = response.json()['goal']['name']
    my_id = response.json()['goal']['id']

    get_response = get_goal(my_id)
    assert get_response.json()['goal']['name'] == my_name

    delete_goal(my_id)



def test_get_goals():
    response = create_goal()
    my_id1 = response.json()['goal']['id']


    response = create_goal()
    my_id2 = response.json()['goal']['id']


    result = get_goals()
    assert result.json()['goals'][0]['id'] == my_id1 and result.json()['goals'][1]['id'] == my_id2


    delete_goal(my_id1)
    delete_goal(my_id2)



def test_create_goal():
    response = create_goal()
    assert response.json()['goal']['name'] == body['name']

    my_id = response.json()['goal']['id']
    delete_goal(my_id)


def test_update_goal():
    body_upd = {"name": fake.name()}
    response = create_goal()
    my_id = response.json()['goal']['id']
    my_name = response.json()['goal']['name']

    update_body = update_goal(my_id, body_upd)
    assert update_body.json()['goal']['name'] != my_name

    delete_goal(my_id)


def test_delete_goal():
    response = create_goal()
    my_id = response.json()['goal']['id']
    del_response = delete_goal(my_id)
    assert del_response.status_code == 200

