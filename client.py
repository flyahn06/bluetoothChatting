from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
import sys

class BluetoothChattingClient(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralwidget = QtWidgets.QWidget(self)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.usertable = QtWidgets.QTableView(self.centralwidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.userinput = QtWidgets.QLineEdit(self.centralwidget)
        self.sendbutton = QtWidgets.QPushButton(self.centralwidget)
        self.chattextbox = QtWidgets.QTextBrowser(self.centralwidget)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(778, 441)

        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.usertable.setObjectName("usertable")
        self.gridLayout.addWidget(self.usertable, 0, 2, 1, 1)

        self.horizontalLayout.setObjectName("horizontalLayout")

        self.userinput.setObjectName("userinput")
        self.horizontalLayout.addWidget(self.userinput)

        self.sendbutton.setText("전송")
        self.sendbutton.setObjectName("sendbutton")
        self.horizontalLayout.addWidget(self.sendbutton)

        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 2)

        self.chattextbox.setObjectName("chattextbox")
        self.gridLayout.addWidget(self.chattextbox, 0, 1, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.setWindowTitle("블루투스 채팅 클라이언트")

        self.chattextbox.append("안동기: 우리는 자습실에서 채팅을 할 권리가 있습니다!")
        self.chattextbox.append("조용히 해라!")


app = QtWidgets.QApplication(sys.argv)
ui = BluetoothChattingClient()
ui.setupUi()
ui.show()
sys.exit(app.exec_())
