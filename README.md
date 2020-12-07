# Projet Intégré !

# Appli DBLP
L'application que nous avons programmé vous sera utile pour extraire les données du site DBLP (la bibliothèque scientifique en ligne), les traiter dans notre interface puis en extraire des connaissances, avec de la data analyse et de la data visualisation.

Elle est divisée en 4 parties, qui partagent les données de DBLP. D'abord, utilisez la partie Interface pour récupérer les données du site.

# Interface

Dans la partie Interface, vous avez l'accès à trois options : La partie télécharger vous permet de récupérer les données selon un filtre (par exemple : les publications contenant "data science"), la partie Importer récupère les données depuis un fichier **CSV** (que nous avons déjà généré avec l'interface), puis la partie Affichage des Données vous renvoie un tableau avec toutes les informations.

Pour **télécharger** les données, vous avez 2 champs. Le premier vous offre un choix entre une publication / un auteur / un lieu, puis entrer votre recherche . Attendez quelques temps, et c'est bon ! Vos données sont chargées dans l'interface.

Pour **importer** les données, spécifiez un délimiteur CSV et le nom de votre fichier source, et en quelques secondes vos données seront traitées et importées dans l'application.

Vous pouvez ensuite les afficher simplement avec la fonction **Affichage des Données**.

# Installation de l'interface
1) Installer la librairie Dash et les autres packages nécessaires pour faire tourner notre code (lxml, ntlk)
2) Exécuter le fichier testt.py, sur Spyder, Anaconda Prompt, ou n'importe quelle méthode souhaitée.
3) Aller, avec un navigateur Web, à l'adresse http://localhost:8050

Tout est bon ! N'oubliez juste pas de récupérer des données avant de lancer la fonction d'Affichage des Données, pour ne pas avoir d'erreur de Dash.

# Dataviz 1
Dataviz 1


Partie Dataviz

# Description générale du système ou du projet.
 Ce projet est répartie en trois grandes parties :  ___Interface___ - ___Visulation___ - ___Analyse___
  
  # Visulation
  En ce qui concerne notre partie , on permet au client de faire des recherches sur des fichiers .csv, nos fichiers sont extraites du site DBLP ce qui permet de faire des recherches sur des auteurs,venues,mots-clés(keywords) ou des années d'une publication ou pourquoi pas des publications elles-memes.Pour cela on a adapter une démarche qui permet au client de rentrer lui meme les attributs aux quels il souhaite avoir une réponse dans une page html avec une simple interface, et puis le résultat est affiché sous forme d'un graphe avec des noeuds qui representent les réponses souhaitées.


## Outils utilisés
    * Lecture des fichiers et requetes : Pandas https://pandas.pydata.org/docs/
    * Graphes : NetworkX et  Pyvis https://networkx.org/documentation/stable/ - https://pyvis.readthedocs.io/en/latest/documentation.html
    * Interface : Flask https://flask-doc.readthedocs.io/en/latest/

## Statut du projet
Projet finalisé avec une intégration avec les autres groupes , mais il est toujours possible de ramener des nouveautés ou modifcations sur l'ensemble du projet.

## Processus global du Projet
* Sprint 1 : Etude des fichiers csv
    * mauvaises lignes(bad_lines)
    * lignes vides (empty_lines)
 * Sprint 2 : Fonctions et interface 
    * Fonctions 
    * html *CSS 
* Sprint 3 : Graphe 
* Spritn 4 :  Intégration 
 
 ## Indications sur l'éxecution du projet

Afin d'éxecuter le projet vous avez besoin d'un intérpréteur python ( Spyder...).

* Executer le fichier ___projet_dblp.py___ 
* Redirection vers le localhost : ***https://127.0.0.1:10500***
* Remplir les cases selon le choix du client
* Cliquer sur le boutton d'affichage du graphe
* Affichage du graphe .


# Dataviz 2
Dataviz 2

# Analyse

## Dans le dossier Dict :
	Sauvegardes des dictionnaires à chaque étape du traitement
### Ordre des sauvegardes :
  * original_titles
  * cleaned
  * onlyenglish
  * tokenized
  * nostopwords
  * lemmatized (version finale)

## Pour charger un .pickle :
```python
import pickle

with open('dict/lemmatized.pickle', 'rb') as handle:
	article_titles = pickle.load(handle)
```

## Pré-traitement des données :
  * INPUT: fichier publication.csv
  * OUTPUT: dictionnaire de listes { idconf:[tokens], idconf:[tokens], ...}
  * Utilisation de dictionnaire : + rapide que les listes sur un gros jeu de données
