from src.TodoJournal import TodoJournal


def run(args):
    todo = TodoJournal("./test")
    print("no")
    if args.text:
        todo.add_entry(args.text)
        raw_text = ''.join(args.text)
        todo.add_entry(raw_text)
    if args.delete:
        print("yes")
        todo.remove_entry(int(args.delete))
    if args.path:
        with open("../config.config", "w") as file:
            file.write(args.path)
