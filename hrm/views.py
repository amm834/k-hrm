from django.urls import reverse_lazy
from django.db.models import Q

from vanilla import ListView, DetailView, UpdateView

from hrm import models
from hrm import forms

class EmployeeListView(ListView):
    model = models.Employee
    form_class = forms.SearchForm
    paginate_by = 100

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            search_form = self.form_class(self.request.GET)
            employee_list = self.model.objects.filter(Q(user__is_active=True))
            if search_form.is_valid():
                employee_list = employee_list.filter(
                    Q(id__icontains=search_form.cleaned_data['search_query']) |
                    Q(name__icontains=search_form.cleaned_data['search_query']) |
                    Q(identity__nrc_no__icontains=search_form.cleaned_data['search_query']) |
                    Q(user__email__icontains=search_form.cleaned_data['search_query']) |
                    Q(phone__icontains=search_form.cleaned_data['search_query']) |
                    Q(position__name__icontains=search_form.cleaned_data['search_query']) |
                    Q(position__team__name__icontains=search_form.cleaned_data['search_query']) |
                    Q(position__team__department__name__icontains=search_form.cleaned_data['search_query'])
                )
        else:
            employee_list = self.model.objects.filter(Q(user__id__exact=self.request.user.id))
        return employee_list

    def get_paginate_by(self):
        try:
            return int(self.request.GET['page_size'] if 'page_size' in self.request.GET else self.paginate_by)
        except ValueError:
            return None

class EmployeeDetailView(DetailView):
    model = models.Employee
    lookup_field = 'id'

    def get_queryset(self):
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            return self.model.objects.filter(Q(user__id__exact=self.request.user.id))
        return self.model

class EmployeeUpdateView(UpdateView):
    model = models.Employee
    lookup_field = 'id'
    form_class = forms.EmployeeForm

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('hrm:employee_detail', kwargs={'id': self.object.id})

    def get_queryset(self):
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            return self.model.objects.filter(Q(user__id__exact=self.request.user.id))
        return self.model