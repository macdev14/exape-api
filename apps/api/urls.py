from django.urls import include, path
from rest_framework import routers


from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken.views import(
    obtain_auth_token
)
router = routers.DefaultRouter()
router.register(r'usuario', views.UserViewSet, basename="users")
router.register(r'cotacao/processamento', views.ProcessViewSet,basename="processamento")
router.register(r'cotacao', views.QuoteViewSet,basename="quote")

urlpatterns = [
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]