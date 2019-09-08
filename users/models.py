from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=False, verbose_name="User", on_delete=models.CASCADE)
    adress = models.TextField(max_length=1000, verbose_name='Adress:', blank=True, null=True,
                              help_text="Your shipping adress.")
    phone_number = models.CharField(max_length=10, verbose_name='Phone Number', blank=True, null=True,
                                    help_text="Notifications will send to your phone number.")

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username

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
        return reverse('#', kwargs={'username': self.user.username})