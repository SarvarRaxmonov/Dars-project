
from django.urls import path
from . import views
from .views import PostListView
urlpatterns = [
     path('home/',views.home, name='home'),
     path('register/',views.RegisterPage, name='register'),
     path('login/',views.LoginPage, name='login'),
     path('profile/', views.Profile, name='profile'),
     path('logout/', views.logoutUser, name='logout') ,
     path('', PostListView.as_view(), name='postlist')
]  

