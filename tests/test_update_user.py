from core import endpoints


def test_check_status_code_update_user_request(api_client):
    resp = api_client.put(f'{endpoints.GET_SINGLE_USER}')

    assert resp.status_code == 200
