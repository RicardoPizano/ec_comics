from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_search_comics():
    response = client.get("/searchComics")
    response_json = response.json()
    assert len(response_json["characters"]) > 0
    assert len(response_json["comics"]) == 0
    response = client.get("/searchComics?query=Ant-Man")
    response_json = response.json()
    assert len(response_json["characters"]) == 3
    assert len(response_json["comics"]) == 20
    response = client.get("/searchComics?query=Ant-Man&search_by_type=characters")
    response_json = response.json()
    assert len(response_json["characters"]) == 3
    assert len(response_json["comics"]) == 0
    response = client.get("/searchComics?query=Ant-Man&limit=1")
    response_json = response.json()
    assert len(response_json["characters"]) == 1
    assert len(response_json["comics"]) == 1
