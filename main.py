"""
Создаем туду приложение
"""
import json
import sys


class TodoJournal:
    """
    Класс в котором определяем методы для работы с туду такие как удаление, удаление
    """

    def __init__(self, path_todo, name):
        self.path_todo = path_todo
        self.name = name

    def create(self):
        """
        Функия создающая файл , в виде json, name - имя файла ,
         todos[] - список , внутри которого будут наши to_do записки
        :return: None
        """
        with open(self.path_todo, "w", encoding='utf-8') as todo_file:
            json.dump(
                {"name": self.name, "todos": []},
                todo_file,
                sort_keys=True,
                indent=4,
                ensure_ascii=False,
            )

    def add_entry(self, new_entry):
        """
        Функция заполняющая наш список todos[] заметками
        :param new_entry: Содержание заметки
        :return: None
        """
        data = self._parse()

        name = data["name"]
        todos = data["todos"]

        todos.append(new_entry)

        new_data = {
            "name": name,
            "todos": todos,
        }

        self._update(new_data)

    def remove_entry(self, index):
        """
        Функция удаления заметок в todos[] по индексу
        :param index: Индекс заметки, которую хотим удалить
        :return: None
        """
        data = self._parse()
        name = data["name"]
        todos = data["todos"]

        todos.remove(todos[index])

        new_data = {
            "name": name,
            "todos": todos,
        }

        self._update(new_data)

    def _update(self, new_data):
        """
        Функция отвечающий за записи json в файл
        :param new_data: Информация которую мы хотим записать
        :return: None
        """
        with open(self.path_todo, "w", encoding='utf-8') as todo_file:
            json.dump(
                new_data,
                todo_file,
                sort_keys=True,
                indent=4,
                ensure_ascii=False,
            )

    def _parse(self):
        """
        Функция , получающая содержимое нашего to_do файла
        :return: data - содержимое to_do листа
        """
        try:
            with open(self.path_todo, 'r') as todo_file:
                data = json.load(todo_file)
            return data
        except FileNotFoundError as error:
            print(f"{error}")
            print(f"Не существует такой тудушки: {self.path_todo}")
            sys.exit(1)


def main():
    """
    Вызов и создание нашего журанала(по идее)
    :return: None
    """
    pass


if __name__ == '__main__':
    main()
