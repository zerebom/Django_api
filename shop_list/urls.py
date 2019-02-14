from django.urls import path

# from . import views
from rest_framework import routers
# from .views import ShoptextViewSet, ShoptextWithDescriptionViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.conf.urls import url
@api_view(['GET', 'POST'])
def hello_world(request, pk):
    if request.method == 'POST':
        return Response({f"message": "Got some data!{pk}", "data": request.data})
    return Response({f'message": "Hello, world!{pk}'})

# router = routers.DefaultRouter()

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^api_view/(?P<pk>[0-9]+)/$', hello_world)

]

# router.register(r'shoptext', ShoptextViewSet)
# router.register(r'recommendation', ShoptextWithDescriptionViewSet)
