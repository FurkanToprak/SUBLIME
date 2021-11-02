import pandas as pd
import numpy as np
from config import datasetPath
from os import path

ratingsPath = path.join(datasetPath, "ratings.csv")
moviesPath = path.join(datasetPath, "movies.csv")
userInteractionData = pd.read_csv(ratingsPath)
movieData = pd.read_csv(moviesPath)
# drop timestamp feature
userInteractionData.drop("timestamp", axis=1, inplace=True)
print(userInteractionData.size)
# create interaction matrix
numUsers = np.max(userInteractionData['userId'])
numMovies = np.max(movieData['movieId'])
interaction_matrix = np.zeros((numUsers, numMovies))
print(numUsers)
print(numMovies)