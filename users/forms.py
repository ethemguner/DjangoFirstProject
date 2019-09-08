from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import re
from django.db import models
from .models import Profile


class RegisteringForm(forms.ModelForm):
    password = forms.CharField(min_length=6, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               help_text="Must be at least 6 character.")
    password_confirm = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                       help_text="Must be at least 6 character.")

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirm', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(RegisteringForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            self.add_error('password', "Passwords doesn't match.")
            self.add_error('password_confirm', "Passwords doesn't match.")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This e-mail is already exist.')
        return email

    def clean_username(self):
        user = self.cleaned_data.get('username')

        if User.objects.filter(email=user).exists():
            raise forms.ValidationError('This username is already exist.')
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Username or e-mail:', required=True, max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'your username or e-mail'}))

    password = forms.CharField(label='Password:', required=True, max_length=50,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'your password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError('Wrong password or username/e-mail!')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if re.match(r"[^@]+@[^@]+\.[^@]+", username):
            users = User.objects.filter(email__iexact=username)
            print(users)
            if len(users) > 0 and len(users) == 1:
                return users.first().username
        return username


class UserSettingsForm(forms.ModelForm):
    adress = forms.CharField(widget=forms.Textarea, required=True)
    phone_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['adress', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(UserSettingsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['adress'].widget.attrs = {'class': 'form-control', 'placeholder':'your full adress'}
            self.fields['phone_number'].widget.attrs = {'class': 'form-control', 'placeholder': '5xxxxxxxxx'}

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number', None)
        try:
            int(phone_number)
            if len(phone_number) != 10:
                raise forms.ValidationError("Phone number's length must be 10 characters.")
        except ValueError:
            raise forms.ValidationError("This isn't a phone number.")
        return phone_number

class PasswordChangeForm(forms.Form):
    user = None
    old_password =forms.CharField(min_length=6, required=True, label='Current password:',
                                  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password = forms.CharField(min_length=6, required=True, label='New Password:',
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password_confirm = forms.CharField(min_length=6, required=True, label='New Password Confirm:',
                                           widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

    def clean(self):
        new_password = self.cleaned_data.get('new_password')
        new_password_confirm = self.cleaned_data.get('new_password_confirm')

        if new_password != new_password_confirm:
            self.add_error('new_password', "Password doesn't match.")
            self.add_error('new_password_confirm', "Password doesn't match.")

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')

        if not self.user.check_password(old_password):
            raise forms.ValidationError("Current password wrong.")

        return old_password