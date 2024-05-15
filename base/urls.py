from django.contrib import admin
from django.urls import path

from cars.views import CarAPIList, CarAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/carslist/', CarAPIView.as_view()),
    # path('api/v1/carslist/<int:pk>/', CarAPIView.as_view())
    path('api/v1/carslist/', CarAPIList.as_view()),
    path('api/v1/carslist/<int:pk>/', CarAPIList.as_view())
]
