from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accaunt'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('sign_in/', views.UserLoginView.as_view(), name='sign_in'),
    path('sign_up/', views.UserRegisterView.as_view(), name='sign_up'),
    path('logout/', LogoutView.as_view(next_page="/sign_in/"), name='logout'),
    path('settings/', views.UserSettingView.as_view(), name='settings'),
    path('profiles/', views.ListUserView.as_view(), name='profiles'),
    path('follow/', views.user_follow, name='user_follow'),
    path('user_detail/<slug:slug>/', views.UserProfileView.as_view(), name='user_profile'),
    path('create_post/', views.PostCreateView.as_view(), name='post_create')
]
