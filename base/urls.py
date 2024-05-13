from django.contrib import admin
from django.urls import path

from cars.views import CarAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/carslist/', CarAPIView.as_view())
]
