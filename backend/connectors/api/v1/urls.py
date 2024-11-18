from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137488ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137488", Testconnectors137488ViewSet, basename="testconnectors137488"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
