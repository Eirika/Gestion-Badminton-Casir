import csv
import control
from db import Tournoi, Adherent, Cotisation, Paiement

from datetime import datetime

with open('donnes/tournoi.csv', 'rt') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    list_tournois = list()
    for row in reader:
        list_tournois.append(Tournoi(nom=row['nom'], lieu=row['lieu'], type=row['type']))
        print("Tournoi ajouté : {} | {} | {}".format(row['nom'], row['lieu'], row['type']))
    control.add_all_tournois(list_tournois)


with open('donnes/adherent.csv', 'rt') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    list_adherents = list()
    for row in reader:
        list_adherents.append(
            Adherent(
                nom=row['nom'],
                prenom=row['prenom'],
                ville=row['ville'],
                cp=row['cp'],
                adresse=row['adresse'],
                date_naissance=row['date_naissance'],
                courriel=row['courriel'],
                tel=row['tel'],
                age=row['age'],
                classement=row['classement']
            )
        )
        print("Adherent ajouté : {} | {}".format(row['nom'], row['prenom']))
    control.add_all_adherents(list_adherents)


with open('donnes/cotisation.csv', 'rt') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    list_cotisations = list()
    for row in reader:
        list_cotisations.append(Cotisation(saison=row['saison'], type=row['type'], tarif=row['tarif']))
        print("Cotisation ajoutée : {} | {} | {}".format(row['saison'], row['type'], row['tarif']))
    control.add_all_cotisations(list_cotisations)


with open('donnes/paiement.csv', 'rt') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    list_paiement = list()
    for row in reader:
        adh = control.get_one_adherents(adh_id=row['adh_id'])
        cotisation = control.get_one_cotisation(cotisation_id=row['cotisation_id'])
        if adh and cotisation:
            the_date = datetime.strptime(row['date'], '%Y-%m-%d').date()
            new_paiement = Paiement(montant=row['montant'], date=the_date, adherent=adh, cotisation=cotisation)
            list_paiement.append(new_paiement)
            print("Paiement ajoutée : {} {} | {} {} | {} | {}".format(adh.nom, adh.prenom, cotisation.saison, cotisation.type, row['montant'], the_date))
    control.add_all_paiement(list_paiement)
