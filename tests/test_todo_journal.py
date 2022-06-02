from src.TodoJournal import TodoJournal
from src.TodoJournal import json


def test_init(tmpdir):
    """Проверка корректности инициализации TodoJournal"""
    todo_filename = "test"
    todo = TodoJournal(todo_filename)
    entries = todo.entries
    name = todo.name
    expected_entries = []
    expected_name = "test_todo"
    assert entries == expected_entries
    assert name == expected_name


def test_create_journal(tmpdir):
    todo_filename = "test"
    todo = tmpdir.join(todo_filename)
    TodoJournal.create(todo, "test")

    expected_todo = json.dumps(
        {
            "name": "test",
            "todos": []
        },
        indent=4)
    assert expected_todo == todo.read()


def test_add_entry(tmpdir):
    todo_filename = "test"
    todo = tmpdir.join(todo_filename)
    TodoJournal.create(todo, "test")
    todo_jrnl = TodoJournal(todo)
    todo_jrnl.add_entry("Сходить за молоком")

    expected_todo = json.dumps(
        {
            "name": "test",
            "todos": ["Сходить за молоком"]
        },
        indent=4,
        ensure_ascii=False, )
    assert expected_todo == todo.read()
