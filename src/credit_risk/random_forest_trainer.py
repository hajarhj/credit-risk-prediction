from sklearn.ensemble import RandomForestClassifier

from .model_trainer import ModelTrainer


class RandomForestTrainer(ModelTrainer):

    def train(self, features, target):
        model = RandomForestClassifier(random_state=42)

        model.fit(features, target)

        return model
