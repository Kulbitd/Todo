from src.TodoJournal import *


def run(args):
    TodoJournal.create("./test", "test2")
    todo = TodoJournal("./test")
    print("no")
    if args.text:
        raw_text = ' '.join(args.text)
        todo.add_entry(raw_text)
    if args.delete:
        print("yes")
        todo.remove_entry(int(args.delete))
