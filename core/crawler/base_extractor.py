"""
Classe de base pour tous les extracteurs de données.
"""

class BaseExtractor:
    """
    Classe abstraite définissant l'interface pour tous les extracteurs.
    """
    
    def extract_matches(self):
        """
        Extrait les informations sur les matchs depuis une page HTML.
        """
        pass
    
    def extract_stats(self):
        """
        Extrait les statistiques détaillées depuis une page HTML.
        """
        pass
    
    def validate_data(self):
        """
        Valide les données extraites.
        """
        pass
