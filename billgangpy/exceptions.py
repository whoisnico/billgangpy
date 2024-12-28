class ApiError(Exception):
    def __init__(self, response):
        try:
            self.message = response.json().get('message', 'Unknown Error')
        except ValueError:
            self.message = 'Invalid JSON response'
        self.status_code = response.status_code
        super().__init__(self.message)
