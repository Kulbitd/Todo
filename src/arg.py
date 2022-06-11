import click


@click.command()  # Не может возвращать
@click.option('text', help='Add new note', type=str)
@click.option("--delete", "-d", "index", help='Enter the index what you want to remove', type=str)
def parse_args(filename, index):
    print(filename)


if __name__ == "__main__":
    parse_args()
