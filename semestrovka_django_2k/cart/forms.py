from django.forms import ModelForm

from cart.models import *
from catalog.models import Comment
from client.models import UserProfile


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class OrderForm(ModelForm):
    class Meta:
        model = UserProfile
        # Shipping, Payment, CreditCard, Address
        fields = ['email']
        #  'shipping_method', 'shipping_price',
        # 'shipping_tax', 'payment_method', 'payment_price', 'payment_tax',
        # 'number', 'bank_name', 'expiration_date_month', 'expiration_date_year',
        # 'firstname', 'lastname', 'zip_code', 'city', 'state', 'country']
