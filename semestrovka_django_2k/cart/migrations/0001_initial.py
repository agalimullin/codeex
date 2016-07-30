# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=50, verbose_name=b'Firstname')),
                ('lastname', models.CharField(max_length=50, verbose_name=b'Lastname')),
                ('zip_code', models.CharField(max_length=10, verbose_name=b'Zip code')),
                ('city', models.CharField(max_length=50, verbose_name=b'City')),
                ('state', models.CharField(max_length=50, null=True, verbose_name=b'State', blank=True)),
                ('country', models.CharField(max_length=30, null=True, verbose_name=b'Country', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(default=None, to='catalog.Product', null=True)),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=30, verbose_name=b'Number', blank=True)),
                ('bank_name', models.CharField(max_length=100, verbose_name=b'Bank name', blank=True)),
                ('expiration_date_month', models.IntegerField(null=True, verbose_name=b'Expiration date month', blank=True)),
                ('expiration_date_year', models.IntegerField(null=True, verbose_name=b'Expiration date year', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Payment Method', choices=[(b'in cash', b'in cash'), (b'credit card', b'credit card')])),
                ('payment_price', models.FloatField(default=0.0, verbose_name=b'Payment Price')),
                ('payment_tax', models.FloatField(default=0.0, verbose_name=b'Payment Tax')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shipping_method', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Shipping Method', choices=[(b'Russian POST', b'Russian POST'), (b'SPSR', b'SPSR')])),
                ('shipping_price', models.FloatField(default=0.0, verbose_name=b'Shipping Price')),
                ('shipping_tax', models.FloatField(default=0.0, verbose_name=b'Shipping Tax')),
            ],
        ),
    ]
