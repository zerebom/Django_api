from django.urls import path

# from . import views
from rest_framework import routers
from .views import ShoptextViewSet, ShoptextWithDescriptionViewSet

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

router = routers.DefaultRouter()
router.register(r'shoptext', ShoptextViewSet)
router.register(r'recommendation', ShoptextWithDescriptionViewSet)
