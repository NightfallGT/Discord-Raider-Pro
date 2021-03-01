from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from util import *
from ui import *
import threading
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        clear()

        os.system('title Discord Raid Pro [Console]')
        os.system('mode 60, 20')

        self.C = Container()

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon('icon/discord-128.ico')) 

        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggle_menu(self, 250, True))

        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        self.ui.pushButton.clicked.connect(lambda: UIFunctions.ui_file_dialog(self))

        #status changer
        self.ui.pushButton_20.clicked.connect(self.status_changer)

        #dm spammer  fake type
        self.ui.pushButton_19.clicked.connect(self.fake_type)

        #embed spammer
        self.ui.pushButton_17.clicked.connect(self.embed_spam)

        #reaction adder
        self.ui.pushButton_16.clicked.connect(self.react)

        #vc spammer
        self.ui.pushButton_13.clicked.connect(self.vc_music)

        #vc leave
        self.ui.pushButton_8.clicked.connect(self.vc_leave)

        #vc join
        self.ui.pushButton_7.clicked.connect(self.vc_join)

        #text spam
        self.ui.pushButton_6.clicked.connect(self.text_spam)

        #server leave
        self.ui.pushButton_5.clicked.connect(self.server_leave)

        #server join
        self.ui.pushButton_4.clicked.connect(self.server_join)

        self.show()

    def _setup(self):
        tokens = self.C.get_tokens()
        if tokens:
            s = Setup(tokens)
            return s

        else:
            return False

    def _status_changer(self):
        file_path = self.C.get_file_path()
        os.system('start /wait cmd /c python util/console/status_changer.py --i "%s"' % (file_path))

    def status_changer(self):
        s = self._setup()

        if not s:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Add tokens')
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
            return None
        threading.Thread(target=self._status_changer).start()

    def server_join(self):
        s = self._setup()

        if not s:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Add tokens')
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
            return None

        print('Server Join called.')
        discord_invite = self.ui.lineEdit_4.text()
        
        threading.Thread(target=s.server_join, args=(discord_invite,)).start()

    def server_leave(self):
        s = self._setup()

        if not s:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Add tokens')
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
            return None

        print('Server leave called.')
        guild_id = self.ui.lineEdit_5.text()
        
        threading.Thread(target=s.server_leave, args=(guild_id,),).start()

    def _text_spam(self):
        channel_id = self.ui.lineEdit_6.text()
        file_path = self.C.get_file_path()
        os.system('start /wait cmd /c python util/console/text_spam.py --i "%s" --m %s' % (file_path, channel_id))

    def text_spam(self):
        s = self._setup()

        if not s:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Add tokens')
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
            return None
        threading.Thread(target=self._text_spam).start()

    def _vc_join(self):
        vcid = self.ui.lineEdit_7.text()
        file_path = self.C.get_file_path()
        os.system('start /wait cmd /c python util/console/vc_join.py --i "%s" --m %s' % (file_path, vcid))

    def vc_join(self):
        s = self._setup()

        if not s:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Add tokens')
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
            return None
        threading.Thread(target=self._vc_join).start()

    def _vc_leave(self):
        vcid = self.ui.lineEdit_8.text()
        file_path = self.C.get_file_path()
        os.system('start /wait cmd /c python util/console/vc_leave.py --i "%s" --m %s' % (file_path, vcid))

    def vc_leave(self):
        s = self._setup()

        if not s:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Add tokens')
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
            return None
        threading.Thread(target=self._vc_leave).start()


    def _vc_music(self):
        vcid = self.ui.lineEdit_13.text()
        file_path = self.C.get_file_path()
        os.system('start /wait cmd /c python util/console/vc_music.py --i "%s" --m %s' % (file_path, vcid))

    def vc_music(self):
        s = self._setup()

        if not s:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Add tokens')
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
            return None
        threading.Thread(target=self._vc_music).start()

    def _react(self):
        channel_id = self.ui.lineEdit_16.text()
        file_path = self.C.get_file_path()
        os.system('start /wait cmd /c python util/console/react_mes.py --i "%s" --m %s' % (file_path, channel_id))

    def react(self):
        s = self._setup()

        if not s:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Add tokens')
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
            return None

        threading.Thread(target=self._react).start()

    def _embed_spam(self):
        channel_id = self.ui.lineEdit_17.text()
        file_path = self.C.get_file_path()
        os.system('start /wait cmd /c python util/console/embed_spam.py --i "%s" --m %s' % (file_path, channel_id))

    def embed_spam(self):
        s = self._setup()

        if not s:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Add tokens')
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
            return None
        threading.Thread(target=self._embed_spam).start()


    def _fake_type(self):
        channel_id = self.ui.lineEdit_19.text()
        file_path = self.C.get_file_path()
        os.system('start /wait cmd /c python util/console/fake_type.py --i "%s" --m %s' % (file_path, channel_id))

    def fake_type(self):
        s = self._setup()

        if not s:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Add tokens')
            msg.setIcon(QMessageBox.Critical)

            x = msg.exec_()
            return None
        threading.Thread(target=self._fake_type).start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
