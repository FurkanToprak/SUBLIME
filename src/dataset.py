""" Taken from https://github.com/caionobrega/explaining-recommendations """
import numpy as np
import pandas as pd
from scipy import sparse
from os import path


class Dataset:
    def __init__(self, dataset_path):
        """ Model-agnostic representation of a dataset. """
        trainDataPath = path.join(dataset_path, "training.csv")
        testDataPath = path.join(dataset_path, "testing.csv")
        validationDataPath = path.join(dataset_path, "validation.csv")
        itemFeaturesPath = path.join(dataset_path, 'item_features.csv')
        train_df = pd.read_csv(trainDataPath, dtype={"userId": str, "movieId": str, "rating": float})
        test_df = pd.read_csv(testDataPath, dtype={"userId": str, "movieId": str, "rating": float})
        validation_df = pd.read_csv(validationDataPath, dtype={"userId": str, "movieId": str, "rating": float})
        item_features_df = pd.read_csv(itemFeaturesPath, dtype={"userId": str, "movieId": str, "rating": float})
        # seperate ratings as labels
        self.train_labels = train_df['ratings']
        self.test_labels = test_df['ratings']
        # drop ratings from features
        train_df.drop(columns=['rating'], inplace=True)
        test_df.drop(columns=['rating'], inplace=True)
        # assign remaining
        self.train_features = train_df
        self.test_features = test_df
        self.validation = validation_df # TODO: validation?
        self.item_features = item_features_df

    @staticmethod
    def convert_to_pyfm_format(df, columns=None):
        """ 
        PyFM formatting of a dataset.
        Requres one-hot encoding of columns and matrix representation.
        Columns are typically userId, movieId, (optional) feature, (optional) value.
        """
        # Get OHE encoding of dataframe
        df_ohe = pd.get_dummies(df)
        if columns is not None:
            # relabel columns as OHE
            df_ohe = df_ohe.reindex(columns=columns)
            df_ohe = df_ohe.fillna(0)
        # compressed sparse matrix representation
        data_sparse = sparse.csr_matrix(df_ohe.astype(np.float))
        data_sparse = data_sparse.astype(np.float)
        # return data and corresponding columns
        return data_sparse, df_ohe.columns
