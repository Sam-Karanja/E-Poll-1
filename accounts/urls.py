from django.urls import path, re_path
from . import views

app_name="accounts"

urlpatterns = [
    path('login/', views.account_login, name="accounts_login"),
    path('register/', views.account_register, name="accounts_register"),
    path('logout/', views.account_logout, name="account_logout"),
]
