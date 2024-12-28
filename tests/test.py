import unittest
from billgangpy.api import BillgangPY

class TestBillgangPY(unittest.TestCase):
    def setUp(self):
        self.billgang = BillgangPY(apikey='YOUR TOEKN')
    def test_get_user(self):
        response = self.billgang.get_user()
        print(response.email)
        self.assertIsNotNone(response.email)

if __name__ == '__main__':
    unittest.main()
