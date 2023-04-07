from django.urls import path, include
from rest_framework import routers

from .views import *

app_name = 'task'

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('status/', get_status)
    
]
