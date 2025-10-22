from http.client import responses

from core.api_client import ApiClient
from core import endpoints


def test_get_users(api_client):
    resp = api_client.get(f'{endpoints.GET_SINGLE_USER}')
    assert resp.status_code == 200
    assert resp.json()['data']['email'] == 'janet.weaver@reqres.in'


def test_check_bad_request_create_user(api_client):
    request_body = {'name': 'Ilya'}
    res = api_client.post(f'{endpoints.USER_REGISTER}', json=request_body)

    assert res.status_code == 400

def test_create_user(api_client):
    request_body = {'name': 'Ilya','email': 'imat@gmail.com','password': 'qwerty'}
    res = api_client.post(f'{endpoints.USER_REGISTER}', json=request_body)

    assert res.status_code == 201
    assert res.json()['data']['name'] == 'Ilya'


def test_status_code_get_user(api_client):
    resp = api_client.get(f'{endpoints.GET_SINGLE_USER}')

    assert resp.status_code == 200
