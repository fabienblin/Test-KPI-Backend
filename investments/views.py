from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from investments.serializers import *
from investments.models import *

class InvestmentViewSet(viewsets.ModelViewSet):
	queryset = Investment.objects.all()
	serializer_class = InvestmentSerializer

class InvestmentListViewSet(viewsets.ModelViewSet):
	serializer_class = InvestmentListSerializer

	def get_queryset(self):
		print("====ici====")
		id = self.kwargs["id"]
		return Investment.objects.filter(pk=id)