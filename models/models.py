from datetime import datetime, date

from sqlalchemy import create_engine, Table, Column, Float, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
engine = create_engine('sqlite:///db.sqlite3')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


adh_tournoi_assoc_table = Table('adh_to_tournoi', Base.metadata,
    Column('adh_id', Integer, ForeignKey('adherent.adh_id')),
    Column('tournoi_id', Integer, ForeignKey('tournoi.tournoi_id'))
)


class Adherent(Base):
    __tablename__ = 'adherent'
    adh_id = Column(Integer, primary_key=True, nullable=False)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    ville = Column(String)
    cp = Column(String)
    adresse = Column(String)
    date_naissance = Column(String)
    courriel = Column(String)
    tel = Column(Integer)
    classement = Column(String, nullable=False)

    tournois = relationship(
        "Tournoi",
        secondary=adh_tournoi_assoc_table,
        back_populates="adherents")

    paiements = relationship(
        "Paiement",
        back_populates="adherent")

    def __init__(self, nom, prenom, ville=None, cp=None, adresse=None, date_naissance=None, courriel=None, tel=None, classement='NC'):
        self.nom = nom
        self.prenom = prenom
        self.ville = ville
        self.cp = cp
        self.adresse = adresse
        self.date_naissance = date_naissance
        self.courriel = courriel
        self.tel = tel
        self.classement = classement

    @staticmethod
    def get_age(adh):
        today = date.today()
        date_naissance = datetime.strptime(adh.date_naissance, '%Y-%m-%d')
        return today.year - date_naissance.year - ((today.month, today.day) < (date_naissance.month, date_naissance.day))


class Tournoi(Base):
    __tablename__ = 'tournoi'
    tournoi_id = Column(Integer, primary_key=True, nullable=False)
    nom = Column(String, nullable=False)
    lieu = Column(String, nullable=False)
    type = Column(String, nullable=False)
 
    adherents = relationship(
        "Adherent",
        secondary=adh_tournoi_assoc_table,
        back_populates="tournois")


class Paiement(Base):
    __tablename__ = 'paiement'
    paiement_id = Column(Integer, primary_key=True, nullable=False)
    adh_id = Column(Integer, ForeignKey('adherent.adh_id'))
    cotisation_id = Column(Integer, ForeignKey('cotisation.cotisation_id'))
    adherent = relationship("Adherent", back_populates="paiements")
    cotisation = relationship("Cotisation", back_populates="adherents")

    date = Column(Date, default=datetime.now().date())
    montant = Column(Float, nullable=False)


class Cotisation(Base):
    __tablename__ = 'cotisation'
    cotisation_id = Column(Integer, primary_key=True, nullable=False)
    saison = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    tarif = Column(Float, nullable=False)

    adherents = relationship(
        "Paiement",
        back_populates="cotisation")


Base.metadata.create_all(engine)
