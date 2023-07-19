from django.urls import path
from hrm import views

from django.contrib.auth.decorators import login_required

app_name = "hrm"
urlpatterns = [
    path('employee_list', login_required(views.EmployeeListView.as_view()), name="employee_list"),
    path('employee_detail/<id>', login_required(views.EmployeeDetailView.as_view()), name='employee_detail'),
]