from os import path
# repository's path
parentPath = path.dirname(path.dirname(__file__))
# path to a given dataset
datasetPath = path.join(path.join(parentPath, "datasets"), "ml-20m")
trainingSplit, testingSplit = (0.8, 0.2)
