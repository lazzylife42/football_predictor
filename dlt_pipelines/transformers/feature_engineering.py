"""
Transformations DLT pour préparer les features ML.
"""
import dlt
import pandas as pd

@dlt.transformer
def prepare_match_features(data: pd.DataFrame) -> pd.DataFrame:
    """
    Transforme les données brutes des matchs en features utilisables par le ML.
    """
    pass

@dlt.transformer
def normalize_stats(data: pd.DataFrame) -> pd.DataFrame:
    """
    Normalise les statistiques pour améliorer les performances du modèle ML.
    """
    pass
