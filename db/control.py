from sqlalchemy.orm import sessionmaker

from models.models import Adherent, Cotisation, Paiement, Tournoi, Base, engine

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# ADHERENTS
def add_adherent(**kwargs):
    new_adherent = Adherent(**kwargs)
    session.add(new_adherent)
    session.commit()


def add_all_adherents(list_adherent):
    session.add_all(list_adherent)
    session.commit()


def get_all_adherents():
    return session.query(Adherent).all()


def get_one_adherents(**kwargs):
    return session.query(Adherent).filter_by(**kwargs).first()


def del_adherent(**kwargs):
    session.delete(get_one_adherents(**kwargs))
    session.commit()


def get_paiements_adherent(adh_id, cotisation_id):
    return session.query(Paiement).join(Paiement.adherent).join(Paiement.cotisation).filter(Adherent.adh_id == adh_id).filter(Cotisation.cotisation_id == cotisation_id).all()


def get_all_paiements_adherent(adh_id):
    return session.query(Paiement).join(Paiement.adherent).join(Paiement.cotisation).filter(Adherent.adh_id == adh_id).all()


# TOURNOIS
def add_tournoi(**kwargs):
    new_tournoi = Tournoi(**kwargs)
    session.add(new_tournoi)
    session.commit()


def add_all_tournois(list_tournois):
    session.add_all(list_tournois)
    session.commit()


def get_all_tournois():
    return session.query(Tournoi).all()


def get_one_tournois(**kwargs):
    return session.query(Tournoi).filter_by(**kwargs).first()


def del_tournoi(tournoi_id):
    session.delete(get_one_tournois(tournoi_id=tournoi_id))
    session.commit()


def add_adherent_to_tournoi(tournoi_id, adh_id):
    the_tournoi = get_one_tournois(tournoi_id=tournoi_id)
    the_tournoi.adherents.append(get_one_adherents(adh_id=adh_id))
    session.add(the_tournoi)
    session.commit()


# COTISATIONS
def add_cotisation(**kwargs):
    new_cotisation = Cotisation(**kwargs)
    session.add(new_cotisation)
    session.commit()


def add_all_cotisations(list_cotisation):
    session.add_all(list_cotisation)
    session.commit()


def get_all_cotisation():
    return session.query(Cotisation).all()


def get_one_cotisation(**kwargs):
    return session.query(Cotisation).filter_by(**kwargs).first()


def get_cotisation_by_param(**kwargs):
    return session.query(Cotisation).filter_by(**kwargs).all()


# PAIEMENTS
def add_all_paiement(list_paiement):
    session.add_all(list_paiement)
    session.commit()


def add_paiement(**kwargs):
    new_paiement = Paiement(**kwargs)
    session.add(new_paiement)
    session.commit()
