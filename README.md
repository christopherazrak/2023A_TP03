<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Polytechnique_Montr%C3%A9al_logo.jpg" />
</p>

# TP03 : Librairies scientifiques et graphiques
- [Directives particulières](#directives)
- [Introduction](#Introduction)
- [Objectifs](#Objectif)
- [Description: La dynamique proie-prédateur](#Description)
- [Déroulement de la simulation](#simulation)
- [Module animal](#animal)
- [Module grille animaux](#animaux)
- [Module simulation](#animaux)
- [Barème](#bareme)
- [Annexe: Guide et normes de codage](#annexe)

:alarm_clock: [[Date de remise le dimanche 6 novembre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20231106T235959&p0=165&font=cursive)

## Directives particulières <a name="directives"></a>
* Respecter [guide de codage](https://github.com/INF1007-Gabarits/Guide-codage-python) et les normes pep8;
* Noms de variables et fonctions adéquats (concis, compréhensibles);  
* Pas de librairies externes autres que celles déjà importées;

## 1. Introduction
<div align="justify">
L’analyse des données fait partie des disciplines les plus prisées de nos jours. Outil stratégique au sein des organisations, elle permet entre autres de mieux comprendre des événements qui se produisent avec les facteurs qui les favorisent, ou encore de mesurer l’impact d’une opération ou d’une politique grâce à des indicateurs de performance.
</div>

## 2. Objectifs du laboratoire

<div align="justify">
  
- **Maîtrise des notions de base et structures de données** : Renforcer la compréhension et l'application des concepts fondamentaux et des structures de données en Python.
- **Gestion de fichiers** : Apprendre à lire des données depuis un fichier texte et à écrire des données dans un fichier texte en respectant un format spécifié.
- **Respect des exigences de programmation** : Veiller à suivre les meilleures pratiques de programmation et à respecter les spécifications fournies.
- **Utilisation de Dataframes** : Créer et manipuler des Dataframes, structures de données essentielles pour l'analyse de données.
- **Analyse avec les bibliothèques scientifiques** : Exploiter des bibliothèques telles que pandas, numpy, matplotlib et autres pour effectuer une analyse complète des données.
</div>

## 3. Description du problème: 

<div align="justify">
  
L'objectif de ce laboratoire est de simuler la fin de la saison 2019 de la Ligue Nationale de Hockey (LNH). Selon le site de [statistiques sportives](http://www.sportsclubstats.com/NHL2.html), en date du 5 février 2019, le Club de Hockey Canadien (CH) de Montréal possédait une probabilité de 84.6% de se qualifier parmi les 16 équipes (sur 31) pour les séries éliminatoires de cette saison. Mais comment ce site arrive-t-il à une telle prédiction? Il effectue plusieurs millions de simulations aléatoires des matchs restants chaque jour, puis détermine la probabilité basée sur les résultats obtenus.
</div>

### 3.1 Votre mission:

<div align="justify">
  
1. Créer un programme capable de simuler la fin de la saison en se basant sur des données fournies et des fonctions aléatoires.
2. Effectuer une étude détaillée et produire des visualisations sur les points suivants:
    - Équipes ayant marqué le plus et le moins de buts.
    - Équipes ayant accumulé le plus et le moins de points.
    - Équipes ayant le plus grand et le plus petit nombre de victoires et de défaites.
    - Analyse par division sur:
        - Le pourcentage de buts marqués.
        - Le pourcentage de points accumulés.
        - Le pourcentage de victoires et de défaites.
</div>

### 3.2 Données:
<div align="justify">
  
- `classement2019.txt`: Liste des 31 équipes (réparties en 4 divisions) avec leurs statistiques jusqu'au 4 février.
- `matchs2019.txt`: Liste des matchs restants à partir du 5 février.
</div>

### 3.3 Mécanisme de simulation:

<div align="justify">
  
- Les résultats des matchs sont déterminés aléatoirement avec la fonction `md_randnormal()`. Cette fonction génère des nombres suivant une distribution normale basée sur une moyenne donnée, permettant d'avantager une équipe par rapport à une autre selon leurs performances.
- L'avantage du terrain sera également pris en compte pour l'équipe jouant à domicile.
- La conclusion de chaque match (temps règlementaire, prolongation ou tirs de barrage) est déterminée aléatoirement, influençant les points accordés aux équipes.</div>

<div align="justify">Une fois tous les matchs simulés, le classement des équipes est mis à jour. Le processus est répété plusieurs millions de fois pour obtenir la probabilité de qualification aux séries éliminatoires pour chaque équipe.</div>

## 4. Déroulement d'une saison de la LNH

<div align="justify"> La LNH se compose de 31 équipes réparties en 4 divisions. Deux divisions (Atlantique et Métropolitaine) constituent la conférence de l'Est, tandis que les deux autres (Centrale et Pacifique) forment la conférence de l'Ouest. Chaque équipe joue 82 matchs lors de la saison régulière, et les points sont attribués selon le résultat du match:</div>

<div align="justify">

- **Victoire régulière (REG):** 2 points pour le gagnant, 0 pour le perdant.
- **Prolongation (PROL)**: 2 points pour le gagnant, 1 pour le perdant.
- **Fusillade (FUS)**: 2 points pour le gagnant, 1 pour le perdant. Néanmoins, cette victoire n'est pas comptabilisée dans la statistique VRP.</div>

<div align="justify">À la fin de la saison, les équipes sont classées en fonction de leurs points. En cas d'égalité, la statistique VRP est utilisée comme critère de départage. Les trois meilleures équipes de chaque division sont automatiquement qualifiées, et les deux places restantes (wildcards) sont attribuées aux meilleures équipes non encore qualifiées. Ces wildcards peuvent venir de la même division. On applique le même protocole de sélection dans l’autre conférence et on obtient ainsi la liste des 16 équipes qualifiées.</div>


## 5. Partie 1: Lire et construire la base de données
### 5.1. lire_classement() 

<div align="justify">

  Cette fonction est destinée à lire la base de données depuis le fichier `classement2019.txt`.</div>

<div align="justify">

  Le fichier `classement2019.txt` est organisé en quatre sections, chacune représentant une division. Par exemple, une ligne d'en-tête typique pourrait ressembler à `8 Atlantic`, où `8` indique le nombre d'équipes et `Atlantic` est le nom de la division. Après avoir lu ces informations, vous devez ignorer le reste de la ligne d'en-tête qui contient les titres des colonnes de données.</div>

<div align="justify">

  Ensuite, en utilisant une boucle basée sur le nombre d'équipes, chaque équipe est lue ligne par ligne, capturant 11 données pour chaque équipe. Une fois que les 4 divisions ont été lues, le fichier est fermé et la fonction retourne un dictionnaire qui encapsule les quatre divisions, avec chaque division contenant entre sept ou huit équipes.</div>

- **Type de retour:**
  - Le dictionnaire principal est divisé par divisions.
  - Un dictionnaire dont les clés sont les noms des divisions et les valeurs sont des dictionnaires.
  - Chaque sous-dictionnaire correspond à une équipe et contient des paires clé-valeur pour différentes informations sur l'équipe.

- **Exemple:**
```python
 { 
   'NOM DIVISION': {
     'NOM EQUIPE':{
        'ABV': '',
        # ...
        # les autres colonnes du fichier
     },
     'NOM EQUIPE':{
        'ABV': '',
        # ...
        # les autres colonnes du fichier
     },
     # Toutes les autres équipes de la division
 }
```

 ### 5.2. lire_match()
<div align="justify">
  
Cette fonction est chargée de lire les informations relatives aux matchs à partir du fichier `matchs2019.txt`.</div>

<div align="justify">

La première ligne du fichier `matchs2019.txt` indique le nombre total de matchs, par exemple `467`. Après avoir lu cette information, la fonction parcourt chaque ligne du fichier pour identifier les deux équipes qui joueront dans un match spécifique. Par exemple, une entrée telle que `TOR MTL` signifie que l'équipe de `Toronto` joue en déplacement contre celle de `Montréal`. Chaque ligne du fichier correspond donc à un match distinct et est transformée en une sous-liste de deux éléments dans la liste retournée.</div>

- **Type de retour:**
  - Une liste de listes, où chaque sous-liste contient deux chaînes de caractères (des acronymes).
  - Chaque sous-liste représente un match distinct.
  - Le premier acronyme de la sous-liste désigne l'équipe visiteuse.
  - Le deuxième acronyme de la sous-liste représente l'équipe à domicile.

- **Exemple:**
```python
    [['ANA', 'TOR'], ['L-A', 'NYR'], ...]
```


 ### 5.3. trouver_equipe_division(equipe_abv, classement)
 
 <div align="justify">
 
Cette fonction est conçue pour identifier le nom de l'équipe et sa division associée à partir de son acronyme.
 </div>

 <div align="justify">

Dans le processus de recherche d'une équipe à partir de son acronyme au sein du dictionnaire `classement`, chaque division est minutieusement parcourue. Au sein de chaque division, chaque équipe est examinée en détail, et son acronyme est comparé à celui spécifié par le paramètre `equipe_abv`. Lorsqu'une correspondance parfaite est identifiée, c'est-à-dire que les deux acronymes concordent parfaitement, la fonction renvoie alors le nom précis de la division ainsi que le nom intégral de l'équipe concernée.
   </div>
 
- **Paramètres:**
  - `equipe_abv`: Une chaîne de caractères représentant l'acronyme de l'équipe à rechercher.
  - `classement`: Le dictionnaire contenant les informations des divisions et des équipes.
    
- **Type de retour:**
  - Un tuple contenant deux chaînes de caractères : le nom de la division et le nom de l'équipe.

- **Exemple:**
```python
classement = {
    "Pacific Division": {
        "Anaheim Ducks": {
            "ABV": "ANA",
            # autres détails de l'équipe...
        },
        # autres équipes...
    },
    # autres divisions...
}

resultat = trouver_equipe_division("ANA", classement)
print(resultat)  # ("Pacific Division", "Anaheim Ducks")
```
 
### 5.4. jouer_match(dif_vis, dif_dom)

<div align="justify">
  
La fonction `jouer_match` simule un match entre deux équipes, l'une à domicile et l'autre visiteuse, en se basant sur les différences de buts de chaque équipe accumulées au cours de la saison. La fonction calcule le nombre de buts que chaque équipe marque pendant ce match simulé et détermine si la victoire est obtenue en temps régulier, en prolongation ou en fusillade.

La simulation utilise la distribution normale de Python pour générer un nombre aléatoire de buts basé sur une moyenne et un écart-type. La moyenne de base est fixée à 3 buts par match, avec un écart-type de 1.5. Cette moyenne est ajustée pour tenir compte de la différence de buts entre les deux équipes, donnant un avantage à l'équipe statistiquement la plus performante. Une pénalité fixe de 0.2 est systématiquement soustraite de la moyenne de l'équipe visiteuse, pour simuler l'avantage à domicile.

Les équations pour le calcul des buts sont :

<p align="center">
<img src="https://latex.codecogs.com/svg.image?\begin{align*}\text{buts\_vis}&=\text{round}\left(\text{random.normalvariate}\left(3&plus;\frac{\text{diff\_total}}{100}-0.2,1.5\right)\right)\\\text{buts\_dom}&=\text{round}\left(\text{random.normalvariate}\left(3-\frac{\text{diff\_total}}{100},1.5\right)\right)\end{align*}" /></p>

où `diff_total = dif_vis - dif_dom`.

Les valeurs générées sont arrondies à l'entier le plus proche. Si une valeur est négative, elle est ramenée à zéro.

Si une équipe marque plus de buts que l'autre après cette simulation, elle gagne le match en temps régulier et l'indicateur `vrp` est fixé à 1. Si les deux équipes ont le même nombre de buts, une prolongation ou une fusillade est simulée. Si le match est décidé en fusillade, l'indicateur `vrp` est fixé à 0.
</div>

<p align="center">
    <img src="Images/img_01.svg">
</p>

- **Paramètres:**
  - `dif_vis`: Différence de buts de l'équipe visiteur sur la saison.
  - `dif_dom`: Différence de buts de l'équipe domicile sur la saison.
    
- **Type de retour:**
  - `pts_vis`: Points gagnés par l'équipe visiteur.
  - `pts_dom`: Points gagnés par l'équipe domicile.
  - `but_vis`: Nombre de buts marqués par l'équipe visiteur.
  - `but_dom`: Nombre de buts marqués par l'équipe domicile.
  - `vrp`: Indicateur de victoire en temps régulier ou en prolongation (1) ou en fusillade (0).
 
### 5.5. trier_classement(classement)

<div align="justify">
  
La fonction `trier_classement` organise les équipes au sein de chaque division de manière descendante selon leur nombre total de points.

Chaque division doit être triée indépendamment des autres. La fonction modifie directement le dictionnaire `classement` sans rien retourner. Une fois la fonction exécutée, en consultant le dictionnaire `classement`, vous devriez voir les équipes de chaque division classées de la plus performante à la moins performante, basées sur leur nombre de points.

Il est important de noter que dans le cas où deux équipes ont le même nombre de points dans une division, le critère de tri supplémentaire peut être basé sur d'autres statistiques, comme le nombre de buts pour ou contre, mais cela dépendra de l'implémentation spécifique et des règles de la ligue.

- **Paramètres:**
  - `classement` (dict): Un dictionnaire de dictionnaires représentant le classement actuel des équipes par division. La structure du dictionnaire est détaillée dans les fonctions précédentes, notamment `mis_a_jour_classement`.

</div>
 
### 5.6. mis_a_jour_classement(equipe, stats, division, classment) 

<div align="justify">

La fonction `mis_a_jour_classement` met à jour les statistiques d'une équipe donnée dans un classement de division après la conclusion d'un match. Elle utilise les statistiques fournies pour augmenter le nombre de points, le nombre de buts marqués, le nombre de buts encaissés, et détermine également si la victoire a été obtenue en temps régulier ou en prolongation.

- **Paramètres:**
  - `equipe`: Le nom de l'équipe dont les statistiques doivent être mises à jour.
  - `stats`: Un dictionnaire contenant les statistiques du match récent. Il a la structure suivante :
     ```python
     {
         'PTS': int,  # Nombre de points gagnés dans le match.
         'BP': int,  # Buts marqués par l'équipe lors du match.
         'BC': int,  # Buts encaissés par l'équipe lors du match.
         'VRP': int  # Valeur 1 si victoire en temps régulier ou en prolongation, 0 si en fusillade.
     }
     ```
  - `division`: Le nom de la division à laquelle appartient l'équipe.
  - `classment`: Un dictionnaire de dictionnaires représentant le classement actuel des équipes par division.

</div>


### 5.7. simuler_rencontres(matchs, classement)

<div align="justify">
  
La fonction `simuler_rencontres` est responsable de la simulation d'une série de rencontres entre différentes équipes et de la mise à jour du classement en conséquence.

Après avoir extrait le nom et la division des deux équipes impliquées dans chaque match de la liste `matchs`, la fonction simule le résultat du match en utilisant `jouer_match`. Suite à cette simulation, vous devez créer deux dictionnaires, `stats_vis` et `stats_dom`, pour contenir les statistiques de la rencontre pour chaque équipe. Ces dictionnaires doivent respecter le format suivant :
  ```python
  {
      'PTS': int,  # Nombre de points gagnés dans le match.
      'BP': int,  # Buts marqués par l'équipe lors du match.
      'BC': int,  # Buts encaissés par l'équipe lors du match.
      'VRP': int  # Valeur 1 si victoire en temps régulier ou en prolongation, 0 si en fusillade.
  }
  ```
Ces dictionnaires sont ensuite utilisés pour mettre à jour le classement général des équipes en utilisant la fonction `mis_a_jour_classement()`.

Après avoir simulé tous les matchs et mis à jour le classement pour chaque match, la fonction `trier_classement(classement)` est appelée pour s'assurer que le classement des équipes au sein de chaque division est organisé de manière descendante selon leur nombre total de points.

- **Paramètres :**
  - `matchs`: Une liste de matchs à simuler. Chaque match est représenté par une liste contenant le nom et la division des deux équipes impliquées.
  - `classement`: Un dictionnaire de dictionnaires représentant le classement actuel des équipes par division.

</div>


### 8. ecrire_classement(classement)

<div align="justify">

La fonction `ecrire_classement` a pour objectif de sauvegarder le classement final des équipes dans un fichier texte, en l'occurrence "classement_final.txt". Pour assurer la cohérence et la lisibilité des données, il est essentiel que le format de sortie respecte celui du fichier "classement2019.txt".

La structure du fichier "classement_final.txt" doit être organisée de manière à lister chaque division, suivie par les équipes de cette division classées par ordre décroissant selon leurs points. 

Le format du classement doit suivre le modèle suivant:

```
            ABV MJ  V   D   DP  PTS VRP BP  BC  DIFF
Tampa_Bay   T-B 52  39  11  2   80  35  205 146 +59
Toronto     TOR 51  31  17  3   65  31  179 145 +34
Montreal    MTL 53  29  18  6   64  27  160 155 +5
Boston      BOS 52  28  17  7   63  27  149 135 +14
Buffalo     BUF 51  25  20  6   56  22  148 156 -8
Florida     FLA 50  21  21  8   50  19  156 175 -19
Detroit     DET 53  21  25  7   49  19  150 174 -24
Ottawa      OTT 52  19  28  5   43  19  159 194 -35
```

Chaque ligne après l'en-tête représente une équipe, avec des détails:
  - Nom complet
  - Abréviation
  - Nombre de matchs joués (MJ)
  - Nombre de victoires (V),
  - Nombre de défaites (D),
  - Nombre de défaites en prolongation (DP),
  - Nombre de points totaux (PTS),
  - Nombre de victoires en temps régulier ou en prolongation (VRP),
  - Nombre de buts marqués (BP),
  - Nombre de buts concédés (BC)
  - La différence de buts (DIFF).

- **Paramètre :**
  - `classement`: Un dictionnaire de dictionnaires représentant le classement final des équipes par division.

</div>

## 6. Partie 2: Construire la base de données
### 6.1. creer_df(classement)

<div align="justify">

La fonction `creer_df` sert à transformer un dictionnaire contenant les informations des équipes pour chaque division en un dataframe. Cette transformation est réalisée grâce à l'utilisation de la bibliothèque Pandas.

- **Paramètre:**
  - `classement` : Un dictionnaire contenant les informations des équipes pour chaque division.
  

- **Valeur de retour :**
  - Un dataframe contenant les informations de chaque équipe.

- **Lien utile :** 
  - [Conversion d'un dictionnaire en dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html)
    
En utilisant la fonction, vous devriez obtenir un résultat semblable à :

```python
nhl_df = creer_df(ligue_classement)
print(nhl_df)
```

```
                  ABV  MJ   V   D  DP  PTS  VRP   BP   BC  DIFF           DIV
    Buffalo       BUF  51  25  20   6   56   22  148  156    -8      Atlantic
    Toronto       TOR  51  31  17   3   65   31  179  145    34      Atlantic
    Montreal      MTL  53  29  18   6   64   27  160  155     5      Atlantic
    Boston        BOS  52  28  17   7   63   27  149  135    14      Atlantic
    Detroit       DET  53  21  25   7   49   19  150  174   -24      Atlantic
    Tampa_Bay     T-B  52  39  11   2   80   35  205  146    59      Atlantic
    Florida       FLA  50  21  21   8   50   19  156  175   -19      Atlantic
    Ottawa        OTT  52  19  28   5   43   19  159  194   -35      Atlantic
    Washington    WAS  52  28  18   6   62   25  175  166     9  Metropolitan
    Columbus      CLB  51  28  20   3   59   28  163  159     4  Metropolitan
    NY_Islanders  NYI  51  30  15   6   66   28  151  125    26  Metropolitan
    Pittsburgh    PIT  52  28  18   6   62   27  183  160    23  Metropolitan
    Philadelphia  PHI  52  23  23   6   52   21  151  176   -25  Metropolitan
    NY_Rangers    NYR  51  22  22   7   51   17  145  171   -26  Metropolitan
    New_Jersey    N-J  51  20  24   7   47   19  152  173   -21  Metropolitan
    Carolina      CAR  52  25  21   6   56   24  148  155    -7  Metropolitan
    Winnipeg      WIN  52  34  16   2   70   32  185  146    39       Central
    Colorado      COL  51  22  21   8   52   22  170  167     3       Central
    St-Louis      STL  50  23  22   5   51   23  143  151    -8       Central
    Dallas        DAL  52  27  21   4   58   27  133  130     3       Central
    Minnesota     MIN  52  26  22   4   56   25  146  149    -3       Central
    Chicago       CHI  53  20  24   9   49   19  167  196   -29       Central
    Nashville     NAS  54  31  19   4   66   30  166  139    27       Central
    Los-Angeles   L-A  51  20  27   4   44   19  116  154   -38       Pacific
    Calgary       CAL  53  34  14   5   73   34  197  152    45       Pacific
    Vancouver     VAN  52  24  22   6   54   23  152  162   -10       Pacific
    Arizona       ARI  51  23  23   5   51   21  134  145   -11       Pacific
    San-Jose      SJS  53  30  16   7   67   30  190  169    21       Pacific
    Vegas         VGK  54  29  21   4   62   28  160  148    12       Pacific
    Edmonton      EDM  52  23  24   5   51   20  151  172   -21       Pacific
    Anaheim       ANA  52  21  22   9   51   18  123  162   -39       Pacific
```
</div>

### 6.2. df_extraite_divison(df, division)

<div align="justify">

La fonction `df_extraite_divison` a pour but d'extraire et de retourner un DataFrame réduit, contenant seulement les équipes d'une division donnée. La colonne "DIV", qui indique la division des équipes, sera supprimée du DataFrame résultant pour ne pas avoir d'informations redondantes.


- **Paramètre:**
  - `df`: Un DataFrame Pandas qui contient les informations de toutes les équipes de la ligue. Ce DataFrame possède une colonne "DIV" qui indique la division de chaque équipe.
  - `division`: Une chaîne de caractères représentant le nom de la division dont les équipes doivent être extraites du DataFrame original.

- **Type de retour:**
  - Un DataFrame contenant uniquement les équipes de la division spécifiée. Ce DataFrame ne possède pas la colonne "DIV".

- **Lien utile :** 
  - Filtrer les données avec Pandas : [Lien](https://pandas.pydata.org/docs/user_guide/indexing.html)
  - Supprimer une colonne avec Pandas : [Lien](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)

</div>

- **Exemple:**
  ```python
  for div in division:
      print(df_extraite_divison(nhl_df, div))
      print("\n")
  ```

  ```
               ABV  MJ   V   D  DP  PTS  VRP   BP   BC  DIFF
    Buffalo    BUF  51  25  20   6   56   22  148  156    -8
    Toronto    TOR  51  31  17   3   65   31  179  145    34
    Montreal   MTL  53  29  18   6   64   27  160  155     5
    Boston     BOS  52  28  17   7   63   27  149  135    14
    Detroit    DET  53  21  25   7   49   19  150  174   -24
    Tampa_Bay  T-B  52  39  11   2   80   35  205  146    59
    Florida    FLA  50  21  21   8   50   19  156  175   -19
    Ottawa     OTT  52  19  28   5   43   19  159  194   -35
    
    
                  ABV  MJ   V   D  DP  PTS  VRP   BP   BC  DIFF
    Washington    WAS  52  28  18   6   62   25  175  166     9
    Columbus      CLB  51  28  20   3   59   28  163  159     4
    NY_Islanders  NYI  51  30  15   6   66   28  151  125    26
    Pittsburgh    PIT  52  28  18   6   62   27  183  160    23
    Philadelphia  PHI  52  23  23   6   52   21  151  176   -25
    NY_Rangers    NYR  51  22  22   7   51   17  145  171   -26
    New_Jersey    N-J  51  20  24   7   47   19  152  173   -21
    Carolina      CAR  52  25  21   6   56   24  148  155    -7
    
    
               ABV  MJ   V   D  DP  PTS  VRP   BP   BC  DIFF
    Winnipeg   WIN  52  34  16   2   70   32  185  146    39
    Colorado   COL  51  22  21   8   52   22  170  167     3
    St-Louis   STL  50  23  22   5   51   23  143  151    -8
    Dallas     DAL  52  27  21   4   58   27  133  130     3
    Minnesota  MIN  52  26  22   4   56   25  146  149    -3
    Chicago    CHI  53  20  24   9   49   19  167  196   -29
    Nashville  NAS  54  31  19   4   66   30  166  139    27
    
    
                 ABV  MJ   V   D  DP  PTS  VRP   BP   BC  DIFF
    Los-Angeles  L-A  51  20  27   4   44   19  116  154   -38
    Calgary      CAL  53  34  14   5   73   34  197  152    45
    Vancouver    VAN  52  24  22   6   54   23  152  162   -10
    Arizona      ARI  51  23  23   5   51   21  134  145   -11
    San-Jose     SJS  53  30  16   7   67   30  190  169    21
    Vegas        VGK  54  29  21   4   62   28  160  148    12
    Edmonton     EDM  52  23  24   5   51   20  151  172   -21
    Anaheim      ANA  52  21  22   9   51   18  123  162   -39
  ```

### 6.3. df_sort_type(df, column, ascending):

<div align="justify">
  
La fonction `df_sort_type` permet de trier un DataFrame selon une colonne spécifique. La direction du tri (croissant ou décroissant) est également spécifiée en tant que paramètre.

- **Paramètre:**
  - `df`: DataFrame Pandas qui contient les informations de toutes les équipes de la ligue.
  - `column`: Une chaîne de caractères représentant le nom de la colonne selon laquelle le DataFrame doit être trié.
  - `ascending`: Un booléen qui détermine la direction du tri. Si `True`, le tri est effectué dans l'ordre croissant; si `False`, le tri est effectué dans l'ordre décroissant. Par défaut, la valeur est `True`.

- **Type de retour:**
  - Un DataFrame Pandas trié selon la colonne spécifiée et dans la direction d'ordre donnée.


- **Lien utile :** 
  - Trier un DataFrame avec Pandas: [Lien](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
</div>

- **Exemple:**
  ```python
  nhl_df_sort_by_pts = df_sort_type(nhl_df, "PTS", False)
  print(nhl_df_sort_by_pts)
  print("\n")
  ```
  
  ```
                  ABV  MJ   V   D  DP  PTS  VRP   BP   BC  DIFF           DIV
    Tampa_Bay     T-B  52  39  11   2   80   35  205  146    59      Atlantic
    Calgary       CAL  53  34  14   5   73   34  197  152    45       Pacific
    Winnipeg      WIN  52  34  16   2   70   32  185  146    39       Central
    San-Jose      SJS  53  30  16   7   67   30  190  169    21       Pacific
    NY_Islanders  NYI  51  30  15   6   66   28  151  125    26  Metropolitan
    Nashville     NAS  54  31  19   4   66   30  166  139    27       Central
    Toronto       TOR  51  31  17   3   65   31  179  145    34      Atlantic
    Montreal      MTL  53  29  18   6   64   27  160  155     5      Atlantic
    Boston        BOS  52  28  17   7   63   27  149  135    14      Atlantic
    Vegas         VGK  54  29  21   4   62   28  160  148    12       Pacific
    Washington    WAS  52  28  18   6   62   25  175  166     9  Metropolitan
    Pittsburgh    PIT  52  28  18   6   62   27  183  160    23  Metropolitan
    Columbus      CLB  51  28  20   3   59   28  163  159     4  Metropolitan
    Dallas        DAL  52  27  21   4   58   27  133  130     3       Central
    Buffalo       BUF  51  25  20   6   56   22  148  156    -8      Atlantic
    Minnesota     MIN  52  26  22   4   56   25  146  149    -3       Central
    Carolina      CAR  52  25  21   6   56   24  148  155    -7  Metropolitan
    Vancouver     VAN  52  24  22   6   54   23  152  162   -10       Pacific
    Colorado      COL  51  22  21   8   52   22  170  167     3       Central
    Philadelphia  PHI  52  23  23   6   52   21  151  176   -25  Metropolitan
    St-Louis      STL  50  23  22   5   51   23  143  151    -8       Central
    NY_Rangers    NYR  51  22  22   7   51   17  145  171   -26  Metropolitan
    Arizona       ARI  51  23  23   5   51   21  134  145   -11       Pacific
    Edmonton      EDM  52  23  24   5   51   20  151  172   -21       Pacific
    Anaheim       ANA  52  21  22   9   51   18  123  162   -39       Pacific
    Florida       FLA  50  21  21   8   50   19  156  175   -19      Atlantic
    Chicago       CHI  53  20  24   9   49   19  167  196   -29       Central
    Detroit       DET  53  21  25   7   49   19  150  174   -24      Atlantic
    New_Jersey    N-J  51  20  24   7   47   19  152  173   -21  Metropolitan
    Los-Angeles   L-A  51  20  27   4   44   19  116  154   -38       Pacific
    Ottawa        OTT  52  19  28   5   43   19  159  194   -35      Atlantic
  ```

  ```python
  nhl_div_df = df_extraite_divison(nhl_df, "Atlantic")
  nhl_div_df_sort_by_v = df_sort_type(nhl_div_df, "V", True)
  print(nhl_div_df_sort_by_v)
  ```    
  
  ```    
               ABV  MJ   V   D  DP  PTS  VRP   BP   BC  DIFF
    Ottawa     OTT  52  19  28   5   43   19  159  194   -35
    Detroit    DET  53  21  25   7   49   19  150  174   -24
    Florida    FLA  50  21  21   8   50   19  156  175   -19
    Buffalo    BUF  51  25  20   6   56   22  148  156    -8
    Boston     BOS  52  28  17   7   63   27  149  135    14
    Montreal   MTL  53  29  18   6   64   27  160  155     5
    Toronto    TOR  51  31  17   3   65   31  179  145    34
    Tampa_Bay  T-B  52  39  11   2   80   35  205  146    59
  ```



## 7. Partie 3: Analyse des données

## 8. Barème /100 <a name="bareme"></a>

|**Nom des fonctions**|**Nombre de points attribuer**|
| :- | :- |
|creer_animal                              | 2  |


## Annexe: Guide et normes de codage <a name="annexe"></a>
- [Le guide maison](https://github.com/INF1007-Gabarits/Guide-codage-python) de normes supplémentaires à respecter
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. 
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)


