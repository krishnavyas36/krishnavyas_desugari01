

# Create your models here.
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    class Meta:
        app_label = 'pycontacts'
        managed = False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
