from gui import MainWindow


def main() -> None:
    """Docstring for main.

    This function initializes the main graphical user interface by creating an
    instance of the MainWindow class (imported from the gui module) and starts
    the application's event loop.
    The event loop runs until the user closes the window.

    Returns:
        None
    """
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
