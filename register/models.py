from django.db import models

class RegisterModel(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name +' '+self.last_name