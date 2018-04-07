from django.urls import path
from Pak_Political_Trends import views

app_name = 'Pak_Political_Trends'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('trends_form/', views.trends_form, name='trends_form'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_login/index', views.index, name='index'),
]

