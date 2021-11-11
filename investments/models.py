from django.db import models

class Investment(models.Model):
	titreoperation = models.CharField(max_length=255)		#": "Ravalement des façades, mise en conformité des ateliers et création foyer des élèves",
	entreprise = models.CharField(max_length=255)			#": "Coulon SA",
	annee_de_livraison = models.DateField()				#": "2006",
	ville = models.CharField(max_length=255)				#": "Paris 12ème",
	mandataire = models.CharField(max_length=255)			#": "SEMAEST",
	ppi = models.CharField(max_length=255)					#": "2001/2006",
	lycee = models.CharField(max_length=255)				#": "Métiers-de-l'ameublement",
	notification_du_marche = models.DateField()			#": "2002-10-28",
	codeuai = models.CharField(max_length=255)				#": "0750784V",
	longitude = models.FloatField()							#": 2.391504327000064,
	etat_d_avancement = models.CharField(max_length=255)	#": "Opération livrée",
	montant_des_ap_votes_en_meu = models.IntegerField()		#": 1,
	cao_attribution = models.DateField()				#": "2005-10-02",
	latitude = models.FloatField()							#": 48.84675373500005,
	maitrise_d_oeuvre = models.CharField(max_length=255)	#": "Laumonnier Menninger / SLI",
	mode_de_devolution = models.CharField(max_length=255)	#": "Ent générale",
	annee_d_individualisation = models.DateField()		#": "1998",
	enveloppe_prev_en_meu = models.FloatField()				#": 0.43

	def __str__(self):
		return self.titreoperation
