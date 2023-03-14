from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Posts
from .serializers import PostsSerializer
from rest_framework import serializers
import json
#from django.core.serializers import serialize

class PostsApi(APIView):
    def post(self,request): #create
        serializer=PostsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error":"Not valid!"})
    
    def delete(self,request): #delete
        title=request.data['title']
        author=request.data['author']
        serializer=Posts.objects.filter(title=title,author=author)
        serializer.delete()
        return Response({"Message":"ok! deleted"})

    def put(self,request): #edit
        title=request.data['title']
        author=request.data['author']
        content=request.data['content']
        serializer=Posts.objects.get(title=title,author=author)
        serializer.content=content
        serializer.save()
        return Response({"message":"Updated done!"})

class HomeApi(APIView):
    def get(self,request):
        s=Posts.objects.all()
        serializer=PostsSerializer(s,many=True)
        #print(serializer.data)
        return Response({"records":serializer.data})
