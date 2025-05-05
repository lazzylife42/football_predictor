"""
Assets de base pour toutes les ligues de football.
"""
from dagster import asset

@asset
def teams():
    """Asset pour les équipes."""
    pass

@asset
def leagues():
    """Asset pour les ligues."""
    pass
