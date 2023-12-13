

from django.core.exceptions import ValidationError
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=20, unique=True)
    last_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=10)

    class Meta:
        app_label = 'pycontacts'
        managed = False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # Check for duplicate name
        if Contact.objects.filter(first_name=self.first_name, last_name=self.last_name).exclude(pk=self.pk).exists():
            raise ValidationError('Contact with the same name already exists.')

        # Check for duplicate email
        if Contact.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError('Contact with the same email already exists.')

        super().save(*args, **kwargs)

