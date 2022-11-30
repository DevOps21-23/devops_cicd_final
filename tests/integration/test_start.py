import requests
def test_start(config):
 response = requests.get(config.base_url, timeout=config.TIMEOUT)
 assert response.headers['content-type'] == 'text/html; charset=utf-8'
 assert "Welcome to the shop" in response.text
 assert response.status_code == 200