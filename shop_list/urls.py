from django.urls import path

# from . import views
from rest_framework import routers
from .views import ShoptextViewSet

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

router = routers.DefaultRouter()
router.register(r'shoptext',ShoptextViewSet)