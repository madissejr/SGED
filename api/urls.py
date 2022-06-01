from django.db import router
from django.urls import path

from api.views import (
    ArquivoViewSet,
    DocumentoViewSet,
    CacifoViewSet,
    SeccaoViewSet
)
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()
router.register(r'arquivo', ArquivoViewSet, basename='arquivo')
router.register(r'documentos', DocumentoViewSet, basename='documentos')
router.register(r'cacifo', CacifoViewSet, basename='cacifo')
router.register(r'seccao', SeccaoViewSet, basename='seccao')



urlpatterns = router.urls