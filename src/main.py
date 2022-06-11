from src.arg import parse_args
from src.todo import run


def main():
    try:
        args = parse_args()
        return run(args)
    except Exception as e:
        print(e)
        return 1


if __name__ == '__main__':
    main()
