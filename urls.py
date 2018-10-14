from django.urls import path

from django.conf.urls import url

from stockprices  import views

from .apiviews import PricesList, PriceDetail, UserCreate, Login

from rest_framework import routers

from rest_framework.authtoken import views

urlpatterns = [

url(r'^prices/', PricesList.as_view(), name="prices_list"),

url(r'^price/(?P<id>\d+)/', PriceDetail.as_view(), name="price_detail"),

url(r'^users/', UserCreate.as_view(), name="usercreate"),

url(r'^login/', Login.as_view(), name="login"),
]


