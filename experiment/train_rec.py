from src.utils import get_logger
from experiment.data import load_data

logger = get_logger("train_rec")

def train_rec(experimentName: str, useFeatures: bool):
    logger.info(f"Starting training [{experimentName}] {'with' if useFeatures else 'without'} features.")
    dataset = load_data()
    