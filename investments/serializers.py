from rest_framework import serializers
from investments.models import Investment

class InvestmentSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField(required=False)
	titreoperation = serializers.CharField()
	entreprise = serializers.CharField(required=False, allow_blank=True)
	annee_de_livraison = serializers.DateField(required=False, format="%Y")
	ville = serializers.CharField(required=False, allow_blank=True)
	mandataire = serializers.CharField(required=False, allow_blank=True)
	ppi = serializers.CharField(required=False, allow_blank=True)
	lycee = serializers.CharField(required=False, allow_blank=True)
	notification_du_marche = serializers.DateField(required=False, format="%Y-%m-%d")
	codeuai = serializers.CharField(required=False, allow_blank=True)
	longitude = serializers.FloatField(required=False, default=None, allow_null=True)
	etat_d_avancement = serializers.CharField(required=False, allow_blank=True)
	montant_des_ap_votes_en_meu = serializers.IntegerField(required=False, default=None, allow_null=True)
	cao_attribution = serializers.DateField(required=False, format="%Y-%m-%d")
	latitude = serializers.FloatField(required=False, default=None, allow_null=True)
	maitrise_d_oeuvre = serializers.CharField(required=False, allow_blank=True)
	mode_de_devolution = serializers.CharField(required=False, allow_blank=True)
	annee_d_individualisation = serializers.DateField(required=False, format="%Y")
	enveloppe_prev_en_meu = serializers.FloatField(required=False, default=None, allow_null=True)

		
	class Meta:
		model = Investment
		fields = "__all__"
