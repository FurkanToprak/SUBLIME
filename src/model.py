from abc import ABC, abstractmethod

class Model(ABC):
    def __init__(self, rec_name, dataset, uses_features):
        self.rec_name = rec_name
        self.dataset = dataset
        self.uses_features = uses_features

    @abstractmethod
    def train(self):
        raise NotImplementedError

    @abstractmethod
    def predict(self, df):
        raise NotImplementedError

    @abstractmethod
    def recommend(self, user_id, n=10, filter_history=True):
        raise NotImplementedError