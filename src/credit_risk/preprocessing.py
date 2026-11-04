def clean_data(data):
    """Supprime les observations contenant des valeurs manquantes."""
    return data.dropna()
