"""
Assets Dagster pour la Super League suisse.
"""
from dagster import asset, AssetExecutionContext

@asset
def swiss_league_data_extraction(context: AssetExecutionContext):
    """
    Asset Dagster qui extrait les données de la Super League suisse
    en utilisant les sources DLT.
    """
    pass

@asset
def swiss_league_ml_training(context: AssetExecutionContext):
    """
    Asset Dagster qui prépare les features et déclenche l'entraînement ML
    sur la machine avec RTX3060.
    """
    pass
