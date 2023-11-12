import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from Partie_2 import *



def df_summary_divison(df, type_sort, ascending):
    liste=df['DIV'].unique()
    figure=plt.figure()
    i=1
    for division in liste:
        titre=f"Classement des equipes de la division {division} par nombre de {dic_abv[type_sort]}"
        div=df_extraite_divison(df,division)
        sort=df_sort_type(div, type_sort,ascending)
        a=figure.add_subplot(2,2,i)
        sns.barplot(data=div, x=type_sort,y=sort.index,palette=("Spectral"))
        a.set_title(titre)
        x_ax=f"Nombre de{dic_abv[type_sort]} "
        plt.xlabel(x_ax)
        plt.ylabel(None)
        i+=1
    plt.subplots_adjust(left=None,bottom=None,right=None,top=1,wspace=0.5,hspace=0.25)
    return plt.show()
def df_summary_league(df, criteria, ascending):

    # Tri du DataFrame en fonction du critère spécifié
    df_sorted = df_sort_type(df, criteria, ascending)
    
    # Sélection des 10 premières équipes
    df_top10 = df_sorted[:10]
    
    # Extraction des noms d'équipes et du critère pour l'axe x et y du graphique
    teams = df_top10.index
    axe = f"Nombre de {criteria}"
    titre = f"Classement des 10 équipes par nombre de {criteria}"
    
    # Création du graphique en barres avec Seaborn
    sns.barplot(data=df_top10, x=df_top10[criteria], y=teams, palette="Spectral").set(title=titre)
    
    # Ajout de labels
    plt.xlabel(axe)
    plt.ylabel(None)  # Pas de label pour l'axe y
    
    # Affichage du graphique
    plt.show()
    

def df_groupby_div(df):
    group=df.groupby(by=['DIV']).sum()
    return group

def df_secteur_div(df, type_data, ascendant):
    alt=df.sort_values(by=[type_data],ascending=ascendant)
    sorted_df=alt[:10]
    f=px.pie(sorted_df,values=sorted_df[type_data],names=sorted_df['DIV'],color_discrete_sequence=px.colors.sequential.RdBu, hole=0.3)
    f.show()


if __name__ == '__main__':
    path=r"C:\Users\chris\Desktop\classement2019.txt"
    
    ligue_classement = lire_classement(path)
    nhl_df = creer_df(ligue_classement)

    df_summary_divison(nhl_df,"PTS", False)
    df_summary_divison(nhl_df,"V", False)
    df_summary_divison(nhl_df,"BP", False)

    df_summary_league(nhl_df,"PTS", False)
    df_summary_league(nhl_df,"V", False)
    df_summary_league(nhl_df,"DIFF", False)
    df_summary_league(nhl_df,"DIFF", True)

    df_secteur_div(nhl_df, "PTS", False)
    df_secteur_div(nhl_df, "PTS", True)

    df_secteur_div(nhl_df, "V", False)
    df_secteur_div(nhl_df, "V", True)
