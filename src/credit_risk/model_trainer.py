from abc import ABC, abstractmethod


class ModelTrainer(ABC):

    @abstractmethod
    def train(self, features, target):
        """Entraîne et retourne un modèle."""
