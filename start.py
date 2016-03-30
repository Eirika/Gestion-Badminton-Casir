from hud import hud
from db import control
import os
clear = lambda: os.system('cls')


def menu_adh():
    stopAdh = False
    while stopAdh is False:
        try:
            print('------------------------')
            print('------- ADHERENT -------')
            print('  1) Afficher tous les adhérents')
            print('  2) Afficher les détails d\'un adhérents choisi')
            print('  3) Ajouter un adhérent')
            print('  4) Supprimer un adhérent')
            print('  5) Ajouter un paiement d\'un adhérent')
            print('  6) Afficher les paiements d\'un adhérent')
            print('  7) Ajouter un adhérent à un tournoi')
            print('  8) Retour au menu principal')
            choiceAdh = int(input("Entrez votre choix : ")) or 8
            if choiceAdh == 1:
                hud.hud_print_adherents(control)
            elif choiceAdh == 2:
                hud.hud_print_details_adherents(control)
            elif choiceAdh == 3:
                hud.hud_add_adherent(control)
            elif choiceAdh == 4:
                hud.hud_del_adherent(control)
            elif choiceAdh == 5:
                hud.hud_add_paiement_adherent(control)
            elif choiceAdh == 6:
                hud.hud_print_paiements_adherent(control)
            elif choiceAdh == 7:
                hud.hud_add_tournoi_adherent(control)
            else:
                stopAdh = True
        except ValueError:
            pass
        except Exception as e:
            print(e)
            print('Erreur lors du choix, retour au menu principal')
            stopAdh = True


def menu_tournoi():
    stopTournoi = False
    clear()
    while stopTournoi is False:
        try:
            print('---------------------')
            print('------ TOURNOIS -----')
            print('  1) Afficher tous les tournois')
            print('  2) Afficher les participant d\'un tournoi')
            print('  3) Ajouter un tournoi')
            print('  4) Supprimer un tournoi')
            print('  5) Ajouter un adhérent à un tournoi')
            print('  6) Retour au menu principal ')
            choiceTournoi = int(input("Entrez votre choix : ")) or 6
            if choiceTournoi == 1:
                hud.hud_print_tournois(control)
            elif choiceTournoi == 2:
                hud.hud_print_details_tournoi(control)
            elif choiceTournoi == 3:
                hud.hud_add_tournoi(control)
            elif choiceTournoi == 4:
                try:
                    hud.hud_del_tournoi(control)
                except Exception:
                    print('Erreur lors de la suppression du tournoi, veuillez réessayer')
            elif choiceTournoi == 5:
                hud.hud_add_tournoi_adherent(control)
            else:
                stopTournoi = True
        except ValueError:
            pass
        except Exception as e:
            print(e)
            print('Erreur lors du choix, retour au menu principal')
            stopTournoi = True


def menu_cotisation():
    stopCotisation = False
    clear()
    while stopCotisation is False:
        try:
            print('------------------------')
            print('------ COTISATIONS -----')
            print('  1) Afficher toutes les cotisations')
            print('  2) Afficher les cotisations d\'une année')
            print('  3) Afficher les cotisations d\'un type')
            print('  4) Retour au menu principal ')
            choiceTournoi = int(input("Entrez votre choix : ")) or 4
            if choiceTournoi == 1:
                hud.hud_print_cotisation(control)
            elif choiceTournoi == 2 or choiceTournoi == 3:
                hud.hud_print_cotisation_param(control, choiceTournoi)
            else:
                stopCotisation = True
        except ValueError:
            pass
        except Exception as e:
            print(e)
            print('Erreur lors du choix, retour au menu principal')
            stopCotisation = True

if __name__ == "__main__":
    stop = False
    clear()
    while stop is False:
        print('---------------------')
        print('------- MENU --------')
        print('  1) Adhérents')
        print('  2) Tournois')
        print('  3) Cotisations')
        print('  4) Quitter')
        print('---------------------')
        try:
            menuChoice = int(input("Entrez votre choix : ")) or 4
            
            if menuChoice > 8:
                stop = True
            elif menuChoice == 1:
                menu_adh()
            elif menuChoice == 2:
                menu_tournoi()
            elif menuChoice == 3:
                menu_cotisation()
            else:
                stop = True
        except ValueError:
            pass
        except Exception as e:
            raise e
