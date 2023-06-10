from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def employee_list(request):
    return render(request, 'hrm/employee_list.html')