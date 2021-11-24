from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import views, viewsets
from investments.serializers import *
from investments.models import *

class InvestmentViewSet(viewsets.ModelViewSet):
	queryset = Investment.objects.all()
	serializer_class = InvestmentSerializer

class InvestmentFilterViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = InvestmentSerializer

	def get_queryset(self):
		filterBy = self.kwargs["filterBy"]
		filterVal = self.kwargs["filterVal"]

		if (filterBy == "ville"):
			return Investment.objects.filter(ville=filterVal)
		elif (filterBy == "etat_d_avancement"):
			return Investment.objects.filter(etat_d_avancement=filterVal)
		else:
			HttpResponse('Bad Request', status=400)