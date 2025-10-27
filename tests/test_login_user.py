from core import endpoints

request_model = {'email': 'eve.holt@reqres.in',
                 'password': 'cityslicka'}


def test_check_status_code_login_request(api_client):
    resp = api_client.post(f'{endpoints.LOGIN}', json=request_model)

    assert resp.status_code == 200


def test_check_token_login_request(api_client):
    resp = api_client.post(f'{endpoints.LOGIN}', json=request_model)
    assert resp.json()['token'] == 'QpwL5tke4Pnpja7X4'


def test_login_user_without_body(api_client):
    resp = api_client.post(f'{endpoints.LOGIN}')

    assert resp.status_code == 400
    assert resp.json() == {"error": "Missing email or username"}
