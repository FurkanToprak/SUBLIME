from dataset import Dataset
from src.utils import get_logger
from fm_model import FMRec
from dataset import Dataset
from experiment.config import datasetPath

logger = get_logger("train_rec")

def train_rec(experimentName: str, useFeatures: bool):
    logger.info(f"Loading data for [{experimentName}].")
    dataset = Dataset(datasetPath)
    # instantiate model
    logger.info(f"Initialized FM model for model [{experimentName}].")
    rec_model = FMRec(experimentName=experimentName, dataset=dataset, useFeatures=useFeatures)
    logger.info(f"Starting training [{experimentName}] {'with' if useFeatures else 'without'} features.")
    # train model
    rec_model.train()
    # save model
    logger.info('Pickling model')
    # TODO: pickle model
    logger.info('Pickled model')