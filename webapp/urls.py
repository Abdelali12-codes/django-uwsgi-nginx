from django.urls import path
from . import views


urlpatterns = [
    path('', views.app),
    path('app/', views.app),
    path('template/', views.template),
    path('login/',  views.login)
]

