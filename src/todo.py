import argparse

from TodoJournal import TodoJournal


def parse_args(args):
    parser = argparse.ArgumentParser()
    composing = parser.add_argument_group("Writing new todos",
                                          "чтобы добавить новую запись в туду лист необходимо выполнить Х")
    composing.add_argument("text", metavar="", nargs="*")
    return parser.parse_intermixed_args(args)


def run(args):
    todo = TodoJournal("../tests/data/test_todo")
    if args.text:
        todo.add_entry(args.text)
        raw_text = ''.join(args.text)
        todo.add_entry(raw_text)
