from random import normalvariate, randint

def lire_classement(path):
    classement = {}
    with open(path, 'r') as file:
        current_division = None
        for line in file:
            line = line.strip()
            if not line:
                continue  
            if line[0].isdigit():
                nb_equipe= line.split()[0]
                nom_division=line.split()[1]
                print(nom_division)
                classement[nom_division] = {}
                current_division = nom_division
            else:
                nom_equipe, abv, *data = line.split()
                equipe_info = {
                    'ABV': abv,
                    'MJ': int(data[0]),
                    'V': int(data[1]),
                    'D':int( data[2]),
                    'DP':int( data[3]),
                    'PTS':int(data[4]),
                    'VRP':int(data[5]),
                    'BP':int(data[6]),
                    'BC':int(data[7]),
                    'DIFF':int(data[8])
                    
                }
                classement[current_division][nom_equipe] = equipe_info

    return classement


def lire_match(path):
    with open(path,'r') as file:
        grandli=[]
        for ligne in file:
            ligne=ligne.strip()
            
            
            petitli=[ligne.split()[0],ligne.split()[1]]
            grandli.append(petitli)
        return grandli

  
    

def trouver_equipe_division(equipe_abv, classement):
    for division, equipes in classement.items():
        for nom, info in equipes.items():
            if info['ABV'] == equipe_abv:
                return (nom, division)
    



def jouer_match(dif_vis, dif_dom):
    import random
    vrp = 1
    diff_total = dif_vis - dif_dom

    #if diff_total < 0:
    #    diff_total = 0

    buts_vis = round(random.normalvariate(3 +(diff_total / 100) - 0.2, 1.5))
    if buts_vis < 0:
        buts_vis = 0
    buts_dom = round(random.normalvariate(3 - (diff_total / 100), 1.5))
    if buts_dom< 0:
        buts_dom = 0

    if buts_vis == buts_dom:
        prolongation = random.choice([True, False])

        if prolongation:
            vrp = 0
            victoire_dom = random.choice([True, False])
            if victoire_dom:
                pts_vis = 1
                pts_dom = 2
                buts_dom+=1
            else:
                pts_vis = 2
                pts_dom = 1
                buts_vis+=1
        else:
            vrp = 1
            victoire_dom = random.choice([True, False])
            if victoire_dom:
                pts_vis = 1
                pts_dom = 2
            else:
                pts_vis = 2
                pts_dom = 1
    else:
        vrp = 1
        #print(buts_vis, buts_dom)
        if buts_vis > buts_dom:
            pts_vis = 2
            pts_dom = 0
        else:
            pts_vis = 0
            pts_dom = 2

    return pts_vis, pts_dom, buts_vis, buts_dom, vrp



def trier_classement(classement):
    # Parcourir chaque division dans le classement
    for division, equipes in classement.items():
        # Utiliser une liste temporaire pour trier les équipes
        equipe_list = list(equipes.items())
        
        # Trier la liste des équipes en fonction du nombre de points (PTS) en ordre descendant
        equipe_list.sort(key=lambda x: x[1]["PTS"], reverse=True)
        
        # Mettre à jour la division avec les équipes triées
        classement[division] = dict(equipe_list)


def mis_a_jour_classement(equipe, stats, division, classement):
    # Vérifier si l'équipe existe dans le classement de la division
    if division in classement and equipe in classement[division]:
        equipe_data = classement[division][equipe]

        # Mettre à jour les statistiques de l'équipe
        equipe_data["MJ"] += 1
        equipe_data["PTS"] += stats["PTS"]
        equipe_data["BP"] += stats["BP"]
        equipe_data["BC"] += stats["BC"]

        # Calculer la différence de buts
        equipe_data["DIFF"] = equipe_data["BP"] - equipe_data["BC"]

        # Déterminer le résultat du match (victoire, défaite en prolongation ou défaite)
        if stats["PTS"] == 2:
            equipe_data["V"] += 1
        elif stats["PTS"] == 1:
            equipe_data["DP"] += 1
        else:
            equipe_data["D"] += 1

    else:
        print(f"L'équipe '{equipe}' n'existe pas dans la division '{division}'.")


def simuler_rencontres(matchs, classement):
    for line in matchs:
        equipe1 = line[0]
        equipe2 = line[1]

        nom_div_eq1 = trouver_equipe_division(equipe1, classement)
        nom_div_eq2 = trouver_equipe_division(equipe2, classement)

        dif_vis = classement[nom_div_eq1[1]][nom_div_eq1[0]]['DIFF']
        dif_dom = classement[nom_div_eq2[1]][nom_div_eq2[0]]['DIFF']
        jeu = jouer_match(dif_vis, dif_dom)

        stats_vis = {
            'PTS': jeu[0],
            'BP': jeu[2],
            'BC': jeu[3],
            'VRP': jeu[4]
        }

        stats_dom = {
            'PTS': jeu[1],
            'BP': jeu[3],
            'BC': jeu[2],
            'VRP': jeu[4]
        }

        mis_a_jour_classement(nom_div_eq1[0], stats_vis, nom_div_eq1[1], classement)
        mis_a_jour_classement(nom_div_eq2[0], stats_dom, nom_div_eq2[1], classement)

    trier_classement(classement)
    return classement

def ecrire_classement(classement, nom_fichier):
    with open(nom_fichier, "w") as file:
        for division, equipes in classement.items():
            # Write division name and header line on the same line with adjusted spacing
            file.write(f"\n{division}{' ':>5}{' '.join(['ABV', 'MJ', 'V', 'D', 'DP', 'PTS', 'VRP', 'BP', 'BC', 'DIFF'])}\n")
            
            # Sort teams by points in descending order
            sorted_equipes = sorted(equipes.items(), key=lambda x: x[1]['PTS'], reverse=True)

            for eq, equipe_data in sorted_equipes:
                # Write team name with a fixed width of 13 characters
                nom_eq = eq
                file.write(f"{nom_eq:<13}")

                # Write team statistics with fixed-width columns
                for stat in ["ABV", "MJ", "V", "D", "DP", "PTS", "VRP", "BP", "BC", "DIFF"]:
                    valeur = equipe_data.get(stat, 0)
                    file.write(f"{valeur:<4}")

                # New line for the next team
                file.write('\n')

            # Two newline characters after each division
            file.write('\n\n')




# Exemple d'utilisation :
# ecrire_classement(classement, "classement_final.txt")

            



def equipes_qualifiees(classementl):

   

    equipes_series = {}

    lst_qual_est = []

    lst_qual_ouest = []

    lsch_est = []

    lsch_ouest = []

 

    for div, teams in classementl.items():

        lt = []

        if div == 'Atlantic' or div == 'Metropolitan':
            for name, stats in teams.items():
                for x, y in stats.items():
                    if x == 'PTS':
                        lt.append((name,y))
                lt.sort(key= lambda x: x[1], reverse= True)


            lst_qual_est.append(lt[:3])
            lsch_est.append(lt[3:])

 

        else:

           

            for name, stats in teams.items():
                for x, y in stats.items():
                    if x == 'PTS':
                        lt.append((name,y))

                       

                lt.sort(key= lambda x: x[1], reverse= True)

               

               

            lst_qual_ouest.append(lt[:3])

            lsch_ouest.append(lt[3:])

   

    lst_qual_est = [name[0] for div in lst_qual_est for name in div]
    lst_qual_ouest = [name[0] for div in lst_qual_ouest for name in div]  

     

    best_est = []
    for div in lsch_est:

        lt2 = []

        for teams in div:

            lt2.append(teams)

            lt2.sort(key= lambda x: x[1], reverse= True)    

        best_est.append(lt2[:2])

    best_est = [team for div in best_est for team in div]

    flag2 = 0

    best_est_vrp = []

    for team1, pts1 in best_est:

        for team2, pts2 in best_est:

            if pts1 == pts2 and team1 != team2:

                flag2 += 1

                for team3, vrp in best_est:

                    for div in classementl.values():

                        if team3 in div:

                            vrp_val = div[team3]["VRP"]

                            best_est_vrp.append((team3, vrp_val))

                           

            break

 

   

    best_est.sort(key= lambda x: x[1], reverse= True)

    best_est = best_est[:2]

   

   

   

               

    for div, teams in classementl.items():

        if best_est[0][0] in teams and best_est[1][0] in teams:

            if div == 'Metropolitan':

                lst_qual_est.insert(3, best_est[1][0])

                lst_qual_est.append(best_est[0][0])

            else:

 

                lst_qual_est.insert(3, best_est[0][0])

                lst_qual_est.append(best_est[1][0])

            break      

        elif best_est[0][0] in teams and best_est[1][0] not in teams:

            if flag2 == 1:

                best_est_vrp.sort(key= lambda x: x[1], reverse= True)

                lst_qual_est.insert(3, best_est_vrp[0][0])

                lst_qual_est.append(best_est_vrp[1][0])

            else:

                best_est.sort()

                lst_qual_est.insert(3, best_est[0][0])

                lst_qual_est.append(best_est[1][0])

            break

       

    best_ouest = []

    for div in lsch_ouest:

        lt2 = []

       

        for teams in div:

            lt2.append(teams)

            lt2.sort(key= lambda x: x[1], reverse= True)    

        best_ouest.append(lt2[:2])

    best_ouest = [team for div in best_ouest for team in div]

    flag = 0

    best_ouest_vrp = []

    for team1, pts1 in best_ouest:

        for team2, pts2 in best_ouest:

            if pts1 == pts2 and team1 != team2:

                flag += 1

                for team3, vrp in best_ouest:

                    for div in classementl.values():

                        if team3 in div:

                            vrp_val = div[team3]["VRP"]

                            best_ouest_vrp.append((team3, vrp_val))

                           

            break

   

    best_ouest.sort(key= lambda x: x[1], reverse= True)

    best_ouest = best_ouest[:2]

             

    for div, teams in classementl.items():

        if best_ouest[0][0] in teams and best_ouest[1][0] in teams:

            if div == 'Pacific':

                lst_qual_ouest.insert(3, best_ouest[1][0])

                lst_qual_ouest.append(best_ouest[0][0])

            else:

                lst_qual_ouest.insert(3, best_ouest[0][0])

                lst_qual_ouest.append(best_ouest[1][0])

            break      

        elif best_ouest[0][0] in teams and best_ouest[1][0] not in teams:

            if flag == 1:

                best_ouest_vrp.sort(key= lambda x: x[1], reverse= True)

                lst_qual_ouest.insert(3, best_ouest_vrp[1][0])

                lst_qual_ouest.append(best_ouest_vrp[0][0])

            else:

                best_ouest.sort()

                lst_qual_ouest.insert(3, best_ouest[0][0])

                lst_qual_ouest.append(best_ouest[1][0])

            break

   

    equipes_series['Est'] = lst_qual_est

    equipes_series["Ouest"] = lst_qual_ouest

    return equipes_series











if __name__ == '__main__':
    path_classement = './database/classement2019.txt'
    ligue_classement = lire_classement(path_classement)
    
    path_match = './database/matchs2019.txt'
    ligues_rencontres = lire_match(path_match)
    
    simuler_rencontres(ligues_rencontres, ligue_classement)
    
    path_classement_final = "./database/classement_final.txt"
    ecrire_classement(ligue_classement, path_classement_final)

    equipes_series = equipes_qualifiees(ligue_classement)
    print("Équipes qualifiées pour la conférence Est :", equipes_series['Est'])
    print("Équipes qualifiées pour la conférence Ouest :", equipes_series['Ouest'])
