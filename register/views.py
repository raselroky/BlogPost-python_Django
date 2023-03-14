from django.shortcuts import render
from .models import RegisterModel
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterApi(APIView):

    def post(self,request):
        serializer= RegisterSerializer(data=request.data)
        if serializer.is_valid():
            password1=request.data['password']
            password2=request.data['confirm_password']
                
            if(password1!=password2):
                return Response({"Message":"Password did not matched!"})
            if(len(str(password1))<7 and len(str(password2))<7):
                return Response({"Message":"Password Too short! try Again."})
            if(any(map(str.isdigit, password1))==False or any(map(str.isalpha, password1))==False):
                return Response({"Message":"Character or Number missing ,try again!"})

            
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error":"Not valid!"})


class LoginApi(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']

        username1=RegisterModel.objects.filter(email=email,password=password).exists()
        password1=RegisterModel.objects.filter(password=password,email=email).exists()

        if(username1 and password1):
            return Response({"Message":"Successfully Login!"})
        else:
            return Response({"Message":"Error, complete your registration then try login."})