# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-15 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaxProductModel',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('tax_code', models.PositiveSmallIntegerField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=255)),
            ],
        ),
    ]
