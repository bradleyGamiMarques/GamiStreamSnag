import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(
        self,
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
    ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # Set window properties
        # Name of our application
        self.title("GSS")

        # Size of the application window
        self.geometry("600x400")
