from dataset import Dataset
from src.utils import get_logger
from fm_model import FMRec
from dataset import Dataset
from experiment.config import datasetPath

logger = get_logger("train_rec")

def train_rec(experimentName: str, useFeatures: bool):
    logger.info(f"Loading data for [{experimentName}].")
    dataset = Dataset(datasetPath)
    logger.info(f"Starting training [{experimentName}] {'with' if useFeatures else 'without'} features.")
    # instantiate model
    rec_model = FMRec(experimentName=experimentName, dataset=dataset, useFeatures=useFeatures)
    # train model
    rec_model.train()