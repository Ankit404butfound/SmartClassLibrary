import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

PDFJS = f"pdfjs/web/viewer.html"
print(PDFJS)
abs_path = os.getcwd().replace("/", "\\")
PDF = f'file:///{abs_path}/enc_3790_StnnZIhQm9 - Copy-2.pdf'
print("loading PDF:", PDF)

class Window(QWebEngineView):
    def __init__(self):
        super(Window, self).__init__()
        self.load(QUrl.fromUserInput(f'file:///{PDFJS}?file={PDF}'))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    sys.exit(app.exec_())
