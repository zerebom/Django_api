from rest_framework import serializers
from .models import Shoptext 

class ShoptextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoptext
        fields =('restaurant_name','restaurant_id','description','menus')

