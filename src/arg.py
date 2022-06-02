import argparse


def parse_args(args):
    parser = argparse.ArgumentParser()
    composing = parser.add_argument_group("Writing new todos",
                                          "чтобы добавить новую запись в туду лист необходимо выполнить Х")
    composing.add_argument("text", metavar="", nargs="*",
                           help="Добавление заметки в туду лист",
                           epilog="Надеюсь это помогло",
                           description="",
                           formatter_class="")
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

    return parser.parse_intermixed_args(args)
