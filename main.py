from lywt import App


from PyQt6.QtWidgets import QApplication, QMainWindow

from lywt import MainWindow

import sys

if __name__ == '__main__':

    app = 2

    if app == 1:
        app = App()
        app.mainloop()

    elif app == 2:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

    else:
        pass
