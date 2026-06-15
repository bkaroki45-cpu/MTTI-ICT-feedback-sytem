from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("departments/", views.departments, name="departments"),
    path("departments/<slug:slug>/", views.department_detail, name="department_detail"),
    path("departments/<slug:department_slug>/feedback/", views.feedback, name="department_feedback"),
    path("feedback/", views.feedback, name="feedback"),
    path("message/", views.message, name="message"),
    path("events/", views.events, name="events"),
    path("events/<int:pk>/", views.event_detail, name="event_detail"),
    path("institutional-dashboard/", views.institutional_dashboard, name="institutional_dashboard"),
]
