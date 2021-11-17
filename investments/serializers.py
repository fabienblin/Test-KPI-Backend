from rest_framework import serializers
from investments.models import Investment

class InvestmentSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField()
	annee_de_livraison = serializers.DateField("%Y")
	notification_du_marche = serializers.DateField("%Y-%m-%d")
	cao_attribution = serializers.DateField("%Y-%m-%d")
	annee_d_individualisation = serializers.DateField("%Y")
		
	class Meta:
		model = Investment
		fields = "__all__"