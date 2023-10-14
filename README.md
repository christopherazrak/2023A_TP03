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


## Partie 1: Lire et construire la base de données
### 1. lire_classement() 

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

- **Exemple de format de retour :**
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

 ### 2. lire_match() /3
<div align="justify">
  
Cette fonction est chargée de lire les informations relatives aux matchs à partir du fichier `matchs2019.txt`.</div>

<div align="justify">

La première ligne du fichier `matchs2019.txt` indique le nombre total de matchs, par exemple `467`. Après avoir lu cette information, la fonction parcourt chaque ligne du fichier pour identifier les deux équipes qui joueront dans un match spécifique. Par exemple, une entrée telle que `TOR MTL` signifie que l'équipe de `Toronto` joue en déplacement contre celle de `Montréal`. Chaque ligne du fichier correspond donc à un match distinct et est transformée en une sous-liste de deux éléments dans la liste retournée.</div>

- **Type de retour:**
  - Une liste de listes, où chaque sous-liste contient deux chaînes de caractères (des acronymes).
  - Chaque sous-liste représente un match distinct.
  - Le premier acronyme de la sous-liste désigne l'équipe visiteuse.
  - Le deuxième acronyme de la sous-liste représente l'équipe à domicile.

- **Exemple de format de retour :**
```python
    [['ANA', 'TOR'], ['L-A', 'NYR'], ...]
```


 ### 3. trouver_equipe_division(equipe_abv, classement) /2
 
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

- **Exemple de format de retour :**
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
 
### 4. jouer_match(dif_vis, dif_dom) /4

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
 
 ### 5. trier_classement(classement) /2
 À l'aide du dictionnaire classement et de l'abbréviation de l'équipe (string), trouvez et retournez le nom de l'équipe et sa division.
 
 Pour chaque division, classer les équipes selon leurs nombres de points. classement est un dictionnaire de dictionnaires
 
 Les points seront données si le dictionnaire est bien parcouru et si le triage a fonctionné.
 
 ### 6. mis_a_jour_classement(equipe, stats, division, classment) /2
 Cette fonction prends en paramètres le nom de l'équipe, un dictionnaire stats, le nom de la division et le classement (dictionnaire de dictionnaires).
 
 Le dictionnaire stats a la forme suivante:
 ```python
    {
        'PTS': 2,
        'BP': 5,
        'BC': 1,
        'VRP': 1
    }
 ```

 Cette fonction met à jour le classement en ajoutant les données du dictionnaire stats, le nombre de victoire, défaite, ... 
 Bref, elle met à jour tous les éléments du dictionnaire classement.

 ### 7. simuler_rencontres(matchs, classement) /3
 Cette fonction prend en paramètres le dictionnaire de dictionnaires classement et la liste de liste matchs.
 
 Pour chaque match, on veut connaitre le nom et la division des deux équipes impliquées. N'oubliez pas d'utiliser les fonctions créées précédemment.
 
 Ensuite, on veut simuler la rencontre. N'oubliez pas d'utiliser les fonctions créées précédemment.
 
 Ensuite, on veut créer les dictionnaires stats_equipe_A et stats_equipe_B. Ces dictionnaires seront utilisés dans la 
 fonction mis_a_jour_classement(). Du coup, n'oubliez pas de respecter le format demandé dans cette fonction.
 
 Finalement, il faut que vous mettiez à jour le classement. N'oubliez pas d'utiliser les fonctions créées précédemment.

 ### 8. ecrire_classement(classement) /4
 Cette fonction écrit le classement final dans un fichier text (classement_fianl.txt). On veut que vous respectiez le format classement2019.txt


 ## 8. Barème /100 <a name="bareme"></a>

|**Nom des fonctions**|**Nombre de points attribuer**|
| :- | :- |
|creer_animal                              | 2  |


## Annexe: Guide et normes de codage <a name="annexe"></a>
- [Le guide maison](https://github.com/INF1007-Gabarits/Guide-codage-python) de normes supplémentaires à respecter
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. 
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)


