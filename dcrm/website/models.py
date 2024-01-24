from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    role = models.CharField(max_length=50)

    def __str__(self) -> str:
        return(f"{self.first_name} {self.last_name}")