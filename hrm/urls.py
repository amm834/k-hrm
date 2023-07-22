from django.urls import path
from hrm import views

from django.contrib.auth.decorators import login_required

app_name = "hrm"
urlpatterns = [
    # employee
    path('employee_list/', login_required(views.EmployeeListView.as_view()), name="employee_list"),
    path('employee_detail/<employee_id>/', login_required(views.EmployeeDetailView.as_view()), name='employee_detail'),
    path('employee_update/<employee_id>/', login_required(views.EmployeeUpdateView.as_view()), name='employee_update'),

    # identity
    path('employee_detail/<employee_id>/identity_create/', login_required(views.IdentityCreateView.as_view()), name='identity_create'),
    path('employee_detail/<employee_id>/identity_update/<identity_id>/', login_required(views.IdentityUpdateView.as_view()), name='identity_update'),
]