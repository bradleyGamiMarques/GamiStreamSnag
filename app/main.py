"""
GamiStreamSnag - A beautiful UI wrapper for the yt-dlp command line tool 
Copyright (C) 2025 Bradley Andrew Marques

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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
