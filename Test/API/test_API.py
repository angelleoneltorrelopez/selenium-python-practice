import requests


class Test_API:
    def test_get(self):
        payload = {"id": 2}
        request = requests.get("https://reqres.in/api/users/", params=payload)
        response_body = request.json()
        assert request.status_code == 200
        print(response_body["data"]["id"])
        assert response_body["data"]["id"] == 2

    def test_post(self):
        payload = {"id": 2, "name": "Angel", "job": "QA"}
        request = requests.post("https://reqres.in/api/users/", data=payload)
        response_body = request.json()
        assert request.status_code == 201
        print(response_body)
        assert response_body["name"] == "Angel"

    def test_put(self):
        payload = {"name": "Leonel", "job": "QM"}
        request = requests.put("https://reqres.in/api/users/2", data=payload)
        response_body = request.json()
        assert request.status_code == 200
        print(response_body)
        assert response_body["name"] == "Leonel"
        assert response_body["job"] == "QM"

    def test_delete(self):
        request = requests.delete("https://fakestoreapi.com/products/1")
        response_body = request.json()
        assert request.status_code == 200
        print(response_body)

    def test_login(self):
        payload = {"username": "mor_2314", "password": "83r5^_"}
        request = requests.post("https://fakestoreapi.com/auth/login", data=payload)
        response_body = request.json()
        assert request.status_code == 200
        print(response_body)
        assert "eyJhbGciOiJIUzI1NiIsInR" in response_body["token"]
