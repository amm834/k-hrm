from django.db.models import Q

from vanilla import ListView, DetailView

from hrm import models
from hrm.forms import SearchForm

class EmployeeListView(ListView):
    model = models.Employee
    form_class = SearchForm
    template_name = 'hrm/employee_list.html'
    paginate_by = 100

    def get_queryset(self):
        search_form = self.form_class(self.request.GET)
        employee_list = self.model.objects.filter(Q(user__is_active=True))
        if search_form.is_valid():
            employee_list = employee_list.filter(Q(id__icontains=search_form.cleaned_data['search_query']) | Q(name__icontains=search_form.cleaned_data['search_query']) | Q(user__email__icontains=search_form.cleaned_data['search_query']) | Q(phone__icontains=search_form.cleaned_data['search_query']) | Q(position__name__icontains=search_form.cleaned_data['search_query']) | Q(position__team__name__icontains=search_form.cleaned_data['search_query']) | Q(position__team__department__name__icontains=search_form.cleaned_data['search_query']))
        return employee_list

    def get_paginate_by(self):
        try:
            return int(self.request.GET['page_size'] if 'page_size' in self.request.GET else self.paginate_by)
        except ValueError:
            return None

class EmployeeDetailView(DetailView):
    model = models.Employee
    lookup_field = 'id'
    template_name = 'hrm/employee_detail.html'

# @login_required
# def employee_list(request):
#     context = {}

#     employee_list = models.Employee.objects.all()
#     paginated_employee_list = Paginator(employee_list, 100)

#     page_number = request.GET.get("page")
#     context['employees'] = paginated_employee_list.get_page(page_number)

#     return render(request, 'hrm/employee_list.html', context)