from django.conf import settings
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    name = models.CharField(max_length=50)
    rate = models.IntegerField()
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=(
        ('male', 'Male'),
        ('female', 'Female'),
    ))
    dob = models.DateField()
    distinct_mark = models.CharField(blank=True, null=True, max_length=50)

    father = models.CharField(blank=True, null=True, max_length=50)
    mother = models.CharField(blank=True, null=True, max_length=50)

    phone = models.IntegerField()
    exact_address = models.TextField(blank=True, null=True)

    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)

    remark = models.TextField(blank=True, null=True)

    photo = models.ImageField(upload_to='employee/', blank=True, null=True)

    def __str__(self):
        return self.name

class Identity(models.Model):

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    family_record = models.ImageField(upload_to='employee/identity/', blank=True, null=True)

    nrc_no = models.CharField(max_length=50)
    nrc_front = models.ImageField(upload_to='employee/identity/', blank=True, null=True)
    nrc_back = models.ImageField(upload_to='employee/identity/', blank=True, null=True)

    passport_no = models.CharField(max_length=50, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    passport_photo = models.ImageField(upload_to='employee/identity/', blank=True, null=True)

    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.employee.name

    class Meta:
        verbose_name_plural = 'Identities'

class Qualification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.employee.name

class Experience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.employee.name

class Employment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.employee.name
