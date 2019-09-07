from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from phone_field import PhoneField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=False,verbose_name="User",on_delete=models.CASCADE)
    adress = models.TextField(max_length=1000, verbose_name='Adress:', blank=True, null=True)
    phone_number = PhoneField(blank=False, null=True, verbose_name='Phone Number:')

    class Meta:
        verbose_name_plural = "Profiles"

    def get_username(self):
        user = self.user
        if user.get_full_name():
            return user.username

    def get_full_name(self):
        user = self.user
        if self.user.get_full_name():
            return self.user.get_full_name()
        return None

    def get_user_url(self):
        return reverse('#', kwargs={'username':self.user.username})