from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect as redirect
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import auth

from cart.models import Cart
from client.forms import ChangeImage
from client.models import UserProfile


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['visit'] = True
            return redirect('/')
        else:
            args['login_error'] = "User does not exist"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth_logout(request)
    return redirect(reverse('login'))


def registration(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            request.session['visit'] = True
            cart = Cart()
            cart.owner = newuser
            cart.save()
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('registration.html', args)


@login_required(login_url=reverse_lazy("login"))
def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    form = ChangeImage(request.POST)
    args = {'form': form,
            'profile': profile}
    args.update(csrf(request))
    return render_to_response("user_profile.html", args)


def refresh_image(request):
    if request.method == 'POST':
        form = ChangeImage(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            profile = UserProfile.objects.get(user=request.user)
            profile.avatar = form.cleaned_data['avatar']
            profile.save()
        # request.session['pause'] = True
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
