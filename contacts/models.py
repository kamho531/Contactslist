from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_format(number):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pattern.match(number):
        return True
    else:
        raise ValidationError(
            _('%(number)s is incorrect phone number format'),
            params={'number':number},
        )


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(validators=[validate_format], max_length=20)
    comment = models.CharField(max_length=100)


    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    

