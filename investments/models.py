from django.db import models

class Investment(models.Model):
	titreoperation = models.CharField(max_length=255, blank=True)			#": "Ravalement des façades, mise en conformité des ateliers et création foyer des élèves",
	entreprise = models.CharField(max_length=255, blank=True)				#": "Coulon SA",
	annee_de_livraison = models.DateField(blank=True, null=True)			#": "2006",
	ville = models.CharField(max_length=255, blank=True)					#": "Paris 12ème",
	mandataire = models.CharField(max_length=255, blank=True)				#": "SEMAEST",
	ppi = models.CharField(max_length=255, blank=True)						#": "2001/2006",
	lycee = models.CharField(max_length=255, blank=True)					#": "Métiers-de-l'ameublement",
	notification_du_marche = models.DateField(blank=True, null=True)		#": "2002-10-28",
	codeuai = models.CharField(max_length=255, blank=True)					#": "0750784V",
	longitude = models.FloatField(blank=True, null=True)					#": 2.391504327000064,
	etat_d_avancement = models.CharField(max_length=255, blank=True)		#": "Opération livrée",
	montant_des_ap_votes_en_meu = models.IntegerField(blank=True, null=True)#": 1,
	cao_attribution = models.DateField(blank=True, null=True)				#": "2005-10-02",
	latitude = models.FloatField(blank=True, null=True)						#": 48.84675373500005,
	maitrise_d_oeuvre = models.CharField(max_length=255, blank=True)		#": "Laumonnier Menninger / SLI",
	mode_de_devolution = models.CharField(max_length=255, blank=True)		#": "Ent générale",
	annee_d_individualisation = models.DateField(blank=True, null=True)		#": "1998",
	enveloppe_prev_en_meu = models.FloatField(blank=True, null=True)		#": 0.43

	def __str__(self):
		return self.titreoperation
