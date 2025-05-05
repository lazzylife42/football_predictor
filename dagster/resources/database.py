"""
Ressources pour la connexion à la base de données MySQL.
"""
from dagster import resource

@resource
def mysql_resource():
    """Ressource pour se connecter à MySQL."""
    pass
