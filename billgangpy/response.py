class Shop:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.logo_image = data.get('logoImage')
        self.currency = data.get('currency')
        self.domain = data.get('domain')
        self.permissions = data.get('permissions', [])

class Subscription:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.expires_at = data.get('expiresAt')
        self.is_trial = data.get('isTrial')
        self.perks = data.get('perks', {})

class User:
    def __init__(self, data):
        self.id = data.get('id')
        self.email = data.get('email')
        self.is_email_verified = data.get('isEmailVerified')
        self.shops = [Shop(shop) for shop in data.get('shops', [])]
        self.subscription = Subscription(data.get('subscription', {}))
        self.is_tfa_enabled = data.get('isTfaEnabled')

class ApiResponse:
    def __init__(self, response):
        self.data = User(response.get('data', {}))
        self.message = response.get('message')
        self.errors = response.get('errors', [])
