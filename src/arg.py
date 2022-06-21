import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     add_help=False,
                                     description='----------------------------------------',
                                     epilog='--------------------------------------')

    # formatter_class - настройка форматирования справки
    # description - краткое описание назначиния команды
    # epilog - вывод текста снизу справки

    composing = parser.add_argument_group("Writing new todos",
                                          "чтобы добавить новую запись в туду лист необходимо выполнить Х")
    composing.add_argument("text", metavar="", nargs="*")
    # metavar - изменяет имя атрибута в обьекте
    # narg - кол во аргументов
    # dest  - определяет имя атрибута

    standalone = parser.add_argument_group(
        "Standalone Commands",
        "После выполнения этих команд работы программы завершиться",
    )
    standalone.add_argument(
        "--delete",
        dest="delete",
        help="Удаляеть запись по индексу",
    )

    standalone = parser.add_argument_group(
        "Enter path ",
        "Указание пути для туду листа",
    )
    standalone.add_argument(
        "--path",
        help="Вводим путь до туду",
    )

    return parser.parse_intermixed_args(args)
