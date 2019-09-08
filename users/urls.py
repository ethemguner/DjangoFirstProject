from django.urls import path
from users.views import user_register, user_login, user_logout, user_settings, password_change

urlpatterns = [
    path('register/', user_register, name='user-register'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('settings/', user_settings, name='user-settings'),
    path('password-change/', password_change, name='password-change'),
]
