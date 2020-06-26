
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.Home, name="Home" ),
    path('login',views.login,name="login"),
    path('client_login',views.client_login,name="client_login"),
    path('client_registration',views.client_registration,name="client_registration"),
    path('save_client',views.save_client,name="save_client"),
    path('client_login_check',views.client_login_check,name="client_login_check"),
    path('client_profile',views.client_profile,name="client_profile"),
    path('client_update',views.client_update,name="client_update"),
    path('logout',views.logout,name="logout"),
    path('save_client_update',views.save_client_update,name="save_client_update"),


]
