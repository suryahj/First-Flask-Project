from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Indian States Blog" in response.data

def test_state_page():
    client = app.test_client()
    response = client.get("/state/karnataka")
    assert response.status_code == 200
    assert b"Karnataka" in response.data

def test_state_not_found():
    client = app.test_client()
    response = client.get("/state/unknownstate")
    assert response.status_code == 404