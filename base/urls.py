from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from cars.views import CarAPIDestroy, CarAPIList, CarAPIUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/cars/', CarAPIList.as_view()),
    path('api/v1/cars/<int:pk>/', CarAPIUpdate.as_view()),
    path('api/v1/cars-delete/<int:pk>/', CarAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path('^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
