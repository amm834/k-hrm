from vanilla import ListView, DetailView

from hrm import models

class EmployeeListView(ListView):
    model = models.Employee
    template_name = 'hrm/employee_list.html'
    paginate_by = 100

    def get_paginate_by(self):
        try:
            return int(self.request.GET['page_size'] if 'page_size' in self.request.GET else self.paginate_by)
        except ValueError:
            return None


# @login_required
# def employee_list(request):
#     context = {}

#     employee_list = models.Employee.objects.all()
#     paginated_employee_list = Paginator(employee_list, 100)

#     page_number = request.GET.get("page")
#     context['employees'] = paginated_employee_list.get_page(page_number)

#     return render(request, 'hrm/employee_list.html', context)