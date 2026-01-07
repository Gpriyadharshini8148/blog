from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User,Blog
from .serializers import UserSerializer,BlogSerializer

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
class BlogViewSet(ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
