from catalog.models import *
from cart.models import *
from client.models import User
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from cart.forms import CartForm, OrderForm


def add_to_cart(request, id):
    product_id = id
    if request.POST:
        username = request.user.id
        if username is not None:
            form = CartForm(request.POST)
            if form.is_valid():
                cart = form.save(commit=False)
                cart.owner = User.objects.get(id=request.user.id)
                cart.product = Product.objects.get(id=id)
                form.save()
                return redirect('/cart')
    return redirect('/product/%s/' % product_id)


def cart(request):
    username = request.user.id
    args = {'categories': Category.objects.all()}
    if username is not None:
        args['username'] = auth.get_user(request).username
        args['email'] = OrderForm
        args.update(csrf(request))
        args['cart'] = Cart.objects.filter(owner=username).raw(
            'SELECT cart.id,product_title, products.product_cost AS cost,quantity*products.product_cost '
            'AS price,quantity,product_id FROM cart, products WHERE cart.product_id=products.id ')
        return render_to_response('cart.html', args)
    else:
        return redirect('/auth/login/')


def order(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            for object in Cart.objects.all():
                object.delete()
            return redirect('/')
        else:
            return redirect('/cart/')


def del_from_cart(request, id):
    Cart.objects.get(id=id).delete()
    return redirect('/cart/')

