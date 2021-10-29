import sys
from src.utils import get_logger

logger = get_logger("main")

def print_usage():
    logger.info("Usage python3: main.py help")

def print_help():
    # TODO:
    logger.info("HELP")

def main():
    if len(sys.argv) < 2:
        print_usage()
    elif sys.argv[1] == "help":
        print_help()
    elif sys.argv[1] == "train":
        pass # TODO:
    elif sys.argv[1] == "test":
        pass # TODO:
    elif sys.argv[1] == "predict":
        pass # TODO:
    elif sys.argv[1] == "limers":
        pass # TODO:
    else:
        print_usage()

if __name__ == "__main__":
    main()