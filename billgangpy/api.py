import requests
from .exceptions import ApiError
from .response import ApiResponse

class BillgangPY:
    def __init__(self, apikey, baseurl="https://pg-api.billgang.com/v1/"):
        self.api_key = apikey
        self.base_url = baseurl
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _get(self, endpoint, params=None):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url, headers=self.headers, params=params)
        
        # Protokolliere die Antwort
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        
        self._handle_response(response)
        
        # Wenn die Antwort erfolgreich ist, geben wir sie zurück
        return response.json() if response.status_code == 200 else {}

    def _handle_response(self, response):
        # Überprüfen, ob die Antwort erfolgreich ist (Statuscode 2xx)
        if not response.ok:
            raise ApiError(f"Error: {response.status_code} - {response.text}")

        # Versuchen, die Antwort als JSON zu parsen
        try:
            response_json = response.json()
        except ValueError:
            raise ApiError(f"Invalid JSON response: {response.text}")

    def get_user(self):
        endpoint = 'dash/user'
        response = self._get(endpoint)
        return ApiResponse(response).data
