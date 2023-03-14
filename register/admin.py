from django.contrib import admin
from .models import RegisterModel

@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email']

