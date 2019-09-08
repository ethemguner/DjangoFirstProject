from django.shortcuts import render
from .forms import RegisteringForm, LoginForm, UserSettingsForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from .models import Profile

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
            Profile.objects.create(user= user)
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

def user_settings(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse('homepage'))

    else:
        form = UserSettingsForm(data=request.POST or None, instance=request.user)

        if form.is_valid():
            adress = form.cleaned_data.get('adress', None)
            phone_number = form.cleaned_data.get('phone_number', None)
            #Information defined.

            request.user.profile.phone_number = phone_number
            request.user.profile.adress = adress
            #Information assignments

            request.user.profile.save()
            form.save()
            #Saved

            msg = "<b>Updated successfully.</b>"
            messages.success(request, msg, extra_tags="success")
            #Message has sent.

            return HttpResponseRedirect(reverse('user-settings'))

    return render(request, 'users/profile/settings.html', context={'form':form})

def password_change(request):
    form = PasswordChangeForm(user=request.user, data=request.POST or None)

    if form.is_valid():
        new_password = form.cleaned_data.get('new_password')
        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)
        messages.success(request, 'Password changed successfully.', extra_tags='success')
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'users/profile/password-change.html', context={'form':form})