from rest_framework import routers
from .api import ClientViewSet
from .views import login

from django.urls import path

router = routers.DefaultRouter()
router.register('/drf/clients',ClientViewSet,'clients')

urlpatterns = [
    path('/login/', login, name='login'),
]


urlpatterns+=router.urls