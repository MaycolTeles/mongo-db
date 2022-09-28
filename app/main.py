"""
Main module, containing the main function.
"""

from src.presenters import CLI


def main() -> None:
    """
    Main function. This is where the application starts.
    """
    cli = CLI()

    cli.run()


if __name__ == '__main__':
    main()
