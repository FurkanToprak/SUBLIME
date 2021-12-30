from abc import ABC, abstractmethod
import pandas as pd

class Model(ABC):
    """ 
    Abstract class implementation. 
    Mainly useful for its _get_candidates method.
    """
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
    
    def _get_candidates(self, user_id, training_df, filter_history=True):
        """ 
        Returns items to predict for a particular user specified by user_id.
        Used in a model_agnostic way to make recommendations.
        If filter_history, does not return already interacted items.
        """
        # enumerate all items
        all_items = set(training_df["movieId"].values.tolist())
        # enumerate all items that a particular user interacted with
        user_items = set(training_df.loc[training_df["userId"] == str(user_id)]["itemId"].values.tolist())
        # filter pre-interacted data
        candidate_items = None
        if filter_history:
            candidate_items = all_items - user_items
        else:
            candidate_items = all_items

        # create dataframe
        df = pd.DataFrame()
        df['itemId'] = list(candidate_items)
        df['userId'] = str(user_id)
        # drop all non-user/movie columns
        df = df[['userId', 'movieId']]

        return df