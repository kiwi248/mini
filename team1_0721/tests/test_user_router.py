import pytest
from fastapi.testclient import TestClient

from app.jso import app
from app.services.user_service import reset_users


client = TestClient(app)
USER = {
    "username": "장상옥",
    "email": "sangok@example.com",
    "password": "1234",
    "bio": "FastAPI를 공부하고 있습니다.",
}


@pytest.fixture(autouse=True)
def clear_fake_db():
    reset_users()
    yield
    reset_users()


def test_create_user_hides_password():
    response = client.post("/users", json=USER)

    assert response.status_code == 201
    assert response.json() == {
        "user_id": 1,
        "username": "장상옥",
        "email": "sangok@example.com",
        "bio": "FastAPI를 공부하고 있습니다.",
    }
    assert "password" not in response.json()


def test_get_all_and_get_one():
    client.post("/users", json=USER)

    assert client.get("/users").json()[0]["user_id"] == 1
    assert client.get("/users/1").json()["username"] == "장상옥"


def test_update_user():
    client.post("/users", json=USER)
    updated = {
        "username": "장상옥",
        "email": "new@example.com",
        "password": "5678",
        "bio": "수정된 소개",
    }

    response = client.put("/users/1", json=updated)

    assert response.status_code == 200
    assert response.json()["email"] == "new@example.com"
    assert "password" not in response.json()


def test_delete_user():
    client.post("/users", json=USER)

    response = client.delete("/users/1")

    assert response.status_code == 200
    assert response.json() == {"message": "삭제하였습니다.", "id": 1}
    assert client.get("/users/1").status_code == 404


@pytest.mark.parametrize("method", ["get", "put", "delete"])
def test_missing_user_returns_404(method):
    if method == "put":
        response = client.put("/users/999", json=USER)
    else:
        response = getattr(client, method)("/users/999")
    assert response.status_code == 404


def test_required_field_validation_returns_422():
    response = client.post(
        "/users",
        json={"username": "장상옥", "email": "sangok@example.com"},
    )
    assert response.status_code == 422


def test_health_check():
    assert client.get("/health").json() == {"status": "ok"}
