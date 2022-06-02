import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(description="Это немного, но это честная работа ",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog="Это должно было помочь ")
    composing = parser.add_argument_group("Writing new todos",
                                          "чтобы добавить новую запись в туду лист необходимо выполнить Х")
    composing.add_argument("text", metavar="", nargs="*", help="Добавление заметки в туду лист", )
    # metavar - изменяет отображение имени
    # аргумент ключевого слова nargs связывает разное количество аргументов
    # discription - краткое описание того, что делает команда
    # formatter_class - форматирование справки (RawDescriptionHelpFormatter, RawTextHelpFormatter
    #   ArgumentDefaultsHelpFormatter, MetavarTypeHelpFormatter)
    standalone = parser.add_argument_group(
        "Standalone Commands",
        "После выполнения этих команд работы программы завершиться",
    )
    standalone.add_argument(
        "--delete",
        dest="delete",
        help="Удаляеть запись по индексу",
    )

    path = parser.add_argument_group(
        "Setting Path",
        "Установить путь до тудушки",
    )
    path.add_argument(
        "--path",
        dest="path",
        default="./TodoJournal",
        help="Указываем, где будет находиться журнал",
    )
    return parser.parse_intermixed_args(args)
