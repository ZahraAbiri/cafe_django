from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '+919198989'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list
    # phone_number = models.CharField(max_length=10)
    email = models.EmailField(null=False, unique=True)
    role = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=8)

    class Meta:
        verbose_name = 'کاربر'

    def __str__(self):
        return self.username + ":" + self.email + ":" + self.phone_number + ":" + self.last_name


class Comments(models.Model):
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    phone_number = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                  message="Phone number must be entered in the format: '+919198989'. Up to 10 digits allowed.")

    def __str__(self):
        return self.description+":"+str(self.phone_number)+":"+self.name+":"+self.family
