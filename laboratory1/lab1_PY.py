from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 676)
        MainWindow.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 220, 256, 192))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(450, 220, 256, 192))
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 300, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 260, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Привязка кнопок к функциям
        self.pushButton.clicked.connect(self.delete_file)
        self.pushButton_2.clicked.connect(self.create_file)
        self.pushButton_3.clicked.connect(self.move_file)

        # Инициализация папок 
        self.source_dir = "source_folder"
        self.target_dir = "target_folder"
        self.load_files()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Файловая система"))
        self.pushButton.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_2.setText(_translate("MainWindow", "Создать"))
        self.pushButton_3.setText(_translate("MainWindow", "Перенести"))

    def load_files(self):
        """Загрузка файлов в списки"""
        self.listWidget.clear()
        self.listWidget_2.clear()

        # Загрузка файлов из исходной папки
        if os.path.exists(self.source_dir):
            for file_name in os.listdir(self.source_dir):
                self.listWidget.addItem(file_name)

        # Загрузка файлов из целевой папки
        if os.path.exists(self.target_dir):
            for file_name in os.listdir(self.target_dir):
                self.listWidget_2.addItem(file_name)

    def create_file(self):
        """Создание файла с указанным именем и расширением"""
        text, ok = QInputDialog.getText(self.centralwidget, 'Создать файл', 'Введите имя файла с расширением:')
        if ok and text:
            file_path = os.path.join(self.source_dir, text)
            try:
                with open(file_path, 'w') as file:
                    file.write('')  # Создаем пустой файл
                self.load_files()
            except Exception as e:
                QMessageBox.critical(self.centralwidget, 'Ошибка', f'Не удалось создать файл: {str(e)}')

    def delete_file(self):
        """Удаление выбранного файла"""
        selected_item = self.listWidget.currentItem()
        if selected_item:
            file_name = selected_item.text()
            file_path = os.path.join(self.source_dir, file_name)
            try:
                os.remove(file_path)
                self.load_files()
            except Exception as e:
                QMessageBox.critical(self.centralwidget, 'Ошибка', f'Не удалось удалить файл: {str(e)}')
        else:
            QMessageBox.warning(self.centralwidget, 'Предупреждение', 'Файл не выбран')

    def move_file(self):
        """Перенос файла из одной папки в другую"""
        selected_item = self.listWidget.currentItem()
        if selected_item:
            file_name = selected_item.text()
            source_path = os.path.join(self.source_dir, file_name)
            target_path = os.path.join(self.target_dir, file_name)
            try:
                shutil.move(source_path, target_path)
                self.load_files()
            except Exception as e:
                QMessageBox.critical(self.centralwidget, 'Ошибка', f'Не удалось перенести файл: {str(e)}')
        else:
            QMessageBox.warning(self.centralwidget, 'Предупреждение', 'Файл не выбран')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

