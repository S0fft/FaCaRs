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
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "PUT method not allowed"})

        try:
            instance = Car.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CarSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)

    #     if not pk:
    #         return Response({"error": "PUT method not allowed"})

    #     try:
    #         instance = Car.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Object does not exists"})

    #     serializer = CarSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.delete()

    #     return Response({"post": serializer.data})
