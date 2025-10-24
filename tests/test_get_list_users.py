from core import endpoints
from models.list_users_model_response import AllObject, Meta,Support


def test_check_status_code(api_client):
    resp = api_client.get(f'{endpoints.GET_LIST_USERS}')

    assert resp.status_code == 200


def test_get_list_users(api_client):
    resp = api_client.get(f'{endpoints.GET_LIST_USERS}')

    #Разбираем JSON
    json_data = resp.json()

    #Кладем в модель правильные объекты из json_data
    model_resp_all_object = AllObject(**json_data)
    model_resp_meta = Meta(**json_data['_meta'])
    model_resp_support = Support(**json_data['support'])

    assert resp.status_code == 200
    assert model_resp_all_object.page == 2
    assert model_resp_meta.upgrade_url == 'https://app.reqres.in/upgrade'
    assert model_resp_support.url == 'https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral'
