"""
Source DLT pour extraire les données de football depuis MySQL.
"""
import dlt

@dlt.source
def mysql_football_source():
    """Source DLT pour extraire les données de football depuis MySQL."""
    pass

@dlt.resource
def teams():
    """Extraction des équipes."""
    pass

@dlt.resource
def matches():
    """Extraction des matchs."""
    pass

@dlt.resource
def match_stats():
    """Extraction des statistiques de match."""
    pass
