from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    cnp = models.CharField(max_length=13, validators=[MinLengthValidator(13)],unique=True, null=False)
    email = models.EmailField()
    employee_code = models.CharField(max_length=50, null=False)
    role = models.CharField(choices=[("IC","IC"), ("Manager","Manager")],null=False,default="IC")
    manager = models.ForeignKey('self', on_delete=models.SET_NULL,null=True,blank=True,related_name='subordinates' )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"






