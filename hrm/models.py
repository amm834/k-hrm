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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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

    remark = models.TextField(blank=True, null=True)

    photo = models.ImageField(upload_to='employee/')

    status = models.CharField(max_length=10, choices=(
            ('active', 'Active'),
            ('inactive', 'Inactive'),
        )
    )

    def __str__(self):
        return self.name

class Qualification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.employee

class Experience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.employee

class Employment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.employee
