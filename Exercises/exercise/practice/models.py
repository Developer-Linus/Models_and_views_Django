from django.db import models

class Department(models.Model):
    department = models.CharField(max_length=20)
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

employees = Employee.objects.select_related('category')

class Product(models.Model):
    name = models.CharField(max_length=20)
class Description(models.Model):
    description = models.TextField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product')

product_description = Description.objects.select_related('product') 


class Student(models.Model):
    name = models.CharField(max_length=150)
class Course(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, on_delete=models.CASCADE, related_name='students')

students = Course.objects.prefetch_related('students')


