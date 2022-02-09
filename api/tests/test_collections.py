import json


class TestBardApi:
    def test_index(self, client):
        assert client.get('/').status_code == 200

    def test_created_collection(self, client):
        r = client.get('/collections')
        json_collections = r.json
        assert len(json_collections) == 0