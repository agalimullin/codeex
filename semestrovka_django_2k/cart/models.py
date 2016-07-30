from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

payment = (('in cash', 'in cash'),
           ('credit card', 'credit card'))

shipping = (('Russian POST', 'Russian POST'), ('SPSR', 'SPSR'))


class Cart(models.Model):
    class Meta:
        db_table = "cart"

    owner = models.ForeignKey(User)
    product = models.ForeignKey(Product, null=True, default=None)
    quantity = models.PositiveIntegerField(null=True, validators=[MinValueValidator(1)])


class Shipping(models.Model):
    shipping_method = models.CharField(max_length=50, choices=shipping, verbose_name="Shipping Method", blank=True,
                                       null=True)
    shipping_price = models.FloatField("Shipping Price", default=0.0)
    shipping_tax = models.FloatField("Shipping Tax", default=0.0)


class Payment(models.Model):
    payment_method = models.CharField(max_length=50, choices=payment, verbose_name="Payment Method", blank=True,
                                      null=True)
    payment_price = models.FloatField("Payment Price", default=0.0)
    payment_tax = models.FloatField("Payment Tax", default=0.0)


class CreditCard(models.Model):
    number = models.CharField("Number", blank=True, max_length=30)
    bank_name = models.CharField("Bank name", blank=True, max_length=100)
    expiration_date_month = models.IntegerField("Expiration date month", blank=True, null=True)
    expiration_date_year = models.IntegerField("Expiration date year", blank=True, null=True)


class Address(models.Model):
    firstname = models.CharField("Firstname", max_length=50, blank=False)
    lastname = models.CharField("Lastname", max_length=50, blank=False)
    zip_code = models.CharField("Zip code", max_length=10, blank=False)
    city = models.CharField("City", max_length=50, blank=False)
    state = models.CharField("State", max_length=50, blank=True, null=True)
    country = models.CharField("Country", max_length=30, blank=True, null=True)
