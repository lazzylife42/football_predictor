"""
Sensors pour le scheduling des jobs Dagster.
"""
from dagster import sensor

@sensor
def daily_update_sensor():
    """Sensor qui déclenche la mise à jour quotidienne des données."""
    pass
