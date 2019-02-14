from rest_framework import serializers
from .models import Shoptext


# class ShoptextSerializer(serializers.ModelSerializer):
#     #　モデルには定義されていない、フィールドを追加
#     author = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Shoptext
#         # 出力するカラムの指定
#         fields = ('id', 'query', 'restaurant_name',
#                   'restaurant_id')


# class ShoptextSerializerWithDescription(serializers.ModelSerializer):
#     class Meta:
#         model = Shoptext
#         # 出力するカラムの指定
#         fields = ('id', 'restaurant_name',
#                   'restaurant_id', 'description', 'menus')
