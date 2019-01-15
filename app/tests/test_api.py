from django.test import TestCase
from ..models import TaxProductModel
import simplejson
import time


class TestApi(TestCase):
    def setUp(self):
        self.rec_id_news = None

    def test_calculate_product_tax(self):
        payload = {
            "1": {
                "product_name": "Lucky Stretch",
                "tax_code": 2,
                "product_price": 1000
            },
            "2": {
                "product_name": "Big Mac",
                "tax_code": 1,
                "product_price": 1000
            },
            "3": {
                "product_name": "Movie",
                "tax_code": 3,
                "product_price": 150
            }
        }
        resp = self.client.post('/api/calculate_product_tax',
                                simplejson.dumps(payload), content_type='application/json')
        # check the response code
        self.assertEqual(resp.status_code, 200)
        # check the db data
        rec = TaxProductModel.objects.filter(product_name="Lucky Stretch").first()
        self.assertIsNotNone(rec)
        self.assertEqual(rec.tax_code, 2)
        self.assertEqual(rec.product_price, 1000)
        # check the api response
        self.assertEqual(resp.data['1']['refundable'], "No")
        self.assertEqual(resp.data['1']['type'], "Tobacco")
        self.assertEqual(resp.data['1']['tax'], 20.0)
        self.assertEqual(resp.data['1']['amount'], 1020)
