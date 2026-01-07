from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from myapp.views import UserViewSet,BlogViewSet
router=DefaultRouter()
router.register('User',UserViewSet)
router.register('Blog',BlogViewSet)
urlpatterns = [
    path('admin/',admin.site.urls), 
    path('',include(router.urls)),
]