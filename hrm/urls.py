from django.urls import path
from hrm import views

app_name = "hrm"
urlpatterns = [
    path('employees', views.employee_list, name="employee_list")
]