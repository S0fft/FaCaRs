from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from cars.views import CarViewSet

router = routers.SimpleRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/carslist/', CarAPIView.as_view()),
    # path('api/v1/carslist/<int:pk>/', CarAPIView.as_view())
    # path('api/v1/carslist/<int:pk>/', CarAPIList.as_view())
    # path('api/v1/carslist/', CarAPIList.as_view()),
    # path('api/v1/carslist/<int:pk>/', CarAPIUpdate.as_view()),
    # path('api/v1/carsdetail/<int:pk>/', CarAPIDetailView.as_view()),
    # path('api/v1/carslist/', CarViewSet.as_view({'get': 'list'})),
    # path('api/v1/carslist/<int:pk>/', CarViewSet.as_view({'put': 'update'})),
]
