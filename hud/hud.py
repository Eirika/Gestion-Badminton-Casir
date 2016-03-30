import os
clear = lambda: os.system('cls')
from datetime import datetime


def hud_add_adherent(control):
    clear()
    nom = None
    while not nom:
        nom = input("Nom : ")
    prenom = None
    while not prenom:
        prenom = input("Prenom : ")
    adresse = input("Adresse [facultatif] : ") or None
    cp = input("Code Postal [facultatif] : ") or None
    ville = input("Ville [facultatif] : ") or None
    date_naissance = input("Date de naissance (AAAA-MM-JJ) [facultatif] : ") or None
    courriel = input("Email [facultatif] : ") or None
    tel = input("Téléphone (sans indicatif) [facultatif] : ") or None
    age = input("Age [facultatif] : ") or None
    classement = input("Classement [NC par défaut] : ") or 'NC'

    control.add_adherent(nom=nom,
                        prenom=prenom,
                        ville=ville,
                        cp=cp,
                        adresse=adresse,
                        date_naissance=date_naissance,
                        courriel=courriel,
                        tel=tel,
                        age=age,
                        classement=classement)


def hud_print_adherents(control):
    clear()
    for adherent in control.get_all_adherents():
        print("N°{})  {} {} | Classé {}".format(adherent.adh_id, adherent.nom, adherent.prenom, adherent.classement))


def hud_print_details_adherents(control):
    clear()
    hud_print_adherents(control)
    adherent_id = int(input("Entrez le N° de l'adhérent : "))
    adh = control.get_one_adherents(adh_id=adherent_id)
    print("N°{}) {} {}".format(adh.adh_id, adh.nom, adh.prenom))
    print("{} {} {}".format(adh.adresse, adh.cp, adh.ville))
    print("{} {} | {} {} ans".format(adh.courriel, adh.tel, adh.date_naissance, adh.age))
    print("Classé {}".format(adh.classement))


def hud_del_adherent(control):
    clear()
    hud_print_adherents(control)
    adherent_id = int(input("Entrez le N° de l'adhérent à supprimer : "))
    control.del_adherent(adh_id=adherent_id)


def hud_print_tournois(control):
    clear()
    for tournoi in control.get_all_tournois():
        print("N°{})  {} | {} | {}".format(tournoi.tournoi_id, tournoi.nom, tournoi.lieu, tournoi.type))


def hud_print_details_tournoi(control):
    clear()
    hud_print_tournois(control)
    tournoi_id = int(input("Entrez le N° du tournoi : "))
    tournoi = control.get_one_tournois(tournoi_id=tournoi_id)
    clear()
    print("N°{}) {} {} [{}]".format(tournoi.tournoi_id, tournoi.nom, tournoi.lieu, tournoi.type))
    if tournoi.adherents:
        print("Participant : ")
        for adherent in tournoi.adherents:
            print("N°{}) {} {} [{}]".format(adherent.adh_id, adherent.nom, adherent.prenom, adherent.classement))
    else:
        print('Aucun adhérent inscrit')
    print('\n\n')


def hud_add_tournoi_adherent(control):
    clear()
    hud_print_tournois(control)
    tournoi_id = int(input("Entrez le N° du tournoi : "))
    clear()
    hud_print_adherents(control)
    adherent_id = int(input("Entrez le N° de l'adhérent : "))
    control.add_adherent_to_tournoi(tournoi_id, adherent_id)


def hud_add_tournoi(control):
    clear()
    nom = None
    while not nom:
        nom = input("Nom : ") or None
    lieu = None
    while not lieu:
        lieu = input("Lieu (ville suffit) : ") or None
    type = None
    while not type or type not in ['Amical', 'Pro']:
        type = input("Type [Amical | Pro] : ") or None

    control.add_tournoi(nom=nom, lieu=lieu, type=type)


def hud_del_tournoi(control):
    clear()
    hud_print_tournois(control)
    tournoi_id = input("Entrez le N° du tournoi à supprimer : ")
    control.del_tournoi(tournoi_id)


def hud_add_paiement_adherent(control):
    clear()
    hud_print_adherents(control)
    adherent_id = int(input("Entrez le N° de l'adhérent : "))
    clear()
    hud_print_cotisation(control)
    cotisation_id = int(input("Entrez le N° de la cotisation choisie : "))
    clear()
    date = input("Entrez la date [{}] : ".format(datetime.now().date())) or datetime.now().date()
    montant = input("Entrez le montant : ")
    control.add_paiement(adh_id=adherent_id, cotisation_id=cotisation_id, date=date, montant=montant)


def hud_print_paiements_adherent(control):
    clear()
    hud_print_adherents(control)
    adherent_id = int(input("Entrez le N° de l'adhérent : "))
    paiements = control.get_all_paiements_adherent(adherent_id)
    if not paiements:
        print("--------------------------")
        print("Aucun réglement effectué !")
        print("--------------------------")
    else:
        for paiement in paiements:
            print("Paiement le {} d'un montant de {} pour la saison {} - {}".format(paiement.date, paiement.montant, paiement.cotisation.saison, paiement.cotisation.type))


def hud_print_cotisation(control):
    clear()
    for cotisation in control.get_all_cotisation():
        print("N°{}) Saison {} {} | {} eur".format(cotisation.cotisation_id, cotisation.saison, cotisation.type, cotisation.tarif))


def hud_print_cotisation_param(control, param):
    clear()
    if param == 2:
        annee = int(input("Entrez l'année souhaitée : "))
        cotisations = control.get_cotisation_by_param(saison=annee)
    else:
        type = None
        while not type or type not in ['Amical', 'Pro']:
            type = input("Entrez le type souhaitée : ")
        cotisations = control.get_cotisation_by_param(type=type)
    for cotisation in cotisations:
        print("N°{}) Saison {} {} | {} eur".format(cotisation.cotisation_id, cotisation.saison, cotisation.type, cotisation.tarif))
