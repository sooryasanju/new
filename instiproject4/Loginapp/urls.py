from django.urls import path

from Loginapp import views

urlpatterns = [
    path('',views.login,name='login'),
]
