import pandas as pd
dic_abv = {
            'V': "victoire",
            'D': "défaite",
            'DP': "défaite par prolongation",
            'PTS': "points",
            'BP': "buts marqués",
            'BC': "buts encaissés",
            'DIFF': "différence de buts"
        }

division = ["Atlantic","Metropolitan","Central","Pacific"]

def lire_classement(path):
    classement = {}
    with open(path, 'r') as file:
        current_division = None
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line[0].isdigit():
                nb_equipe, nom_division = line.split()[:2]
                current_division = nom_division
                classement[current_division] = {}
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
                    'DIFF':int(data[8]),
                    'DIV': current_division
                }
                classement[current_division][nom_equipe] = equipe_info

    return classement



def creer_df(classement):
    rows = {}
    for eq in classement.values():
        for current_division, data in eq.items():
            rows[current_division] = data
           

    
    df = pd.DataFrame.from_dict(rows, orient='index')
    
    return df


def df_extraite_divison(df, division):
    # Filtrer les données pour obtenir uniquement les équipes de la division spécifiée
    df_division = df[df['DIV'] == division].copy()
    
    # Supprimer la colonne "DIV" pour éviter les informations redondantes
    df_division = df_division.drop(columns=['DIV'])
    
    return df_division

def df_sort_type(df, column, ascending=True):
    new_df = df.sort_values(by=[column], ascending=ascending)
    return new_df



def df_summary_inf(df):
    team=[]
    stats=[]
    for i in range(len(division)+1):
        if i<4:
            new_df=df_extraite_divison(df, division[i])
            for cle_s in dic_abv.keys():
                alt_df=df_sort_type(new_df, cle_s, ascending=False)
                stats.append(alt_df.at[alt_df.index[0],cle_s])
                team.append(alt_df.index[0])
        else:
            for league in dic_abv.keys():
                alt_df=df_sort_type(df,league,ascending=False)
                stats.append(alt_df.at[alt_df.index[0],league])
                team.append(alt_df.index[0])
    i=0
    w=0
    while i<34:
        for index, d in enumerate(list(dic_abv.values())):
            if index==0:
                if w<4:
                    print(f"Stats division {division[w]}:")
                else:
                    print("Stats ligue:")
                print(f"\t l'équipe qui a le plus de victoire est {team[i]} avec {stats[i]} {d}")
                i+=1
            elif index==1:
                print(f"\t l'équipe qui a le plus de défaite est {team[i]} avec {stats[i]} {d}")
                i+=1
            elif index==2:
                print(f"\t l'équipe qui a le plus de défaite par prolongation est {team[i]} avec {stats[i]} {d}")
                i+=1
            elif index==3:
                print(f"\t l'équipe qui a le plus de points est {team[i]} avec {stats[i]} {d}")
                i+=1

            elif index==4:
                print(f"\t l'équipe qui a le plus de buts marqués est {team[i]} avec {stats[i]} {d}")
                i+=1
            elif index==5:
                print(f"\t l'équipe qui a le plus de buts encaissés est {team[i]} avec {stats[i]} {d}")
                i+=1
            else:
                print(f"\t l'équipe qui a le plus de différence de buts est {team[i]} avec {stats[i]} {d}\n")
                i+=1
                w+=1


if __name__ == '__main__':
    path = './database/classement2019.txt'
    ligue_classement = lire_classement(path)

    nhl_df = creer_df(ligue_classement)

    print(nhl_df)
    print("\n")

    for div in division:
        print(df_extraite_divison(nhl_df, div))
        print("\n")


    nhl_df_sort_by_pts = df_sort_type(nhl_df, "PTS", False)
    print(nhl_df_sort_by_pts)
    print("\n")

    nhl_div_df = df_extraite_divison(nhl_df, "Atlantic")
    nhl_div_df_sort_by_v = df_sort_type(nhl_div_df, "V", True)
    print(nhl_div_df_sort_by_v)

    print("\n")
    df_summary_inf(nhl_df)
