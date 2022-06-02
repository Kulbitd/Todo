from src.TodoJournal import TodoJournal


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
