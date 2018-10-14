from rest_framework.views import APIView
from rest_framework import generics, status

from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Prices
from .serializers import PricesSerial, UserSerial
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib import auth
from django.contrib.auth.models import User

class PricesList(generics.ListCreateAPIView):
	queryset = Prices.objects.all()[:5]
	serializer_class = PricesSerial


class PriceDetail(generics.RetrieveDestroyAPIView):
	serializer_class = PricesSerial
	#lookup_url_kwarg= "id"

	
	def get_queryset(self):
	#	id = self.kwargs.get(self.lookup_url_kwarg)
	#	price = Prices.objects.filter(id=id)
	#	return price
		queryset = Prices.objects.filter(id=self.kwargs["id"])
		return queryset
	   


class UserCreate(generics.CreateAPIView):
	authentication_classes= ()
	permission_classes =()
	serializer_class= UserSerial



class Login(APIView):
	permission_classes = ()


	def post(self, request, ):
		#uname = request.data.get("username")
		#pwd = request.data.get("password")
		#return self.get(uname=uname,pwd=pwd)

		#user = authenticate(username='med', password='mypassxx')

		return self.get(request)

		
		

	def get(self, request,):

		uname = request.data.get('username')
		pwd = request.data.get("password")

		user = authenticate(username=uname, password=pwd)

		if user:
			token = Token.objects.get(user=user)
			return Response({"token": token.key})

		else:
			return Response({"got an error":"wrong credentials"},status=status.HTTP_404_NOT_FOUND)



		






		



