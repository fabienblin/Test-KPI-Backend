from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from investments.serializers import InvestmentSerializer
from investments.models import Investment

class InvestmentViewSet(viewsets.ModelViewSet):
	queryset = Investment.objects.all()
	serializer_class = InvestmentSerializer