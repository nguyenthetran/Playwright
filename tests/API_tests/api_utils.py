import requests
from .config import BASE_URL, API_TOKEN

BASE_URL1 = "https://uat-api-seller.amaze-x.com/catalog/api/v2"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlMVQ3dGdFekw5ZnBkdkh2dTZ2eHJRa016YW9hMjBfSjhiYWpXd1oxbEo0In0.eyJleHAiOjE3NjE4OTc1MDcsImlhdCI6MTc2MTg3OTUwNywianRpIjoiMmE4ZmUzZDEtODFhNi00MmQ3LThkNWMtNjhiNDYzZmUyOWI3IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay51YXQtYXBpLXNlbGxlci5hbWF6ZS14LmNvbS9yZWFsbXMvYW1hemUtc2VsbGVyIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImM2MDcyZDVhLWNkMWQtNDVkNi1hNTg5LTFhOGUwMzUxZDczNiIsInR5cCI6IkJlYXJlciIsImF6cCI6InNlbGxlci1jbGllbnQiLCJzZXNzaW9uX3N0YXRlIjoiZjU3NWQzY2YtNzdkYy00NGIxLTliYTktYmZmODM0ZDE3ZjhiIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1hbWF6ZS1zZWxsZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBvZmZsaW5lX2FjY2VzcyBlbWFpbCIsInNpZCI6ImY1NzVkM2NmLTc3ZGMtNDRiMS05YmE5LWJmZjgzNGQxN2Y4YiIsInNob3BfaWQiOiIwY2FmMTQwZS0xNDNmLTRjMmItYTI2Mi1kYzMzODZlNjhlZjkiLCJ1c2VyX2FwcHJvdmVkIjoiZmFsc2UiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJ2b2YzcTJtbmNyY2VzbXogYTM2N3EwdHpxdHN2djBoIiwicGhvbmVfbnVtYmVyIjoiMDg0NjQ1NjEzNCIsInByZWZlcnJlZF91c2VybmFtZSI6InFjX3Rlc3RlciIsImdpdmVuX25hbWUiOiJ2b2YzcTJtbmNyY2VzbXoiLCJmYW1pbHlfbmFtZSI6ImEzNjdxMHR6cXRzdnYwaCIsInNob3BfYW1hemVfaWQiOiIyMjQ1NCIsImVtYWlsIjoicWMua2QudHJAZ21haWwuY29tIn0.BG_cLoSvto78YqzAClqblmDc51OjOit440eVQd74bOVvsn7f1NxJH7kWJkbZxY2H7Yzuni9U784kztY44nUCt9KHbOwtP0LkixANX6eGsrQV-NIL0IgBv-0jMCMpWAcF2wbXsVqgIi0MUaWRyq3IYLKwI4bX6PlERXxW3Klw00hqgofqouNRW6bfOtyMZ5oOhF__LgMfXnDYhduHqb4WvPUffqHFxWSXd1lQAWDW3_BQRkvo8IS5qeSWv83wA6xC1SnifYeBbuHqc6cBKej5LBfb4PddsgtXx2-DfmddibI7ZH2RicpBMAT0D1CEG-uGqtcPuXtx7jiDjQcZD5baAQ",
    "x-language-key": "en",
    "x-shop-id": "0caf140e-143f-4c2b-a262-dc3386e68ef9",
    "x-user-id": "c6072d5a-cd1d-45d6-a589-1a8e0351d736",
    "accept": "application/json, text/plain, */*"
}

def create_product(payload):
    url = f"{BASE_URL}/catalog/api/v3/product"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response

def get_product_list():
    url = f"{BASE_URL1}/catalog/api/v2/product?page=1&promotion_detail=true&size=48&normal_price_history=true&price_off_history=true&list_type=all"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlMVQ3dGdFekw5ZnBkdkh2dTZ2eHJRa016YW9hMjBfSjhiYWpXd1oxbEo0In0.eyJleHAiOjE3NjE4OTc1MDcsImlhdCI6MTc2MTg3OTUwNywianRpIjoiMmE4ZmUzZDEtODFhNi00MmQ3LThkNWMtNjhiNDYzZmUyOWI3IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay51YXQtYXBpLXNlbGxlci5hbWF6ZS14LmNvbS9yZWFsbXMvYW1hemUtc2VsbGVyIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImM2MDcyZDVhLWNkMWQtNDVkNi1hNTg5LTFhOGUwMzUxZDczNiIsInR5cCI6IkJlYXJlciIsImF6cCI6InNlbGxlci1jbGllbnQiLCJzZXNzaW9uX3N0YXRlIjoiZjU3NWQzY2YtNzdkYy00NGIxLTliYTktYmZmODM0ZDE3ZjhiIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1hbWF6ZS1zZWxsZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBvZmZsaW5lX2FjY2VzcyBlbWFpbCIsInNpZCI6ImY1NzVkM2NmLTc3ZGMtNDRiMS05YmE5LWJmZjgzNGQxN2Y4YiIsInNob3BfaWQiOiIwY2FmMTQwZS0xNDNmLTRjMmItYTI2Mi1kYzMzODZlNjhlZjkiLCJ1c2VyX2FwcHJvdmVkIjoiZmFsc2UiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJ2b2YzcTJtbmNyY2VzbXogYTM2N3EwdHpxdHN2djBoIiwicGhvbmVfbnVtYmVyIjoiMDg0NjQ1NjEzNCIsInByZWZlcnJlZF91c2VybmFtZSI6InFjX3Rlc3RlciIsImdpdmVuX25hbWUiOiJ2b2YzcTJtbmNyY2VzbXoiLCJmYW1pbHlfbmFtZSI6ImEzNjdxMHR6cXRzdnYwaCIsInNob3BfYW1hemVfaWQiOiIyMjQ1NCIsImVtYWlsIjoicWMua2QudHJAZ21haWwuY29tIn0.BG_cLoSvto78YqzAClqblmDc51OjOit440eVQd74bOVvsn7f1NxJH7kWJkbZxY2H7Yzuni9U784kztY44nUCt9KHbOwtP0LkixANX6eGsrQV-NIL0IgBv-0jMCMpWAcF2wbXsVqgIi0MUaWRyq3IYLKwI4bX6PlERXxW3Klw00hqgofqouNRW6bfOtyMZ5oOhF__LgMfXnDYhduHqb4WvPUffqHFxWSXd1lQAWDW3_BQRkvo8IS5qeSWv83wA6xC1SnifYeBbuHqc6cBKej5LBfb4PddsgtXx2-DfmddibI7ZH2RicpBMAT0D1CEG-uGqtcPuXtx7jiDjQcZD5baAQ",
        "x-language-key": "en",
        "x-shop-id": "0caf140e-143f-4c2b-a262-dc3386e68ef9",
        "x-user-id": "c6072d5a-cd1d-45d6-a589-1a8e0351d736",
    }
    return requests.get(url, headers=headers)

def get_product_by_id(product_id):
    """Return the full product response by ID."""
    for path in [f"/product/{product_id}", f"/product/detail/{product_id}"]:
        url = f"{BASE_URL1}{path}"
        resp = requests.get(url, headers=HEADERS)
        # 🌟 ĐO VÀ IN RA LOAD TIME
        load_time = resp.elapsed.total_seconds()
        
        print(f"➡️ Tried {url} -> {resp.status_code} in {load_time:.3f}s")

        if resp.status_code == 200:
            return resp

    return resp