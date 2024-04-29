from django.db import models

# Create your models here.

    
class Location(models.Model):
    location_id = models.IntegerField()
    location_name = models.CharField(max_length=100)    

    def __str__(self):
        return self.location_name


class Department(models.Model):
    department_id = models.IntegerField()
    department_name = models.CharField(max_length=200)    

    def __str__(self):
        return self.department_name



class EmpData(models.Model):
    emp_id = models.CharField(max_length=100, unique=True)
    emp_name = models.CharField(max_length=254, unique=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.emp_name
    
    def save(self, *args, **kwargs):
        self.emp_name = self.emp_name.lower()
        super().save(*args, **kwargs)

    
