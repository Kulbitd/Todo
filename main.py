"""
Создаем туду приложение
"""
import json
import sys


class TodoJournal:
    """
    Класс в котором определяем методы для работы с туду такие как удаление, удаление
    """

    def __init__(self, path_todo):
        self.path_todo = path_todo
        self.name = self._parse()["name"]
        self.entries = self._parse()["todos"]

    @staticmethod
    def create(filename, name):
        """
        Функия создающая файл , в виде json, filename - имя файла ,
         name - имя тудушки
        :return: None
        """
        try:
            with open(filename, "w", encoding='utf-8') as todo_file:
                json.dump(
                    {"name": name, "todos": []},
                    todo_file,
                    sort_keys=True,
                    indent=4,
                    ensure_ascii=False,
                )
        except FileExistsError as error:
            print(f"{error}")
            print(f"Не возможно создать файл(проверьте права): {filename}")
            sys.exit(3)

    def add_entry(self, new_entry):
        """
        Функция заполняющая наш список todos[] заметками
        :param new_entry: Содержание заметки
        :return: None
        """

        self.entries.append(new_entry)
        # Надо подумать какое исключние сюда(todos вроде всегда существует)

        new_data = {
            "name": self.name,
            "todos": self.entries,
        }

        self._update(new_data)

    def remove_entry(self, index):
        """
        Функция удаления заметок в todos[] по индексу
        :param index: Индекс заметки, которую хотим удалить
        :return: None
        """
        try:
            self.entries.remove(self.entries[index])

            new_data = {
                "name": self.name,
                "todos": self.entries,
            }

            self._update(new_data)
        except ValueError as error:
            print(f"{error}")
            print(f"Не существует такой индекса: {index}")
            sys.exit(2)

    def _update(self, new_data):
        """
        Функция отвечающий за записи json в файл
        :param new_data: Информация которую мы хотим записать
        :return: None
        """
        try:
            with open(self.path_todo, "w", encoding='utf-8') as todo_file:
                json.dump(
                    new_data,
                    todo_file,
                    sort_keys=True,
                    indent=4,
                    ensure_ascii=False,
                )
        except FileNotFoundError as error:
            print(f"{error}")
            print(f"Не существует такой тудушки: {self.path_todo}")
            sys.exit(1)

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


if __name__ == '__main__':
    main()
