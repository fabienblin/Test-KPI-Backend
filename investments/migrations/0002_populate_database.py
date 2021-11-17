# Generated by Django 3.2.9 on 2021-11-16 17:50

from django.db import migrations, transaction
from investments.models import Investment
import json

def populateDB(apps, schema_editor):
	# inform message
	print("\n\n\t=====================================")
	print("\t=======> POPULATING DATABASE <=======")
	print("\t=====================================\n")

	# get local dataset
	dataset = open("dataset.json", 'r').read()
	data_dict = json.loads(dataset)

	# save investments, missing data is replaced by NULL or empty strings
	for data in data_dict:
		with transaction.atomic():
			Investment.objects.create(
			titreoperation = (data["titreoperation"] if ("titreoperation" in data) else ""),
			entreprise = (data["entreprise"] if ("entreprise" in data) else ""),
			annee_de_livraison = (data["annee_de_livraison"]+"-01-01" if ("annee_de_livraison" in data) else None),
			ville = (data["ville"] if ("ville" in data) else ""),
			mandataire = (data["mandataire"] if ("mandataire" in data) else ""),
			ppi = (data["ppi"] if ("ppi" in data) else ""),
			lycee = (data["lycee"] if ("lycee" in data) else ""),
			notification_du_marche = (data["notification_du_marche"] if ("notification_du_marche" in data) else None),
			codeuai = (data["codeuai"] if ("codeuai" in data) else ""),
			longitude = (data["longitude"] if ("longitude" in data) else None),
			etat_d_avancement = (data["etat_d_avancement"] if ("etat_d_avancement" in data) else ""),
			montant_des_ap_votes_en_meu = (data["montant_des_ap_votes_en_meu"] if ("montant_des_ap_votes_en_meu" in data) else None),
			cao_attribution = (data["cao_attribution"] if ("cao_attribution" in data) else None),
			latitude = (data["latitude"] if ("latitude" in data) else None),
			maitrise_d_oeuvre = (data["maitrise_d_oeuvre"] if ("maitrise_d_oeuvre" in data) else ""),
			mode_de_devolution = (data["mode_de_devolution"] if ("mode_de_devolution" in data) else ""),
			annee_d_individualisation = (data["annee_d_individualisation"]+"-01-01" if ("annee_d_individualisation" in data) else None),
			enveloppe_prev_en_meu = (data["enveloppe_prev_en_meu"] if ("enveloppe_prev_en_meu" in data) else None))


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0001_initial'),
    ]

    operations = [
		migrations.RunPython(populateDB)
    ]
