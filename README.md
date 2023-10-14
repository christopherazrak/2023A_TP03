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
<p align="justify">
L’analyse des données fait partie des disciplines les plus prisées de nos jours. Outil stratégique au sein des organisations, elle permet entre autres de mieux comprendre des événements qui se produisent avec les facteurs qui les favorisent, ou encore de mesurer l’impact d’une opération ou d’une politique grâce à des indicateurs de performance.</p>

## 2. Objectifs du laboratoire
- **Maîtrise des notions de base et structures de données** : Renforcer la compréhension et l'application des concepts fondamentaux et des structures de données en Python.
- **Gestion de fichiers** : Apprendre à lire des données depuis un fichier texte et à écrire des données dans un fichier texte en respectant un format spécifié.
- **Respect des exigences de programmation** : Veiller à suivre les meilleures pratiques de programmation et à respecter les spécifications fournies.
- **Utilisation de Dataframes** : Créer et manipuler des Dataframes, structures de données essentielles pour l'analyse de données.
- **Analyse avec les bibliothèques scientifiques** : Exploiter des bibliothèques telles que pandas, numpy, matplotlib et autres pour effectuer une analyse complète des données.

## 3. Description du problème: 
L'objectif de ce laboratoire est de simuler la fin de la saison 2019 de la Ligue Nationale de Hockey (LNH). Selon le site de statistiques sportives [sportsclubstats.com](http://www.sportsclubstats.com/NHL), en date du 5 février 2019, le Club de Hockey Canadien (CH) de Montréal possédait une probabilité de 84.6% de se qualifier parmi les 16 équipes (sur 31) pour les séries éliminatoires de cette saison. Mais comment ce site arrive-t-il à une telle prédiction? Il effectue plusieurs millions de simulations aléatoires des matchs restants chaque jour, puis détermine la probabilité basée sur les résultats obtenus.

### 3.1 Votre mission:
1. Créer un programme capable de simuler la fin de la saison en se basant sur des données fournies et des fonctions aléatoires.
2. Effectuer une étude détaillée et produire des visualisations sur les points suivants:
  1. Équipes ayant marqué le plus et le moins de buts.
  2. Équipes ayant accumulé le plus et le moins de points.
  3. Équipes ayant le plus grand et le plus petit nombre de victoires et de défaites.
  4. Analyse par division sur:
    1. Le pourcentage de buts marqués.
    2. Le pourcentage de points accumulés.
    3. Le pourcentage de victoires et de défaites.

### 3.2 Données:
- `classement2019.txt`: Liste des 31 équipes (réparties en 4 divisions) avec leurs statistiques jusqu'au 4 février.
- `matchs2019.txt`: Liste des matchs restants à partir du 5 février.

### 3.3 Mécanisme de simulation:
- Les résultats des matchs sont déterminés aléatoirement avec la fonction `md_randnormal()`. Cette fonction génère des nombres suivant une distribution normale basée sur une moyenne donnée, permettant d'avantager une équipe par rapport à une autre selon leurs performances.
- L'avantage du terrain sera également pris en compte pour l'équipe jouant à domicile.
- La conclusion de chaque match (temps règlementaire, prolongation ou tirs de barrage) est déterminée aléatoirement, influençant les points accordés aux équipes.

Une fois tous les matchs simulés, le classement des équipes est mis à jour. Le processus est répété plusieurs millions de fois pour obtenir la probabilité de qualification aux séries éliminatoires pour chaque équipe.

## 4. Déroulement d'une saison de la LNH
La LNH se compose de 31 équipes réparties en 4 divisions. Deux divisions (Atlantique et Métropolitaine) constituent la conférence de l'Est, tandis que les deux autres (Centrale et Pacifique) forment la conférence de l'Ouest. Chaque équipe joue 82 matchs lors de la saison régulière, et les points sont attribués selon le résultat du match :
- **Victoire régulière (REG):** 2 points pour le gagnant, 0 pour le perdant.
- **Prolongation (PROL)**: 2 points pour le gagnant, 1 pour le perdant.
- **Fusillade (FUS)**: 2 points pour le gagnant, 1 pour le perdant. Néanmoins, cette victoire n'est pas comptabilisée dans la statistique VRP.

### 4.1 Classement:
À la fin de la saison, les équipes sont classées en fonction de leurs points. En cas d'égalité, la statistique VRP est utilisée comme critère de départage. Les trois meilleures équipes de chaque division sont automatiquement qualifiées, et les deux places restantes (wildcards) sont attribuées aux meilleures équipes non encore qualifiées. Ces wildcards peuvent venir de la même division.



 ### 1. lire_classement() /5
Cette fonction charge en mémoire le contenu du fichier classement2019.txt et store les données dans un dictionnaire.

Dans cette fonction, on veut un dictionnaire de dictionnaires qui ait la forme suivante:

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

Les points seront donnés dans la lecture du fichier et storer les données dans le dictionnaire.

 ### 2. lire_match() /3
Cette fonction charge en mémoire le contenu du fichier matchs2019.txt et store les données dans une liste de listes.

Dans cette fonction, on veut une liste de listes qui ait la forme suivante:
```python
    [['ANA', 'TOR'], ['L-A', 'NYR'], ...]
```

Les points seront donnés dans la lecture du fichier et storer les données dans la liste.

 ### 3. trouver_equipe_division(equipe_abv, classement) /2
 À l'aide du dictionnaire classement et de l'abbréviation de l'équipe (string), trouvez et retournez le nom de l'équipe et sa division.
 
 Le point sera donné si la fonction retourne le bon nom de l'équipe et la bonne division de l'équipe.
 
 ### 4. simulation(diffA, diffB) /4
 Cette fonction prend en paramètre le différentiel de buts de l'équipe A et de l'équipe B. 
 
 Cette fonction a pour but de simuler une rencontre entre l'equipe A et B. N'oubliez pas que l'équipe à domicile est l'équipe B et l'équipe A est l'équipe visitrice

 Pour cela, nous allons dire que la moyenne de base de buts est de 3. Cependant, nous allons modifier cette moyenne en fonction
 des performances d'une équipe et en fonction de si elle joue à domicile. 
 
 La première étape est de calculer diff_dom et diff_vis. diff_dom est la différence entre le différence de l'équipe à domicile et de l'équipe à l'extérieur divisé par la moyenne de 3 buts.
 diff_vis est l'inverse de diff_dom. Par exemple, si l'équipe A a un différenciel de +33 et l'équipe B un différenciel de -3, diff_dom sera un désavantage de -12 et diff_vis sera un avantage de +12.
 
 La deuxième étape est de calculer le nombre de buts de l'équipe à domicile. Pour cela , nous allons utiliser normalvariate de random. Cette fonction
 prend deux paramètres mu et sigma. Mu sera calculer de la sorte 3 + (diff_dom/100) et sigma sera de 1.5
 
 La troisième étape est de calculer le nombre de buts de l'équipe visitrice. Pour cela , nous allons aussi utiliser normalvariate de random.
 Mu sera calculer de la sorte 3 + (diff_vis/100) -0.2 et sigma sera de 1.5. Le -0.2 de l'équipe visitrice est ajouté pour désavantager l'équipe visitrice.
 
 Les valeurs générées par cette fonction aléatoire sont des réels mais nous voulons les ramener à des entiers.  Vous devez donc arrondir les valeurs générées.
 Exemples : 3.4567 donne 3,  2.7654 donne 3, 0.4325 donne 0  et -1.7635 donne 0.
 
 Finalement, il faut décider qui a remporté la partie.
 
 Si l'équipe A a marqué plus de buts que l'équipe B, l'équipe A a gagné. Une victoire donne 2 points et une défaite 0.
 
 Si l'équipe B a marqué plus de buts que l'équipe A, l'équipe B a gagné.
 
 Si les deux équipes ont marqué le même nombre de buts, on utilise une valeur aléatoire pour savoir si le match s'est décidé en prolongation
 ou en fusillades. Dans ces deux cas, l'équipe perdante a 1 point. Dans le cas d'une victoire en fusillade, le vrp est de 0. 
 
 
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


