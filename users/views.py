from django.shortcuts import render
from .forms import RegisteringForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth import update_session_auth_hash

def user_register(request):
    if not request.user.is_active:
        form = RegisteringForm(data=request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            user.save()

            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, '<b>Registered successfully.</b>', extra_tags="success")
                    return HttpResponseRedirect(reverse('homepage'))
    else:
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'users/register.html', context={'form':form})

def user_login(request):
    if not request.user.is_active:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                loginMsg = "<b>Welcome {}!</b>".format(request.user.get_full_name())
                messages.success(request, loginMsg, extra_tags='success')
                return HttpResponseRedirect(reverse('homepage'))
    else:
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, 'users/login.html', context={'form': form})

def user_logout(request):
    username = request.user.username
    logout(request)
    msg = "<b> You logged out.</b>"
    messages.success(request, msg, extra_tags="danger")
    return HttpResponseRedirect(reverse('homepage'))