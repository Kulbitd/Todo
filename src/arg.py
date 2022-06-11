import click


@click.command()  # Не может возвращать
@click.option('--text', prompt=True)
@click.option("--delete", "-d", "index", type=str)
def parse_args(text, index):
    if index:
        return index
    if text:
        return text


if __name__ == "__main__":
    parse_args()
