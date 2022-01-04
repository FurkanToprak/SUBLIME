""" Contains many hard-coded paths and hyperparameters. """
from os import path
# repository's path
parentPath = path.dirname(path.dirname(__file__))
# path to a given dataset
datasetPath = path.join(path.join(parentPath, "datasets"), "ml-latest-small")
outputPath = path.join(parentPath, "outputs")
train_ratio, test_ratio, validation_ratio = 0.7, 0.2, 0.1
# # We only count the interaction in the interaction matrix if rating >= ratingCutoff
# ratingCutoff = 3