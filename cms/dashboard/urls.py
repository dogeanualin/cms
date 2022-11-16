
from django.urls import path
from .views import Home,UserLogin
urlpatterns = [
    path('',Home.as_view(),name='home' ),
    path('login/',UserLogin.as_view(),name='login' ),
]
