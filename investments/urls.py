from django.urls import path, include
from rest_framework import routers
from investments.views import InvestmentViewSet

router = routers.DefaultRouter()
router.register(r"", InvestmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]