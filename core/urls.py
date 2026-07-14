from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from carteira.views import AtivoViewSet, TransacaoViewSet


router = DefaultRouter()
router.register('ativos', AtivoViewSet)
router.register('transacoes', TransacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

