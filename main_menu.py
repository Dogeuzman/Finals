from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
import math
from conic_sections import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,250,250)
        self.setWindowTitle("Conic Sections")
        self.setWindowIcon(QIcon('yinyang_icon.ico'))
        self.loadmenu()
        self.loadwidget()
        self.show()
    

    def loadmenu(self):
        mainMenu = self.menuBar()
        optionMenu = mainMenu.addMenu('Options')

        exitButton = QAction('Exit',self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.triggered.connect(self.close)
        optionMenu.addAction(exitButton)

    def loadwidget(self):
        self.MainMenu = MainMenu()
        self.setCentralWidget(self.MainMenu)
        

class MainMenu(QWidget):
    def __init__(self):
        super(MainMenu,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        
        titlelbl = QLabel("CONIC SECTION PARTS CALCULATOR",self)

        identifier_btn = QPushButton("Conic type identifier",self)
        identifier_btn.clicked.connect(self.identifier)

        circle_btn = QPushButton("Circle",self)
        circle_btn.clicked.connect(self.circleWindow)

        parabola_btn = QPushButton("Parabola",self)
        parabola_btn.clicked.connect(self.parabolaWindow)

        ellipse_btn = QPushButton("Ellipse",self)
        ellipse_btn.clicked.connect(self.ellipseWindow)

        hyperbola_btn = QPushButton("Hyperbola",self)
        hyperbola_btn.clicked.connect(self.hyperbolaWindow)

        list_buttons = (identifier_btn,circle_btn,parabola_btn,ellipse_btn,hyperbola_btn)
        vbox.addWidget(titlelbl)

        vbox.addStretch()
        for button in list_buttons:
            vbox.addWidget(button)
        vbox.addStretch()

    def circleWindow(self):
        self.circle_dialog = CircleWindow()
        self.circle_dialog.show()

    def parabolaWindow(self):
        self.parabola_dialog = ParabolaWindow()
        self.parabola_dialog.show()

    def ellipseWindow(self):
        self.ellipse_dialog = EllipseWindow()
        self.ellipse_dialog.show()

    def hyperbolaWindow(self):
        self.hyperbola_dialog = HyperbolaWindow()
        self.hyperbola_dialog.show()

    def identifier(self):
        self.identifier_dialog = IdentifierWindow()
        self.identifier_dialog.show()


class CircleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle")
        self.setGeometry(300,300,250,250)
        self.initUI()
        
    
    def initUI(self):
        xpluslabel = QLabel("( X +",self)
        xpluslabel.move(30,30)
        self.htextbox = QLineEdit(self)
        self.htextbox.setGeometry(55,30,20,15)
        cplabel = QLabel(")² +",self)
        cplabel.move(76,30)
        ypluslabel = QLabel("( Y +",self)
        ypluslabel.move(100,30)
        self.ktextbox = QLineEdit(self)
        self.ktextbox.setGeometry(125,30,20,15)
        cp2label = QLabel(")²",self)
        cp2label.move(146,30)
        equallbl = QLabel(" = ",self)
        equallbl.move(160,30)
        self.equaltxtbox = QLineEdit(self)
        self.equaltxtbox.setGeometry(175,30,20,15)
        calculate_button = QPushButton("Calculate",self)
        calculate_button.clicked.connect(self.calculateCircleParts)
        view_graph_button = QPushButton("View Graph",self)
        view_graph_button.clicked.connect(self.graphCircle)
        view_graph_button.move(50,50)


    def calculateCircleParts(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.r = (int(self.equaltxtbox.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            print(self.h,self.k)

            radius = math.sqrt(self.r)
            diameter = 2*radius
            endpt1 = (self.h+radius,self.k)
            endpt2 = (self.h-radius,self.k)
            endpt3 = (self.h,self.k+radius)
            endpt4 = (self.h,self.k-radius)
            information = f"CENTER ({self.h},{self.k}) RADIUS = {radius} DIAMETER = {diameter} Endpoints {endpt1},{endpt2},{endpt3},{endpt4}"
            answerBox = QMessageBox.information(self, "Answer", information, QMessageBox.Ok, QMessageBox.Ok)
    
    def graphCircle(self):
        try:
            circle(self.h, self.k, self.r)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)
        

class ParabolaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parabola")
        self.setGeometry(300,300,250,250)
        self.initUI()
    
    def initUI(self):
        upOrDownChoice = QMessageBox.question(self, "Question", "Is your parabola upward or downward?", QMessageBox.Yes, QMessageBox.No)
        if upOrDownChoice == QMessageBox.Yes:
            xpluslabel = QLabel("( X +",self)
            xpluslabel.move(30,30)
            self.htextbox = QLineEdit(self)
            self.htextbox.setGeometry(55,30,20,15)
            cplabel = QLabel(")²  =",self)
            cplabel.move(76,30)
            self.fourP = QLineEdit(self)
            self.fourP.setGeometry(105,30,20,15)
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.move(130,30)
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setGeometry(155,30,20,15)
            cp2label = QLabel(")",self)
            cp2label.move(176,30)
            calculate_button = QPushButton("Calculate",self)
            calculate_button.clicked.connect(self.calculateUpDownParabolaParts)
            view_graph_button = QPushButton("View Graph",self)
            view_graph_button.move(50,50)
            view_graph_button.clicked.connect(self.graphUpDownParabola)
        else:
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.move(30,30)
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setGeometry(55,30,20,15)
            cplabel = QLabel(")²  =",self)
            cplabel.move(76,30)
            self.fourP = QLineEdit(self)
            self.fourP.setGeometry(105,30,20,15)
            xpluslabel = QLabel("( X +",self)
            xpluslabel.move(130,30)
            self.htextbox = QLineEdit(self)
            self.htextbox.setGeometry(155,30,20,15)
            cp2label = QLabel(")",self)
            cp2label.move(176,30)
            calculate_button = QPushButton("Calculate",self)
            calculate_button.clicked.connect(self.calculateRightLeftParabolaParts)
            view_graph_button = QPushButton("View Graph",self)
            view_graph_button.move(50,50)
            view_graph_button.clicked.connect(self.graphRightLeftParabola)
    
    def calculateUpDownParabolaParts(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.fourp = (int(self.fourP.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            vertex = (self.h,self.k)
            focus = (self.h, self.k+(self.fourp/4))
            directrix = (-(self.fourp/4))+self.k
            lengthLR = (self.fourp)
            endptLRA = (self.h+(2*(self.fourp/4)),self.k)
            endptLRB = (self.h-(2*(self.fourp/4)),self.k)
            information = f'VERTEX {vertex} FOCUS {focus} DIRECTRIX y = {directrix}x LENGTH OF LR {lengthLR} ENDPOINT-A LR {endptLRA} ENDPOINT-B LR {endptLRB}'
            QMessageBox.information(self, "Answer",information, QMessageBox.Ok, QMessageBox.Ok)

    def calculateRightLeftParabolaParts(self):
        try:
            self.hPRL = -(int(self.htextbox.text()))
            self.kPRL = -(int(self.ktextbox.text()))
            self.fourpPRL = (int(self.fourP.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            vertex = (self.hPRL,self.kPRL)
            focus = (self.hPRL+(self.fourpPRL/4), self.kPRL)
            directrix = (-(self.fourpPRL/4))+self.hPRL
            lengthLR = (self.fourpPRL)
            endptLRA = (self.hPRL,self.kPRL+(2*(self.fourpPRL/4)))
            endptLRB = (self.hPRL,self.kPRL-(2*(self.fourpPRL/4)))

            information = f'VERTEX {vertex} FOCUS {focus} DIRECTRIX x = {directrix}y LENGTH OF LR {lengthLR} ENDPOINT-A LR {endptLRA} ENDPOINT-B LR {endptLRB}'
            QMessageBox.information(self, "Answer",information, QMessageBox.Ok, QMessageBox.Ok)

    def graphUpDownParabola(self):
        try:
            upDownParabola(self.h,self.k,self.fourp)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)
    
    def graphRightLeftParabola(self):
        try:
            rightLeftParabola(self.hPRL,self.kPRL,self.fourpPRL)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)
        

class EllipseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ellipse")
        self.setGeometry(300,300,250,250)
        self.initUI()
    
    def initUI(self):
        XOrYChoice = QMessageBox.question(self, "Question", "Is the major axis of your ellipse lies on X axis?", QMessageBox.Yes, QMessageBox.No)
        if XOrYChoice == QMessageBox.Yes:
            xpluslabel = QLabel("( X +",self)
            xpluslabel.move(30,30)
            self.htextbox = QLineEdit(self)
            self.htextbox.setGeometry(55,30,20,15)
            cplabel = QLabel(")² +",self)
            cplabel.move(76,30)
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.move(100,30)
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setGeometry(125,30,20,15)
            cp2label = QLabel(")²",self)
            cp2label.move(146,30)
            equallbl = QLabel(" = ",self)
            equallbl.move(160,30)
            equal1 = QLabel('1',self)
            equal1.setGeometry(175,30,20,15)
            _x  = QLabel("________",self)
            _x.move(30,35)
            _y  = QLabel("________",self)
            _y.move(100,35)
            self.aBox = QLineEdit(self)
            self.aBox.setGeometry(45,50,20,15)
            self.bBox = QLineEdit(self)
            self.bBox.setGeometry(115,50,20,15)
            calculate_button = QPushButton("Calculate",self)
            view_graph_button = QPushButton('View Graph',self)
            view_graph_button.move(100,100)
            calculate_button.clicked.connect(self.calculateEllipseXmajParts)
            view_graph_button.clicked.connect(self.graphEllipseXMaj)
        else:
            xpluslabel = QLabel("( Y +",self)
            xpluslabel.move(30,30)
            self.htextbox = QLineEdit(self)
            self.htextbox.setGeometry(55,30,20,15)
            cplabel = QLabel(")² +",self)
            cplabel.move(76,30)
            ypluslabel = QLabel("( X +",self)
            ypluslabel.move(100,30)
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setGeometry(125,30,20,15)
            cp2label = QLabel(")²",self)
            cp2label.move(146,30)
            equallbl = QLabel(" = ",self)
            equallbl.move(160,30)
            equal1 = QLabel('1',self)
            equal1.setGeometry(175,30,20,15)
            _x  = QLabel("________",self)
            _x.move(30,35)
            _y  = QLabel("________",self)
            _y.move(100,35)
            self.aBox = QLineEdit(self)
            self.aBox.setGeometry(45,50,20,15)
            self.bBox = QLineEdit(self)
            self.bBox.setGeometry(115,50,20,15)
            calculate_button = QPushButton("Calculate",self)
            view_graph_button = QPushButton('View Graph',self)
            view_graph_button.move(100,100)
            calculate_button.clicked.connect(self.calculateEllipseYmajParts)
            view_graph_button.clicked.connect(self.graphEllipseYMaj)
        

    def calculateEllipseXmajParts(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.a = (int(self.aBox.text()))
            self.b = (int(self.bBox.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.a > self.b:
                c = ((self.b)**2 - (self.a)**2)**(1/2)
                center = (self.h,self.k)
                focus1 = (self.h+c,self.k)
                focus2 = (self.h-c,self.k)
                vertex1 = (self.h+self.a,self.k)
                vertex2 = (self.h-self.a,self.k)
                lengthLR = (2*(self.b**2))/self.a
                lr1 = (self.b**2)/self.a
                lr2 = -(self.b**2)/self.a 
                endpt1LRA = (self.h+c,self.k+lr1)
                endpt2LRA = (self.h+c,self.k+lr2)
                endpt1LRB = (self.h-c,self.k+lr1)
                endpt2LRB = (self.h-c,self.k+lr2)
                eccentricity = c/self.a
            else:
                QMessageBox.warning(self, "Error", "Value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)
    
    def graphEllipseXMaj(self):
        try:
            if self.a > self.b:
                ellipseXmaj(self.a,self.b,self.h,self.k)
            else:
                QMessageBox.warning(self, "Error", "Value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)

    def calculateEllipseYmajParts(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.a = (int(self.aBox.text()))
            self.b = (int(self.bBox.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.b > self.a:
                c = ((self.b)**2 - (self.a)**2)**(1/2)
                center = (self.h,self.k)
                focus1 = (self.h,self.k+c)
                focus2 = (self.h,self.k-c)
                vertex1 = (self.h,self.k+self.b)
                vertex2 = (self.h,self.k-self.b)
                lengthLR = (2*(self.a**2))/self.b
                lr1 = (self.a**2)/self.b
                lr2 = -(self.a**2)/self.b 
                endpt1LRA = (self.h+lr1,self.k+c)
                endpt2LRA = (self.h+lr2,self.k+c)
                endpt1LRB = (self.h+lr1,self.k-lr1)
                endpt2LRB = (self.h+lr2,self.k-lr2)
                eccentricity = c/self.a
            else:
                QMessageBox.warning(self, "Error", "Value of B must be greater than A", QMessageBox.Ok, QMessageBox.Ok)

    def graphEllipseYMaj(self):
        try:
            if self.a > self.b:
                ellipseYmaj(self.a,self.b,self.h,self.k)
            else:
                QMessageBox.warning(self, "Error", "Value of B must be greater than A", QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)
    

class HyperbolaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hyperbola")
        self.setGeometry(300,300,250,250)
        self.initUI()
    
    def initUI(self):
        XOrYChoice = QMessageBox.question(self, "Question", "Is your major axis on X-Axis?", QMessageBox.Yes, QMessageBox.No)
        if XOrYChoice == QMessageBox.Yes:
            xpluslabel = QLabel("( X +",self)
            xpluslabel.move(30,30)
            self.htextbox = QLineEdit(self)
            self.htextbox.setGeometry(55,30,20,15)
            cplabel = QLabel(")² -",self)
            cplabel.move(77,30)
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.move(100,30)
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setGeometry(125,30,20,15)
            cp2label = QLabel(")²",self)
            cp2label.move(146,30)
            equallbl = QLabel(" = ",self)
            equallbl.move(160,30)
            equal1 = QLabel('1',self)
            equal1.move(175,30)
            _x  = QLabel("________",self)
            _x.move(30,35)
            _y  = QLabel("________",self)
            _y.move(100,35)
            self.aBox = QLineEdit(self)
            self.aBox.setGeometry(45,50,20,15)
            self.bBox = QLineEdit(self)
            self.bBox.setGeometry(115,50,20,15)
            calculate_button = QPushButton("Calculate",self)
            calculate_button.clicked.connect(self.calculateHyperbolaXmaj)
            view_graph_button = QPushButton("View",self)
            view_graph_button.move(100,100)
            view_graph_button.clicked.connect(self.graphHyperbolaXmaj)

        elif XOrYChoice == QMessageBox.No:
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.move(30,30)
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setGeometry(55,30,20,15)
            cplabel = QLabel(")² -",self)
            cplabel.move(77,30)
            xpluslabel = QLabel("( X +",self)
            xpluslabel.move(100,30)
            self.htextbox = QLineEdit(self)
            self.htextbox.setGeometry(125,30,20,15)
            cp2label = QLabel(")²",self)
            cp2label.move(146,30)
            equal1 = QLabel('1',self)
            equal1.move(175,30)
            _x  = QLabel("________",self)
            _x.move(30,35)
            _y  = QLabel("________",self)
            _y.move(100,35)
            self.aBox = QLineEdit(self)
            self.aBox.setGeometry(45,50,20,15)
            self.bBox = QLineEdit(self)
            self.bBox.setGeometry(115,50,20,15)
            calculate_button = QPushButton("Calculate",self)
            calculate_button.clicked.connect(self.calculateHyperbolaYmaj)
            view_graph_button = QPushButton("View",self)
            view_graph_button.move(100,100)
            view_graph_button.clicked.connect(self.graphHyperbolaYmaj)

    def calculateHyperbolaXmaj(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.a = (int(self.aBox.text()))
            self.b = (int(self.bBox.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.a >= self.b:
                c = ((self.b**2)+(self.a**2))**(1/2)
                center = (self.h,self.k)
                focus1 = (self.h,self.k+c)
                focus2 = (self.h,self.k-c)
                vertex1 = (self.h,self.k+self.a)
                vertex2 = (self.h,self.k-self.a)
            else:
                QMessageBox.warning(self, "Error", "The value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)

    def graphHyperbolaXmaj(self):
        try:
            if self.a > self.b:
                hyperbolaXmaj(self.a,self.b,self.h,self.k)
            else:
                QMessageBox.warning(self, "Error", "The value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)
    
    def calculateHyperbolaYmaj(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.a = (int(self.aBox.text()))
            self.b = (int(self.bBox.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.b >= self.a:
                c = ((self.b**2)+(self.a**2))**(1/2)
                center = (self.h,self.k)
                focus1 = (self.h+c,self.k)
                focus2 = (self.h-c,self.k)
                vertex1 = (self.h+self.a,self.k)
                vertex2 = (self.h-self.a,self.k)
            else:
                QMessageBox.warning(self, "Error", "The value of B must be greater than A", QMessageBox.Ok, QMessageBox.Ok)

    def graphHyperbolaYmaj(self):
        try:
            if self.b > self.a:
                hyperbolaYmaj(self.a,self.b,self.h,self.k)
            else:
                QMessageBox.warning(self, "Error", "The value of B must be greater than A", QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)


class IdentifierWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conic Identifier")
        self.setGeometry(300,300,250,250)
        self.initUI()
    
    def initUI(self):
        self.hbox = QHBoxLayout()
        self.hbox.addStretch()
        self.setLayout(self.hbox)
        self.list_of_textbox = []
        

        names = ('', 'x² +', '', 'xy+','','y²+','','x+','','y','','=','0')
        # using a loop to generate positions
        for name in names:
            if name == '':
                self.textbox = QLineEdit(self)
                self.textbox.setFixedSize(20,15)
                self.list_of_textbox.append(self.textbox)
                self.hbox.addWidget(self.textbox)
            else:
                character = QLabel(name)
                self.hbox.addWidget(character)
        
        calculate_button = QPushButton("Identify!",self)
        calculate_button.clicked.connect(self.identifierMethod)

    def identifierMethod(self):
        try:
            A = int(self.list_of_textbox[0].text())
            B = int(self.list_of_textbox[1].text())
            C = int(self.list_of_textbox[2].text())
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            discriminant = (B**2)-(4*A*C)

            if (discriminant<0) and ((B == 0) and (A == C)):
                QMessageBox.information(self, "Identified!", f"The equation has a type of CIRCLE which has a determinant of {discriminant}", QMessageBox.Ok, QMessageBox.Ok)
            elif (discriminant<0) and ((B!=0) or (A!=C)):
                QMessageBox.information(self, "Identified!", f"The equation has a type of ELLIPSE which has a determinant of {discriminant}", QMessageBox.Ok, QMessageBox.Ok)
            elif discriminant>0:
                QMessageBox.information(self, "Identified!", f"The equation has a type of HYPERBOLA which has a determinant of {discriminant}", QMessageBox.Ok, QMessageBox.Ok)
            elif discriminant == 0:
                QMessageBox.information(self, "Identified!", f"The equation has a type of PARABOLA which has a determinant of {discriminant}", QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Error", "The equation is not a conic section!", QMessageBox.Ok, QMessageBox.Ok)
         
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())