# ANDMTM Consulting

ANDMTM Consulting est un projet de site internet développé avec Django. Ce projet permet de gérer une boutique en ligne avec des fonctionnalités telles que la liste des produits,
les détails des produits, la connexion des utilisateurs, et plus encore.

## Prérequis

- Python 3.x
- Django 3.x ou supérieur

## Installation

1. Clonez le dépôt :
    git clone https://github.com/MohamedLammineNDIONGUE1601/ANDMTM_Consulting.git
    cd ANDMTM_Consulting

2. Créez et activez un environnement virtuel :
    python -m venv env
    source env/bin/activate  # Sur Windows: env\Scripts\activate

3. Installez les dépendances :
    pip install -r requirements.txt

4. Appliquez les migrations :
    python manage.py migrate

5. Créez un superutilisateur pour accéder à l'interface d'administration :
    python manage.py createsuperuser

6. Démarrez le serveur de développement :
    python manage.py runserver

7. Accédez à l'application dans votre navigateur à l'adresse 'http://127.0.0.1:8000/'.
