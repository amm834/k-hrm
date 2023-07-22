from django.http import Http404
from django.urls import reverse_lazy
from django.db.models import Q

from vanilla import ListView, CreateView, DetailView, UpdateView

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
    lookup_url_kwarg = 'employee_id'

    def get_queryset(self):
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            return self.model.objects.filter(Q(user__id__exact=self.request.user.id))
        return self.model

class EmployeeCreateView(CreateView):
    model = models.Employee
    form_class = forms.EmployeeForm

    def get_success_url(self):
        return reverse_lazy('hrm:employee_detail', kwargs={'employee_id': self.object.id})

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class EmployeeUpdateView(UpdateView):
    model = models.Employee
    lookup_url_kwarg = 'employee_id'
    form_class = forms.EmployeeForm

    def get_success_url(self):
        return reverse_lazy('hrm:employee_detail', kwargs={'employee_id': self.object.id})

    def get_queryset(self):
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            return self.model.objects.filter(Q(user__id__exact=self.request.user.id))
        return self.model

class IdentityCreateView(CreateView):
    model = models.Identity
    form_class = forms.IdentityForm

    def get_success_url(self):
        return reverse_lazy('hrm:employee_detail', kwargs={'employee_id': self.object.employee.id})

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class IdentityUpdateView(UpdateView):
    model = models.Identity
    lookup_url_kwarg = 'identity_id'
    form_class = forms.IdentityForm

    def get_success_url(self):
        return reverse_lazy('hrm:employee_detail', kwargs={'employee_id': self.object.employee.id})

    def get_queryset(self):
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            return self.model.objects.filter(Q(employee__id__exact=self.request.user.employee.id))
        return self.model