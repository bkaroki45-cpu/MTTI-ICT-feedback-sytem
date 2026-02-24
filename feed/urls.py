
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('feedback/', views.feedback, name = 'feedback'),
    path('message/', views.message, name = 'message'),
    path('clubs/', views.clubs, name = 'clubs'),
    path('courses/', views.courses, name = 'courses'),
    path('contacts/', views.contacts, name = 'contacts'),
]
