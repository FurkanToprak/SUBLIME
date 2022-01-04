from src.dataset import Dataset
from src.utils import get_logger
from src.fm_model import FMRec
from experiment.config import datasetPath, trainedModelPath
import pickle
from os import path

logger = get_logger("train_rec")

def train_rec(experimentName: str, useFeatures: bool):
    logger.info(f"Loading data for [{experimentName}].")
    dataset = Dataset(datasetPath)
    # instantiate model
    logger.info(f"Initialized FM model for model [{experimentName}].")
    rec_model = FMRec(rec_name=experimentName, dataset=dataset, uses_features=useFeatures)
    logger.info(f"Starting training [{experimentName}] {'with' if useFeatures else 'without'} features.")
    # train model
    rec_model.train()
    # save model
    logger.info(f'Pickling model to {trainedModelPath}')
    with open(trainedModelPath, 'wb') as pickleFile:
        pickle.dump(rec_model, pickleFile)
    logger.info('Pickled model.')