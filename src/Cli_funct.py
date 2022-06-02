import argparse


def parse_args(args):
    parser = argparse.ArgumentParser()  # Создание парсера
    composing = parser.add_argument_group("Writing new todos",
                                          "чтобы добавить новую запись в туду лист необходимо выполнить Х")
    # в случае неправильного ввода выведет верхнюю строку
    composing.add_argument("text", metavar="", nargs="*",
                           epilog='Надеюсь после этого хоть кому то стало понятно',
                           description="Вы можете написать новую заметку или посмотреть старую ",
                           help="Сообщение которое вы хотите записать ",
                           formatter_class='Не совсем понял назначение',
                           )
    # epilog = выводится после help
    # description = описывает что делает команда
    # Опция metavar задает имя для ожидаемого значения в выводах ошибок и справки.
    # nargs указывает количество аргументов командной строки, которые должны использоваться.

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


def run(args):
    pass
