from sqlalchemy.orm import sessionmaker

from db import Adherent, Cotisation, Paiement, Tournoi, Base, engine

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_adherent(**kwargs):
    new_adherent = Adherent(**kwargs)
    session.add(new_adherent)
    session.commit()


def get_all_adherents():
    return session.query(Adherent).all()


def get_one_adherents(nom):
    return session.query(Adherent).filter(nom)


def add_tournoi(**kwargs):
    new_tournoi = Tournoi(**kwargs)
    session.add(new_tournoi)
    session.commit()


def get_all_tournois():
    return session.query(Tournoi).all()


def get_one_tournois(nom):
    return session.query(Tournoi).filter(nom=nom).first()
