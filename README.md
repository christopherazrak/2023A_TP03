# TP3

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le mercredi 24 mars 2021 à 23h55](https://www.timeanddate.com/countdown/generic?iso=20200927T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif

- Renforcer la maitrise des notions de base et de l'utilisation de structure de données;
- Faire la lecture de données à partir d'un fichier texte;
- Écrire les données dans un fichier texte;
- Respecter les exigences de programmation;

## Grilles de correction
Le TP est sur 25. 

## Consignes à respecter

Tout d'abord, assurez-vous d'avoir lu le fichier [instructions.md](instructions.md) et d'avoir téléchargé le fichiers exercice.py que vous devrez compléter.
Pour ce TP, certaines contraintes sont à respecter:
- Vous ne pouvez pas importer d'autres librairies que celle qui sont déjà importées dans les fichiers.

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
