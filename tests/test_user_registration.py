from core import endpoints

request_body = {
    'email': 'eve.holt@reqres.in',
    'password': 'pistol'
}


def test_check_status_code(api_client):
    resp = api_client.post(f'{endpoints.USER_REGISTER}',
                           json=request_body)

    assert resp.status_code == 200


def test_check_response(api_client):
    resp = api_client.post(f'{endpoints.USER_REGISTER}',
                           json=request_body)

    assert resp.json() == {
        'id': 4,
        'token': 'QpwL5tke4Pnpja7X4'
    }
