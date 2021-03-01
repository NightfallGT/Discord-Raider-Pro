from main import *
from .logic_functions import *


class UIFunctions(MainWindow):
    def toggle_menu(self, maxWidth, enable):
        if enable:

            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()


    def ui_file_dialog(self):
            filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Open File', dir='.', filter='Text Files (*.txt)')

            if filename:
                temp_token = extract_token(filename)
                self.ui.lineEdit.setText(filename)
                display_str = ''
                for x in temp_token:
                    display_str += x + '\n'

                self.C.add_tokens(temp_token)
                self.C.add_file_path(filename)
                
                with open(filename, 'r', encoding='utf-8') as f:
                    self.ui.textEdit.setText(display_str)

                print('[' + str(len(self.C.get_tokens())) + ']' + ' tokens loaded.')
                

    def disable_button_all(self):
        print('Disabled buttons')
        self.ui.pushButton_20.setEnabled(False)

        self.ui.pushButton_19.setEnabled(False)

        self.ui.pushButton_17.setEnabled(False)

        self.ui.pushButton_16.setEnabled(False)

        self.ui.pushButton_13.setEnabled(False)

        self.ui.pushButton_8.setEnabled(False)

        self.ui.pushButton_7.setEnabled(False)

        self.ui.pushButton_6.setEnabled(False)

        self.ui.pushButton_5.setEnabled(False)

        self.ui.pushButton_4.setEnabled(False)  

    def enable_button_all(self):
        print('Enabled buttons')
        self.ui.pushButton_20.setEnabled(True)

        self.ui.pushButton_19.setEnabled(True)

        self.ui.pushButton_17.setEnabled(True)

        self.ui.pushButton_16.setEnabled(True)

        self.ui.pushButton_13.setEnabled(True)

        self.ui.pushButton_8.setEnabled(True)

        self.ui.pushButton_7.setEnabled(True)

        self.ui.pushButton_6.setEnabled(True)

        self.ui.pushButton_5.setEnabled(True)

        self.ui.pushButton_4.setEnabled(True)  
        
    def wip(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Message')
        msg.setText('Work in progress.')
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()

 
