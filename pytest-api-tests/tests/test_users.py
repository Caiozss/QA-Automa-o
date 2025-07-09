import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_by_id():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "Bret"

def test_create_post():
    payload = {
        "userId": 1,
        "title": "Novo post de teste",
        "body": "Conteúdo do post"
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    result = response.json()
    assert result["title"] == payload["title"]
