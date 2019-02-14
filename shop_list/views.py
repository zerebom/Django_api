from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import django_filters
from rest_framework import viewsets, filters
from .models import Shoptext
from .serializer import ShoptextSerializer, ShoptextSerializerWithDescription
from django_filters import rest_framework as filters
import random


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# class ShopFilter(filters.FilterSet):
#     # どんなふうにフィルタリングするか

#     # def get_shop_ranking(self, queryset, name, value)
#     # name→検索フィールド,
#     def get_random_sample(query=''):
#         return random.sample(range(10000), 10)
#     # value ->ユーザーが投げるクエリ
#     def get_ranking(self, queryset, name, value):
#         return queryset.objects.filter(id__in=get_random_sample())

#     ranking = filters.NumberFilter(method='ranking')

#     class Meta:
#         model = Shoptext
#         fields = ['query', 'ranking']


# class ShoptextViewSet(viewsets.ModelViewSet):
#     # どんなふうに出力するか
#     def get_shop_ranking(query=''):
#         return random.sample(range(10000), 10)

#     # 引数
#     # queryset = Shoptext.objects.filter(id__in=get_shop_ranking())

#     queryset = Shoptext.objects.all()
#     serializer_class = ShoptextSerializer
#     filter_class = ShopFilter


# class ShoptextWithDescriptionViewSet(viewsets.ModelViewSet):
#     def get_shop_ranking(query=''):
#         return random.sample(range(10000), 10)

#     # 引数
#     queryset = Shoptext.objects.filter(id__in=get_shop_ranking())
#     serializer_class = ShoptextSerializerWithDescription
#     filter_fields = ('id')
