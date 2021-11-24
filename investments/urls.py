from django.urls import path, include
from rest_framework import routers
from investments.views import *

router = routers.DefaultRouter()
router.register(r"", InvestmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
	path("filter/<filterBy>/<filterVal>/", InvestmentFilterViewSet.as_view({'get': 'list'}))
]