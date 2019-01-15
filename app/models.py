from django.db import models


class TaxProductModel(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    product_name = models.CharField(max_length=255, null=False)
    tax_code = models.PositiveSmallIntegerField()
    product_price = models.DecimalField(max_digits=255, decimal_places=2)
