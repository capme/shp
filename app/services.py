from .models import TaxProductModel
from django.db import transaction


class TaxProductClass:
    def __init__(self):
        self.type_product = {
            1: {
                "Type": "Food & Beverage",
                "Refundable": "Yes"
            },
            2: {
                "Type": "Tobacco",
                "Refundable": "No"
            },
            3: {
                "Type": "Entertainment",
                "Refundable": "No"
            }
        }

    def calculate(self, payload):
        with transaction.atomic():
            # calculate each trx record
            res = {}
            res['price_subtotal'] = 0
            res['tax_subtotal'] = 0
            res['grand_total'] = 0
            
            if res:
                pass
            else:
                res = {}

            for item_key, item_payload in payload.items():
                res[item_key] = {}

                product_name = item_payload['product_name']
                tax_code = item_payload['tax_code']
                product_price = item_payload['product_price']

                # save to db
                rec = TaxProductModel.objects.create(
                    product_name=product_name,
                    tax_code=tax_code,
                    product_price=product_price,
                )

                # calculate tax value
                res_tax = 0

                if tax_code == 1:
                    # food and beverage product
                    res_tax = (10/100) * product_price

                elif tax_code == 2:
                    # tobacco product
                    res_tax = (2/100) * product_price

                elif tax_code == 3:
                    # entertainment product
                    if product_price >= 100:
                        res_tax = (1/100) * (product_price - 100)

                # composing return value
                res[item_key]['product_name'] = product_name
                res[item_key]['tax_code'] = tax_code
                res[item_key]['type'] = self.type_product[tax_code]['Type']
                res[item_key]['refundable'] = self.type_product[tax_code]['Refundable']
                res[item_key]['price'] = product_price
                res[item_key]['tax'] = res_tax
                res[item_key]['amount'] = res_tax + product_price

                # composing summary
                res['price_subtotal'] = res['price_subtotal'] + res[item_key]['amount']
                res['tax_subtotal'] = res['tax_subtotal'] + res_tax
                res['grand_total'] = res['grand_total'] + (res['price_subtotal'] + res['tax_subtotal'])

            return res

