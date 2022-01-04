import sys
from src.utils import config_logging, get_logger
from experiment.train_rec import train_rec
from experiment.predict_rec import predict_rec

logger = get_logger("main")

def log_usage():
    logger.info("Usage: python3 main.py help")

def log_train_usage():
    logger.info("Usage: python3 main.py train <experimentName> <useFeatures [T/F]>")

def log_predict_usage():
    logger.info("Usage: python3 main.py predict <experimentName>")

def print_help():
    logger.info("Usage: python3 main.py <help/train/test/predict/limers>")

def main():
    print("All output in directory log/")
    if len(sys.argv) < 3:
        log_usage()
    elif sys.argv[1] == "help":
        print_help()
    elif sys.argv[1] == "train":
        if len(sys.argv) != 4:
            log_train_usage()
            return
        experimentName = sys.argv[2]
        useFeatures = sys.argv[3]
        config_logging(f'test-{experimentName}')
        train_rec(experimentName, useFeatures)
    elif sys.argv[1] == "test":
        pass
    elif sys.argv[1] == "predict":
        if len(sys.argv) != 3:
            log_predict_usage()
            return
        experimentName = sys.argv[2]
        config_logging(f'test-{experimentName}')
        predict_rec(experimentName)
    elif sys.argv[1] == "limers":
        pass # TODO:
    else:
        log_usage()

if __name__ == "__main__":
    main()