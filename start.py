import control


def hud_add_adherent():
    nom = input("Nom : ")
    prenom = input("Prenom : ")
    adresse = input("Adresse [facultatif] : ") or None
    cp = input("Code Postal [facultatif] : ") or None
    ville = input("Ville [facultatif] : ") or None
    date_naissance = input("Date de naissance (AAAA/MM/JJ) [facultatif] : ") or None
    courriel = input("Email [facultatif] : ") or None
    tel = input("Téléphone (sans indicatif) [facultatif] : ") or None
    age = input("Age [facultatif] : ") or None
    classement = input("Classement [NC pas défaut] : ") or 'NC'

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
                        

def hud_print_adherents():
    for adherent in control.get_all_adherents():
        print("{} {} | Classé {}".format(adherent.nom, adherent.prenom, adherent.classement))


def hud_add_tournoi():
    nom = input("Nom : ") or None
    lieu = input("Lieu (ville suffit) : ") or None
    type = input("Type [Amical | Pro] : ") or None

    control.add_tournoi(nom=nom, lieu=lieu, type=type)


def hud_print_tournois():
    for tournoi in control.get_all_tournois():
        print("{} à {} | Type {}".format(tournoi.nom, tournoi.lieu, tournoi.type))


if __name__ == "__main__":
    stop = False
    while stop is False:
        print('-----------------------')
        print('''------- MENU -------
            1) Ajouter un adhérent
            2) Afficher tous les adhérents
            3) Ajouter un tournoi
            4) Afficher tous les tournois''')
        try:
            menuChoice = int(input("Entrez votre choix : ")) or 50
            print('-----------------------')
            if menuChoice > 8:
                stop = True
            elif menuChoice == 1:
                hud_add_adherent()
            elif menuChoice == 2:
                hud_print_adherents()
            elif menuChoice == 3:
                hud_add_tournoi()
            elif menuChoice == 4:
                hud_print_tournois()
        except ValueError:
            pass
        except Exception as e:
            raise e
