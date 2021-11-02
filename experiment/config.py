""" Contains many hard-coded paths and hyperparameters. """
from os import path
# repository's path
parentPath = path.dirname(path.dirname(__file__))
# path to a given dataset
datasetPath = path.join(path.join(parentPath, "datasets"), "ml-20m")
trainingSplit, testingSplit = (0.8, 0.2)
# We only count the interaction in the interaction matrix if rating >= ratingCutoff
ratingCutoff = 3