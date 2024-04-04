from PyQt5 import QtCore, QtGui, QtWidgets
import os
from datetime import datetime

ohi = ''

def otrez_lihnee(a):
    a1 = ''
    for i in a:
        if i == ':':
            a1 += ';'
        elif i != '.':
            a1 += i
        else:
            return a1
    return a1

def sravnenie(a):
    b = ui.lineEdit_tip.text()
    if len(b) == 0:
        teh_stroka('увы. нет типа файла.')
        return False
    a = a.lower()
    b = b.lower()
    tip_fa = ''
    t = False
    for i in a:
        if t == True:
            tip_fa += i
        if i == '.':
            t = True
    if b == tip_fa:
        return True
    else:
        return False

def obr_papk(de='.'):
    spis_0 = os.listdir(de)
    adr = []
    for i in spis_0:
        if sravnenie(i):
            adr.append(i)
        elif os.path.isdir(str(de)+'/'+str(i)) and i != '.idea' and i != 'build' and i != 'nazv_2.py' \
                and ui.checkBox_5.isChecked() == True:
            obr_papk(de=f'{de}/{str(i)}')
    obrabot.setdefault(de, adr)

def form_nev(r, t):
    l_nev = ''
    if ui.checkBox_3.isChecked() == True:
        l_nev += f'[{t[0]}]_'
    if ui.checkBox_4.isChecked() == True:
        l_nev += f'[{t[0]}]_'
    if len(ui.lineEdit_nazv.text()) > 0:
        l_nev += f'{ui.lineEdit_nazv.text()}_'
    l_nev += f'{str(r)}'
    if ui.checkBox.isChecked() == True:
        l_nev += f'[{t[0]}]_'
    if ui.checkBox_2.isChecked() == True:
        l_nev += f'[{t[1]}]_'
    l_nev += f'.{ui.lineEdit_tip.text().lower()}'
    return l_nev

def izm_nazv(SYDA):
    for i in obrabot:
        r = 1
        for l in obrabot[i]:
            old_file = os.path.join(i, l)
            t = ['']
            if ui.checkBox.isChecked() == True or ui.checkBox_2.isChecked() == True or\
            ui.checkBox_3.isChecked() == True or ui.checkBox_4.isChecked() == True:
                mtime = os.path.getmtime(old_file)
                mtime_readable = datetime.fromtimestamp(mtime)
                t = otrez_lihnee(str(mtime_readable))
                t = t.split(" ")
            l_nev = form_nev(r, t)
            if SYDA == True:
                kyda = '.'
            else:
                kyda = i
            new_file = os.path.join(kyda, l_nev)
            os.rename(old_file, new_file)
            r += 1


def teh_stroka(a):
    global ohi
    ohi = a
    ui.setupUi(MainWindow)

def kno(a):
    global obrabot
    obrabot = dict()
    obr_papk()
    izm_nazv(a)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        font_1, font_2, font_3 = QtGui.QFont(), QtGui.QFont(), QtGui.QFont()
        spisok_font = [[font_1, 16, True, 75], [font_2, 12, True, 75], [font_3, 8, False, 50]]
        for i in range(len(spisok_font)):
            spisok_font[i][0].setFamily("Segoe Print")
            spisok_font[i][0].setPointSize(spisok_font[i][1])
            spisok_font[i][0].setBold(spisok_font[i][2])
            spisok_font[i][0].setWeight(spisok_font[i][3])

        self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5 = \
            QtWidgets.QCheckBox(self.centralwidget), QtWidgets.QCheckBox(self.centralwidget), \
            QtWidgets.QCheckBox(self.centralwidget), QtWidgets.QCheckBox(self.centralwidget), \
            QtWidgets.QCheckBox(self.centralwidget)
        self.spis_cB= [[self.checkBox, 500, 70], [self.checkBox_2, 560, 70], [self.checkBox_3, 40, 70],
                       [self.checkBox_4, 100, 70], [self.checkBox_5, 40, 145]]
        for i in self.spis_cB:
            i[0].setGeometry(QtCore.QRect(i[1], i[2], 20, 20))
            i[0].setText("")
            i[0].setIconSize(QtCore.QSize(16, 16))
            i[0].setCheckState(2)

        self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, \
            self.label_7, self.label_8, self.label_9,\
            self.pushButton, self.pushButton_2, self.lineEdit_nazv, self.lineEdit_tip =\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget), \
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget), \
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget), \
            QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QPushButton(self.centralwidget), QtWidgets.QPushButton(self.centralwidget), \
            QtWidgets.QLineEdit(self.centralwidget), QtWidgets.QLineEdit(self.centralwidget)
        self.spisok_l = [[self.label, 150, 25, 80, 20, font_2, 'название'],
                         [self.label_2, 480, 50, 50, 20, font_2, 'дата'],
                         [self.label_3, 540, 50, 60, 20, font_2, 'время'],
                         [self.label_7, 20, 50, 50, 20, font_2, 'дата'],
                         [self.label_8, 80, 50, 60, 20, font_2, 'время'],
                         [self.label_4, 620, 25, 80, 20, font_2, 'формат'],
                         [self.label_5, 580, 200, 180, 20, font_3, 'разработчик: Тарасов Д.Л.'],
                         [self.label_6, 150, 190, 300, 30, font_1, ohi],
                         [self.label_9, 65, 142, 80, 20, font_2, 'в глубь'],
                         [self.pushButton, 515, 130, 150, 50, font_1, 'делать.'],
                         [self.pushButton_2, 250, 130, 150, 50, font_1, 'все сюда!'],
                         [self.lineEdit_nazv, 150, 50, 300, 50, font_1, ''],
                         [self.lineEdit_tip, 620, 50, 45, 50, font_1, 'jpg']]
        for i in self.spisok_l:
            i[0].setGeometry(QtCore.QRect(i[1], i[2], i[3], i[4]))
            i[0].setFont(i[5])

        self.pushButton.clicked.connect(lambda: kno(False))
        self.pushButton_2.clicked.connect(lambda: kno(True))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "переименование"))
        for i in self.spisok_l:
            i[0].setText(_translate("MainWindow", i[6]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())