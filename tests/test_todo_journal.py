from src.TodoJournal import TodoJournal


def test_init():
    """Проверка корректности инициализации TodoJournal"""
    todo = TodoJournal("data/test_todo")
    entries = todo.entries
    name = todo.name
    expected_entries = []
    expected_name = "test_todo"
    assert entries == expected_entries
    assert name == expected_name
