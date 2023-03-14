from rest_framework import serializers
from . models import RegisterModel

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegisterModel
        fields=('__all__')