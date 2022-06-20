from src.TodoJournal import *


def run(args):
    todo = TodoJournal("./test")
    if args.text:
        raw_text = ' '.join(args.text)
        todo.add_entry(raw_text)
    if args.delete:
        todo.prin(int(args.delete))
        answer = input("Хотите удалить данную запись? [y/n]:    ")
        if answer == "yes" or answer == "y" or answer == "Yes" or answer == "Y":
            todo.remove_entry(int(args.delete))
            print("Запись удалена ")
        if answer == "no" or answer == "n" or answer == "No" or answer == "N":
            return
