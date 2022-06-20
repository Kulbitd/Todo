import sys

from src.arg import parse_args


def main():
    try:
        # 1. Спарсить аргументы командной
        cli_args = sys.argv[1:]
        # 2. обработать аргументы командной строки
        args = parse_args(cli_args)
        print(args)
    except:
        pass


if __name__ == '__main__':
    main()
