from sklearn.linear_model import LogisticRegression

from .model_trainer import ModelTrainer


class LogisticRegressionTrainer(ModelTrainer):

    def train(self, features, target):
        model = LogisticRegression()

        model.fit(features, target)

        return model
