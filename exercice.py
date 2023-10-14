from random import normalvariate, randint


def lire_classement():
    classement = {}

    # TO-DO: Lire le fichier de classement et insérer les données dans un dictionnaire de dictionnaires.

    return classement


def lire_match():
    rencontres = []

    # TO-DO: Lire le fichier de matchs et insérer les données dans une liste de listes.

    return rencontres


def ecrire_classement(classement):
    # TO-DO: Écrire le classement final dans un fichier text
    # N'oubliez pas d'effacer la ligne pass
    pass


def simulation(diffA, diffB):
    # Données à retourner
    pts_equipeA = 0
    pts_equipeB = 0
    but_equipeA = 0
    but_equipeB = 0
    vrp = 1

    # TO-DO: Calculer diff_dom et diff_vis
    diff_dom = 0
    diff_vis = 0

    # TO-DO: Calculer le nombre de buts de l'equipe à domicile
    alea_d = 0

    # TO-DO: Calculer le nombre de buts de l'equipe visitrice
    alea_v = 0

    # TO-DO: Arrondir les nombres de buts
    # ...

    # TO-DO: Décider qui a remporter la victoire

    return pts_equipeA, pts_equipeB, but_equipeA, but_equipeB, vrp


def trouver_equipe_division(equipe_abv, classement):
    # TO-DO: À l'aide du dictionnaire classement et de l'abbréviation de l'équipe (string),
    # trouvez le nom de l'équipe et sa division
    # N'oubliez pas d'effacer la ligne pass
    pass


def trier_classement(classement):
    classement_trie = {}

    # TO-DO: Pour chaque division, classer les équipes selon leurs nombres de points. classement est un dictionnaire de
    # dictionnaires.

    return classement_trie


def mis_a_jour_classement(equipe, stats, division, classment):
    # TO-DO: Mettre à jour le classement

    # Trier le classement
    classment = trier_classement(classment)

    return classment


def simuler_rencontres(matchs, classement):
    # Pour chaque match
    for match in matchs:
        # TO-DO: nom et la division des deux équipes impliquées.
        teamA, division_equipe_A = '', ''
        teamB, division_equipe_B = '', ''

        # TO-DO: Simuler une rencontre
        pts_equipeA, pts_equipeB, but_equipeA, but_equipeB, vrp = 0, 0, 0, 0, 0

        # Créer les dictionnaires stats_equipe_A et stats_equipe_B
        stats_equipe_A = {}
        stats_equipe_B = {}

        # Mettre à jour le classement
        # ...

    return classement


if __name__ == '__main__':
    ligue_classement = lire_classement()

    ligues_rencontres = lire_match()

    classement_final = simuler_rencontres(ligues_rencontres, ligue_classement)

    ecrire_classement(classement_final)
