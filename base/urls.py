from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from cars.views import CarAPIDestroy, CarAPIList, CarAPIUpdate

# from cars.views import CarViewSet

# class CustomReadOnlyRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         routers.Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         )
#     ]

# router = CustomReadOnlyRouter()
# router = routers.DefaultRouter()

# router.register(r'cars', CarViewSet, basename='cars')
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cars/', CarAPIList.as_view()),
    path('api/v1/cars/<int:pk>/', CarAPIUpdate.as_view()),
    path('api/v1/cars-delete/<int:pk>/', CarAPIDestroy.as_view()),
    # path('api/v1/', include(router.urls)),
    # path('api/v1/carslist/', CarAPIView.as_view()),
    # path('api/v1/carslist/<int:pk>/', CarAPIView.as_view())
    # path('api/v1/carslist/<int:pk>/', CarAPIList.as_view())
    # path('api/v1/carslist/', CarAPIList.as_view()),
    # path('api/v1/carslist/<int:pk>/', CarAPIUpdate.as_view()),
    # path('api/v1/carsdetail/<int:pk>/', CarAPIDetailView.as_view()),
    # path('api/v1/carslist/', CarViewSet.as_view({'get': 'list'})),
    # path('api/v1/carslist/<int:pk>/', CarViewSet.as_view({'put': 'update'})),
]
