from django.contrib import admin
from django.urls import path

from cars.views import CarAPIDetailView, CarAPIList, CarAPIUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/carslist/', CarAPIView.as_view()),
    # path('api/v1/carslist/<int:pk>/', CarAPIView.as_view())
    # path('api/v1/carslist/<int:pk>/', CarAPIList.as_view())
    path('api/v1/carslist/', CarAPIList.as_view()),
    path('api/v1/carslist/<int:pk>/', CarAPIUpdate.as_view()),
    path('api/v1/carsdetail/<int:pk>/', CarAPIDetailView.as_view()),

]
