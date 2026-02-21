
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('see/', views.see, name = 'see'),
    path('message/', views.message, name = 'message'),
]
