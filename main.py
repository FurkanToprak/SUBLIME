import sys

def print_usage():
    print("Usage python3: main.py help")

def print_help():
    print("TODO:")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
    elif sys.argv[1] == "help":
        print_help()
    elif sys.argv[1] == "train":
        pass
    elif sys.argv[1] == "predict":
        pass
    elif sys.argv[1] == "limers":
        pass
    else:
        print_usage()