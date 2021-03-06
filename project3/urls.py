"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from rest_framework import routers,serializers,viewsets
from polls.API.V1.serializer_models import UserViewSet,QuestionViewSet,ChoiceVeiwSet
from snippets.urls import *




router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Questions',QuestionViewSet)
router.register(r'Choices',ChoiceVeiwSet)

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
    path('', include('snippets.urls')),



]


