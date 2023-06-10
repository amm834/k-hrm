from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from hrm import models

@login_required
def employee_list(request):
    context = {}

    employee_list = models.Employee.objects.all()
    paginated_employee_list = Paginator(employee_list, 1)

    page_number = request.GET.get("page")
    context['employees'] = paginated_employee_list.get_page(page_number)

    return render(request, 'hrm/employee_list.html', context)