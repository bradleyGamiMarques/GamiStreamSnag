import tkinter as tk
from tkinter import ttk
from tkinter import font
import os

from yt_dlp import YoutubeDL

from platformdirs import user_downloads_dir


class MainWindow(tk.Tk):
    def download(self) -> None:
        """
        Download the video located at the URL provided by user input.

        This function is unsafe and is a proof of concept.
        It takes the unsanitized user input from the user and passes it to
        YoutubeDL.download().

        The resulting video is downloaded to the user's Downloads directory

        :param self: Instance of the MainWindow class
        :type self:

        Returns:
            None
        """
        # Get the user's Downloads folder
        downloads_dir: str = user_downloads_dir()

        # Ensure the Downloads directory exists
        os.makedirs(downloads_dir, exist_ok=True)

        url: str = self.url_field_entry_str.get()
        urls: list[str] = []
        urls.append(url)

        ydl_opts = {"outtmpl": os.path.join(downloads_dir, "%(title)s.%(ext)s")}

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)

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

        default_font = font.nametofont("TkDefaultFont")
        custom_font = font.Font(
            family=default_font.actual("family"), size=12, weight="bold"
        )

        title_label = ttk.Label(master=self, text="Enter video URL", font=custom_font)
        title_label.pack()

        # Frame for holding the input field and download button
        input_frame = ttk.Frame(master=self)

        self.url_field_entry_str = tk.StringVar()

        # Widgets
        url_field = ttk.Entry(master=input_frame, textvariable=self.url_field_entry_str)
        button = ttk.Button(master=input_frame, text="Download", command=self.download)

        # Add the UI widgets to the MainWindow
        url_field.pack(side="left", padx=10)
        button.pack(side="left")
        input_frame.pack(pady=10)
