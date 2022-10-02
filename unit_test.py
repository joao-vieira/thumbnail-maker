import unittest
from server import app

class RequestCase(unittest.TestCase):
    def test_request(self):
        base64const = "iVBORw0KGgoAAAANSUhEUgAAABIAAAAPCAIAAABm5AhFAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAA6SURBVDhPY/hPFhiS2hgYCIsAwcA6kkhADW1YfY8M4ArQteHSiSaFrggijRVAVYABdrMJAnpq%2B/8fAFBw9CiMWfoDAAAAAElFTkSuQmCC"

        response = app.test_client().post("/image", data = dict(image=base64const))
        #assert response.status_code == 200
        assert response.json == {"result":"success"}

if __name__ == '__main__':
    unittest.main()
