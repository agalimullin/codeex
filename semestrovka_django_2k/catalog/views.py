# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy

from catalog.models import *
from cart.models import *
from client.models import *
from django.shortcuts import *
from django.contrib import auth
from django.core.context_processors import csrf
from cart.forms import CartForm
from catalog.forms import CommentForm


def one_category(request, id):
    args = {'category': Category.objects.filter(id=id), 'products': Product.objects.filter(product_category=id),
            'categories': Category.objects.all()}
    print(Category.objects.filter(id=id))
    username = request.user.id
    if username is not None:
        args['username'] = auth.get_user(request).username
    return render_to_response('catalog.html', args)


def product(request, id):
    username = request.user.id
    comment_form = CommentForm
    cart_form = CartForm
    args = {'comments': Comment.objects.filter(comment_product_id=id),
            'form': comment_form,
            'cart_add_form': cart_form,
            'product': Product.objects.get(id=id),
            'categories': Category.objects.all(),
            'other_products': Product.objects.exclude(id=id).order_by('product_category')[:5],
            }
    args.update(csrf(request))
    if username is not None:
        args['username'] = auth.get_user(request).username
    return render_to_response('product.html', args)


# ПОДПРАВИТЬ
@login_required(login_url=reverse_lazy("login"))
def add_like_product(request, id):
    username = auth.get_user(request).username
    q = username + "_" + id
    try:
        product_id = id
        x = Product.objects.get(id=product_id)
        if q in request.COOKIES:
            f = Product.objects.get(id=product_id)
            return HttpResponse(f.likes)
        else:
            f = Product.objects.get(id=product_id)
            http_response = HttpResponse(f.likes)
            http_response.set_cookie(q, "likes product %s" % product_id)
            f = Product.objects.get(id=product_id)
            f.likes += 1
            f.save()
            # response = redirect('/product/%s/' % x.id)
            # response.set_cookie(q, "likes product %s" % product_id)
            return HttpResponse(f.likes)
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/product/%s/' % x.id)


def add_comment(request, id):
    product_id = id
    if request.POST and ('pause' not in request.session):
        c = Comment()
        c.comment_product = Product.objects.get(id=product_id)
        c.comment_author = User.objects.get(id=request.user.id)
        c.comment_text = request.POST['comment']
        c.save()
        # form = CommentForm(request.POST)
        # if form.is_valid():
        #     comment = form.save(commit=False)
        #     comment.comment_product = Product.objects.get(id=product_id)
        #     comment.comment_author = User.objects.get(id=request.user.id)
        #     form.save()
        #     request.session.set_expiry(30)
            # request.session['pause'] = True
    return redirect('/product/%s/' % product_id)


def del_comment(request, id):
    Comment.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def search(request):
    args = {}
    if ('search' in request.GET) and (request.GET['search']):
        s = request.GET['search']
        result = Product.objects.filter(product_title__contains=s)
        args['products'] = result
        args['categories'] = Category.objects.all()
        return render_to_response('catalog.html', args)
    else:
        args['search'] = 'Nothing found'
        args['categories'] = Category.objects.all()
        return render_to_response('catalog.html', args)
