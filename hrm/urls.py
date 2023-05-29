from django.urls import path

from hrm import views

app_name = "hrm"
urlpatterns = [
    path('profile/', views.profile, name='profile')
]