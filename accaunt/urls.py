from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accaunt'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('sign_in/', views.UserLoginView.as_view(), name='sign_in'),
    path('sign_up/', views.UserRegisterView.as_view(), name='sign_up'),

]
