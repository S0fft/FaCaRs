from urllib import response

from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import Car
from cars.serializer import CarSerializer


class CarAPIView(APIView):
    def get(self, request):
        lst = Car.objects.all().values()

        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Car.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )

        return Response({'post': model_to_dict(post_new)})


# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
