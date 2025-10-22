import requests

base_headers = {"x-api-key": "reqres-free-v1",
                "Accept": "application/json"}


# Тест проверки вызова метода api
def test_request():
    response = requests.get("https://reqres.in/api/users/2", headers=base_headers)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["email"] == "janet.weaver@reqres.in"
