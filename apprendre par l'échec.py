from sqlalchemy.orm import sessionmaker
from datetime import datetime

from db import Adherent, Cotisation, Paiement, Tournoi, Base, engine

# engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
  
# Insert an Address in the address table
new_tournoi = Tournoi(nom='Amical des machins 2', lieu='Home', type='Amical')
session.add(new_tournoi)
session.commit()

# Insert a Person in the person table
new_person1 = Adherent(nom='Chanove 1 ', prenom='Tristan 1 qzerf')
new_person2 = Adherent(nom='Chanove 2 ', prenom='Tristan 1q ez')
new_person3 = Adherent(nom='Chanove 3 ', prenom='Tristanqsdf 1')
new_person = Adherent(nom='Chanove', prenom='Tristan dq 1')
new_person.tournois.append(new_tournoi)
session.add_all([new_person, new_person1, new_person2, new_person3])
session.commit()

new_cotisation = Cotisation(saison=2015, type='Amical', tarif=20.22)
new_cotisation2 = Cotisation(saison=2015, type='Pro', tarif=50)
new_cotisation3 = Cotisation(saison=2016, type='Amical', tarif=10)

new_paiement = Paiement(date=datetime.now().date(), montant=22.50)
new_paiement.adherent = new_person3

new_cotisation.adherents.append(new_paiement)

new_paiement0 = Paiement(date=datetime.now().date(), montant=50)
new_paiement0.cotisation = new_cotisation2
new_person2.paiements.append(new_paiement0)
new_paiement1 = Paiement(date=datetime.now().date(), montant=40)
new_paiement1.cotisation = new_cotisation2
new_person2.paiements.append(new_paiement1)

session.add_all([new_cotisation, new_cotisation2, new_cotisation3, new_person2])
session.commit()
