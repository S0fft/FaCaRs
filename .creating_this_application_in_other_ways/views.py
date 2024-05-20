# from urllib import response
# from django.forms import model_to_dict
# from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from cars.models import Car, Category
from cars.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from cars.serializers import CarSerializer

# class CarViewSet(viewsets.ModelViewSet):
#     # queryset = Car.objects.all()
#     serializer_class = CarSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')

#         if not pk:
#             return Car.objects.all()

#         return Car.objects.filter(pk=pk)

#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         # category = Category.objects.all()
#         category = Category.objects.get(pk=pk)

#         # return Response({'category': [c.name for c in category]})
#         return Response({'category': category.name})


# ---


# class CarAPIListPagination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'page_size'
#     max_page_size = 10000


class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # pagination_class = CarAPIListPagination


class CarAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class CarAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly,)


# ---

# class CarAPIView(APIView):
#     def get(self, request):
#         lst = Car.objects.all()
#         return Response({'posts': CarSerializer(lst, many=True).data})

#     def post(self, request):
#         serializer = CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "PUT method not allowed [Does not indicated the primary key]"})
#         try:
#             instance = Car.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#         serializer = CarSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "DELETE method not allowed [Does not indicated the primary key]"})
#         try:
#             instance = Car.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object does not exists"})
#         return Response({"post": f"The objects {pk} is deleted"})
