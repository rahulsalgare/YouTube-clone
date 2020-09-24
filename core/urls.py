from django.urls import path,include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = "core"

urlpatterns = [
    path('',HomeView.as_view(), name='homeview'),
    path('profile/<slug:nm>', profile,name='profile'),
    path('videoupload/',VideoUploadView.as_view(), name='videoupload'),
    path('video/<int:id>', VideoView.as_view(),name='videoview'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('register',register, name='register'),
    path('likevideo/', likevideo, name='likevideo'),
    path('countview/', countview, name='countview'),
    path('unlikevideo',unlikevideo,name='unlikevideo'),
]
