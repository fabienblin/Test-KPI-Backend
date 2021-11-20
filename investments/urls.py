from django.urls import path, include
from rest_framework import routers
from investments.views import *

router = routers.DefaultRouter()
router.register(r"", InvestmentViewSet)
router.register(r"<int:id>", InvestmentListViewSet, basename="investmentlist")

urlpatterns = [
    path("", include(router.urls)),
]