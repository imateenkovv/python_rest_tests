from core import endpoints
from models.single_user_model_response import get_user_response


def test_get_single_users(api_client):
    resp = api_client.get(f'{endpoints.GET_SINGLE_USER}')
    resp_model = get_user_response(**resp.json())

    assert resp.status_code == 200
    assert resp_model.data.email.endswith("@reqres.in")
    assert resp_model.data.first_name == "Janet"
    assert resp_model.data.id == 2


def test_status_code_get_single_user(api_client):
    resp = api_client.get(f'{endpoints.GET_SINGLE_USER}')

    assert resp.status_code == 200