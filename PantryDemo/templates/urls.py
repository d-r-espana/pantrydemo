from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome,  name='welcome'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]