from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from evento.views import EventoViewSet
from evento.views import CategoriaViewSet
from users.views import UsuarioSerializerViewSet, UserSerializerViewSet


router = routers.DefaultRouter()
router.register(
    'evento', EventoViewSet, base_name='evento'
)

router.register(
    'usuario', UsuarioSerializerViewSet, base_name='usuario'
)

router.register(
    'categoria', CategoriaViewSet, base_name='categoria'
)

router.register(
    'user', UserSerializerViewSet, base_name='user'
)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
    path('', include('emailfood.urls')),
    path('', include(router.urls)),
]
