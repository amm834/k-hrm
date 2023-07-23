from django.urls import path
from hrm import views

from django.contrib.auth.decorators import login_required
from hrm.views import EmployeeCreateView

app_name = "hrm"
urlpatterns = [
    # employee
    path('employee_list/', login_required(views.EmployeeListView.as_view()), name="employee_list"),
    path('employee_detail/<employee_id>/', login_required(views.EmployeeDetailView.as_view()), name='employee_detail'),
    path('employee_create/', login_required(views.EmployeeCreateView.as_view()), name='employee_create'),
    path('employee_update/<employee_id>/', login_required(views.EmployeeUpdateView.as_view()), name='employee_update'),

    # identity
    path('employee_detail/<employee_id>/identity_create/', login_required(views.IdentityCreateView.as_view()), name='identity_create'),
    path('employee_detail/<employee_id>/identity_update/<identity_id>/', login_required(views.IdentityUpdateView.as_view()), name='identity_update'),

    # experience
    path('employee_detail/<employee_id>/experience_create/', login_required(views.ExperienceCreateView.as_view()), name='experience_create'),
    path('employee_detail/<employee_id>/experience_update/<experience_id>/', login_required(views.ExperienceUpdateView.as_view()), name='experience_update'),
    path('employee_detail/<employee_id>/experience_delete/<experience_id>/', login_required(views.ExperienceDeleteView.as_view()), name='experience_delete'),

    # qualification
    path('employee_detail/<employee_id>/qualification_create/', login_required(views.QualificationCreateView.as_view()), name='qualification_create'),
    path('employee_detail/<employee_id>/qualification_update/<qualification_id>/', login_required(views.QualificationUpdateView.as_view()), name='qualification_update'),
    path('employee_detail/<employee_id>/qualification_delete/<qualification_id>/', login_required(views.QualificationDeleteView.as_view()), name='qualification_delete'),
]