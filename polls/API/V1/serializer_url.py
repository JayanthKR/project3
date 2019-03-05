from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .serializer_models import UserViewSet,QuestionViewSet,ChoiceVeiwSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Questions',QuestionViewSet)
routers.register(r'Choices',ChoiceVeiwSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]