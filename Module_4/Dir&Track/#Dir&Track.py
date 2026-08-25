#Dir&Track
import sys
from pathlib import Path
from colorama import Fore, init
init()

def show_tree(path, indent=""):
    for item in path.iterdir():

        if item.name == ".venv":
            continue

        if item.is_dir():
            print(Fore.BLUE + indent + item.name + Fore.RESET)
            show_tree(item, indent + "    ")
        else:
            print(Fore.GREEN + indent + item.name + Fore.RESET)
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print("Вказаний шлях не існує")
        sys.exit(1)

    if not path.is_dir():
        print("Вказаний шлях не є директорією")
        sys.exit(1)

    show_tree(path)