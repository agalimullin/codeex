from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf

from catalog.models import Product, Category
from client.models import UserProfile
from goldenshop.forms import ReviewForm
from goldenshop.models import *


def index(request, page_number=1):
    all_products = Product.objects.all()
    current_page = Paginator(all_products, 9)
    args = {'products': current_page.page(page_number),
            'categories': Category.objects.all(),
            'newest_products': Product.objects.all().order_by('-release_date')[:4],
            'cheap_products': Product.objects.all().order_by('product_cost')[:6]}
    username = request.user.id
    if username is not None:
        args['username'] = auth.get_user(request).username
    return render_to_response('catalog.html', args)


def review(request):
    profile = UserProfile.objects.get(user=request.user)
    review_form = ReviewForm
    args = {'reviews': Review.objects.all(),
            'form': review_form,
            'profile': profile}
    args.update(csrf(request))
    return render_to_response('Reviews.html', args)


def about(request):
    return render_to_response('About.html')


def contact(request):
    return render_to_response('Contact.html')


def add_review(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.review_author = User.objects.get(id=request.user.id)
        form.save()
        request.session.set_expiry(30)
        # request.session['pause'] = True
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
