from urllib import response

from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import Car
from cars.serializers import CarSerializer


class CarAPIView(APIView):
    def get(self, request):
        lst = Car.objects.all()

        return Response({'posts': CarSerializer(lst, many=True).data})

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Car.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )

        return Response({'post': CarSerializer(post_new).data})


# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
