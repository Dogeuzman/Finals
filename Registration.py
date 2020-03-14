from sqlitedict import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

class Registration(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "User Registation"
        self.x = 750
        self.y = 350
        self.width = 400
        self.height = 400

        self.userrecorddb = SqliteDict("user_register.db", autocommit = True)
        self.record = self.userrecorddb.get('self.record',[])
        self.UserInterface()

    def UserInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('sage'))

        self.titlelbl = QLabel ("Fill up the following:", self)
        self.titlelbl.move(160, 20)

        self.fnamelbl = QLabel ("First Name", self)
        self.fnamelbl.move(80, 60)
        self.fnametxt = QLineEdit(self)
        self.fnametxt.move (180, 58)
        self.fnametxt.resize (150, 20)
        self.fnametxt.setPlaceholderText("Input your First Name")

        self.lnamelbl = QLabel ("Last Name", self)
        self.lnamelbl.move(80, 90)
        self.lnametxt = QLineEdit(self)
        self.lnametxt.move (180, 88)
        self.lnametxt.resize (150, 20)
        self.lnametxt.setPlaceholderText("Input your Last Name")

        self.usernamelbl = QLabel ("Username", self)
        self.usernamelbl.move(80, 120)
        self.usernametxt = QLineEdit(self)
        self.usernametxt.move (180, 118)
        self.usernametxt.resize (150, 20)
        self.usernametxt.setPlaceholderText("Input your Username")

        self.passlbl = QLabel ("Password", self)
        self.passlbl.move(80, 150)
        self.passtxt = QLineEdit(self)
        self.passtxt.setEchoMode(QLineEdit.Password)
        self.passtxt.move (180, 148)
        self.passtxt.resize (150, 20)
        self.passtxt.setPlaceholderText("Input your Password")

        self.emaillbl = QLabel ("Email", self)
        self.emaillbl.move(80, 180)
        self.emailtxt = QLineEdit(self)
        self.emailtxt.move (180, 178)
        self.emailtxt.resize (150, 20)
        self.emailtxt.setPlaceholderText("Input your Email")

        self.contactlbl = QLabel ("Contact Number", self)
        self.contactlbl.move(80, 210)
        self.contacttxt = QLineEdit(self)
        self.contacttxt.move (180, 208)
        self.contacttxt.resize (150, 20)
        self.contacttxt.setPlaceholderText("Input your Contact Number")
        
        self.subbttn = QPushButton('Submit', self)
        self.subbttn.setToolTip("Click if you want to go to the next step.")
        self.subbttn.move(80, 300) #button.move(x,y)
        self.subbttn.clicked.connect(self.submit)
        
        self.shwbttn = QPushButton('Show', self)
        self.shwbttn.setToolTip("Click if you want to see your account.")
        self.shwbttn.move(170, 300) #button.move(x,y)
        self.shwbttn.clicked.connect(self.showUsers)

        self.clrbttn = QPushButton('Clear', self)
        self.clrbttn.setToolTip("Click if you want to clear submisssion.")
        self.clrbttn.move(260, 300) #button.move(x,y)
        self.clrbttn.clicked.connect(self.clear)

        self.show()
        
    def submit(self):
        registration_list=[{'First Name': self.fnametxt.text()}, {'Last Name': self.lnametxt.text()}, {'Username': self.usernametxt.text()},
                            {'Password': self.passtxt.text()}, {'Email': self.emailtxt.text()}, {'Contact Number': self.contacttxt.text()}]
        
        buttonReply = QMessageBox.question(self, "Submit", "Are you sure you want to submit?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if (self.fnametxt.text() == '') and (self.lnametxt.text() == '') and (self.usernametxt.text() == '') and (self.passtxt.text() == '') and (self.emailtxt.text() == '') and (self.contacttxt.text() == ''):
            QMessageBox.warning(self, "Error!", "Please fill up all the boxes.", QMessageBox.Ok, QMessageBox.Ok)
        
        elif (self.fnametxt.text() == '') or (self.lnametxt.text() == '') or (self.usernametxt.text() == '') or (self.passtxt.text() == '') or (self.emailtxt.text() == '') or (self.contacttxt.text() == ''):
            for registration in registration_list:
                for key, value in registration.items():
                    if value == '':
                        QMessageBox.warning(self, "Error!", f"Please fill up {key}.", QMessageBox.Ok, QMessageBox.Ok)
        
        elif buttonReply == QMessageBox.No:
            QMessageBox.warning(self, "Program will Exit", "You clicked no.", QMessageBox.Ok, QMessageBox.Ok)
            sys.exit(app.exec_())
                
        elif buttonReply == QMessageBox.Yes:
                self.record.append({'First Name': self.fnametxt.text().title(), 
                                    'Last Name': self.lnametxt.text().title(), 
                                    'Username': self.usernametxt.text(),
                                    'Password': self.passtxt.text(), 
                                    'Email': self.emailtxt.text(), 
                                    'Contact Number': self.contacttxt.text()
                                    })
                self.userrecorddb["record"] = self.record
                QMessageBox.information(self, "Acknowleged.", "You have successfully made an account!", QMessageBox.Ok, QMessageBox.Ok)
                
       
                
    def showUsers(self):
        for record in self.record:
            for key, value in record.items():
                print(f"{key}: {value}")
            print('')
                
    def clear(self):
        self.fnametxt.clear()
        self.lnametxt.clear()
        self.usernametxt.clear()
        self.passtxt.clear()
        self.emailtxt.clear()
        self.contacttxt.clear()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registration() 
    sys.exit(app.exec_())        
