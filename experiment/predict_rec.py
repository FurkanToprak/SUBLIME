from src.dataset import Dataset
from src.utils import get_logger
from src.fm_model import FMRec
from experiment.config import datasetPath, trainedModelPath
import pickle
from os import path

logger = get_logger("predict_rec")

def predict_rec(experimentName: str):
    logger.info(f"Loading data for [{experimentName}].")
    dataset = Dataset(datasetPath)
    logger.info(f"Loading pretrained model for [{experimentName}].")
    rec_model = None
    with open(trainedModelPath, "rb") as pickleFile:
        rec_model = pickle.load(pickleFile)
    logger.info(f"Generating predictions.")
    logger.info(f"Saving predictions.")

    usersToRecommendTo = ["1", "2", "3", "5", "8", "13", "21", "34"]
    logger.info(f"Generating recommendations for users {usersToRecommendTo}")
    recs = rec_model.recommend(usersToRecommendTo)
    logger.info(f"Saving recommendation")

