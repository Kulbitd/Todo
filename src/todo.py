import sys

from src.TodoJournal import *


def run(args):
    if args.path:
        try:
            with open('../config.config', 'w') as f:
                f.writelines(args.path)
        except FileNotFoundError as e:
            sys.exit(-0)
    with open('../config.config', 'r') as f:
        a = f.read()
        TodoJournal.create(a, "name")
        todo = TodoJournal(a)
    if args.text:
        raw_text = ' '.join(args.text)
        todo.add_entry(raw_text)
    if args.delete:
        todo.prin(int(args.delete))
        answer = input("Хотите удалить данную запись? [y/n]:    ")
        if answer == "yes" or answer == "y" or answer == "Yes" or answer == "Y":
            todo.remove_entry(int(args.delete))
            print("Запись удалена ")
        elif answer == "no" or answer == "n" or answer == "No" or answer == "N":
            return
        else:
            print("Некоректный ввод ")
