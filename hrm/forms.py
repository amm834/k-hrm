from django import forms

from hrm import models
class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = '__all__'

class TeamForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = '__all__'

class PositionForm(forms.ModelForm):
    class Meta:
        model = models.Position
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = '__all__'

class IdentityForm(forms.ModelForm):
    class Meta:
        model = models.Identity
        fields = '__all__'

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = models.Experience
        fields = '__all__'

class QualificationForm(forms.ModelForm):
    class Meta:
        model = models.Qualification
        fields = '__all__'

class EmploymentForm(forms.ModelForm):
    class Meta:
        model = models.Employment
        fields = '__all__'