# Chess Tournament Manager

Application de gestion de tournois d'échecs en Python, fonctionnant hors ligne.

## Prérequis

- Python 3.12+

## Installation

1. Cloner le repository :

git clone https://github.com/GuillaumeQuelen/Chess_Tournaments.git
cd Chess_Tournaments


2. Créer et activer l'environnement virtuel :

python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


3. Installer les dépendances :

pip install -r requirements.txt


## Lancer le programme

python3 main.py


## Rapport Flake8

flake8 --max-line-length=119 --exclude=venv --format=html --htmldir=flake8_rapport .


Le rapport sera disponible dans le dossier `flake8_rapport/index.html`.

## Fonctionnalités

- Gestion des joueurs (ajout, validation identifiant national)
- Gestion des tournois (création, rounds, matchs, scores)
- Système suisse d'appariement
- 5 rapports disponibles
- Sauvegarde automatique en JSON