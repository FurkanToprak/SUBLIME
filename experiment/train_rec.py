from src.utils import get_logger
from src.fm_rec_model import FMRec
from experiment.data import load_data

logger = get_logger("train_rec")

def train_rec(experimentName: str, useFeatures: bool):
    logger.info(f"Loading data for [{experimentName}].")
    dataset = load_data()
    logger.info(f"Starting training [{experimentName}] {'with' if useFeatures else 'without'} features.")
    # instantiate model
    rec_model = FMRec(experimentName=experimentName, dataset=dataset, useFeatures=useFeatures)
    # train model
    rec_model.train()