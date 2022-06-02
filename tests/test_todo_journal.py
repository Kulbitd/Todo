import pytest

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


@pytest.fixture()
def todo_journal_with_3_entries(tmpdir):
    todo_filename = "test_todo"
    todo_path = tmpdir.join(todo_filename)
    with open(todo_path, "w") as f:
        json.dump(
            {
                "name": "test",
                "todos": ["first entry", "second_entry", "third entry"]
            },
            f,
            indent=4,
            ensure_ascii=False, )
    return todo_path


@pytest.fixture()
def todo_json_after_remove_second_entry():
    return json.dumps(
        {
            "name": "test",
            "todos": ["first entry", "third entry"]
        },
        indent=4,
        ensure_ascii=False, )


@pytest.fixture()
def todo_object_with_with_3_entries(todo_journal_with_3_entries):
    return TodoJournal(todo_journal_with_3_entries)


def test_remove_entry(todo_object_with_with_3_entries, todo_json_after_remove_second_entry):
    todo_object_with_with_3_entries.remove_entry(1)
    expected_todo_json_after_remove_second_entry = todo_json_after_remove_second_entry
    assert expected_todo_json_after_remove_second_entry == todo_object_with_with_3_entries.path_todo.read()


def test_parse():
    with pytest.raises(SystemExit):
        todo_jrnl = TodoJournal("./data/ggg")
