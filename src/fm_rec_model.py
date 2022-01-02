from pyfm import pylibfm
import pandas as pd
from src.dataset import Dataset

class FMRec(Model):
    def __init__(self, rec_name, dataset, uses_features):
        super(FMRec, self).__init__(rec_name, dataset, uses_features)

        # init
        self.one_hot_columns = None

        # default rec
        self.fm = pylibfm.FM(num_factors=50, num_iter=10, task="regression",
                             initial_learning_rate=0.001,
                             learning_rate_schedule="optimal",
                             verbose=True)

    def train(self):
        if self.uses_features:
            df = pd.merge(self.dataset.training_df, self.dataset.item_features, on="item_id", how="left")
        else:
            df = self.dataset.training_df.copy()

        training_data, training_columns = Dataset.convert_to_pyfm_format(df)
        self.one_hot_columns = training_columns

        self.fm.fit(training_data, self.dataset.y_train)

    def predict(self, df):
        if self.uses_features:
            df = pd.merge(df, self.dataset.item_features, on="item_id", how="left")

        all_predictions = list()

        # divide in chunks to avoid memory errors
        chunk_size = 10
        chunks = np.array_split(df, chunk_size)
        for chunck in chunks:
            # convert
            test_data, _ = Dataset.convert_to_pyfm_format(chunck)

            # get predictions
            preds = self.fm.predict(test_data)
            all_predictions.extend(preds.round(3))

        return all_predictions

    def recommend(self, user_ids, n=10, filter_history=True):
        df_list = list()

        # get predictions
        for uid in user_ids:
            logger.info("recommending for user: {}".format(uid))
            df = self._get_candidates(uid, self.dataset.training_df, filter_history=filter_history)
            predictions = self.predict(df)
            df['prediction'] = predictions

            df_list.append(df)
        result = pd.concat(df_list)

        # Sort by uid and predictions
        result.sort_values(by=['user_id', 'prediction'], inplace=True, ascending=[True, False])
        return result.groupby("user_id").head(n)
