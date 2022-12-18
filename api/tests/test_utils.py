from django.test import TestCase
from api.utils import Sum

class UtilsTestCase(TestCase):

    def test_sum(self):
        params = {
            "val_1": 3,
            "val_2": 2,
        }
        result = Sum(params).call().get("result")
        self.assertEqual(result, 5)
