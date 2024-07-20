import sys
import mysql.connector
from PyQt6.QtWidgets import* 
from PyQt6.QtCore import QRect
from PyQt6.QtGui import QGuiApplication
QApplication , QHBoxLayout ,  QVBoxLayout , QWidget , QLabel , QTableView,QTextEdit , QLayout , QLineEdit , QPushButton,QMessageBox
from PyQt6.QtCore import QPropertyAnimation
from dictionarry_py import mydictionary


class Mydictionary(QWidget):
       
       def __init__(self) -> None:
              super().__init__()
              
              self.child_dict = None
              self.child_trans = None
              self.table1 = None
              
              self.setWindowTitle("Longman")
              
              self.label = QLabel()
       
              self.button1   = QPushButton("Show all words")
              self.button2   = QPushButton("Add new word")
              self.button3   = QPushButton("Search")
              self.button4   = QPushButton("Exit")
              
              self.setGeometry(100, 100, 450, 450)
             
              self.button1.resize(250, 100)
              self.button2.resize(250, 100)
              self.button3.resize(250, 100)
              self.button4.resize(250, 100)
              
              self.button1.setStyleSheet("background-color: blue; color: white; font-size: 30px;")
              self.button2.setStyleSheet("background-color:  blue; color: white; font-size: 30px;")
              self.button3.setStyleSheet("background-color: red; color: white; font-size: 30px;")
              self.button4.setStyleSheet("background-color: red; color: white; font-size: 30px;")
              self.setStyleSheet('background-color: black-yellow;')
              
              self.h1 = QHBoxLayout()
              self.h1.addWidget(self.button1)
              
              self.h2 = QHBoxLayout()
              self.h2.addWidget(self.button2)
              
              self.h3 = QHBoxLayout()
              self.h3.addWidget(self.button3
                                )
              self.h4 = QHBoxLayout()
              self.h4.addWidget(self.button4)
              
              self.v = QVBoxLayout()
              self.v.addLayout(self.h1)
              self.v.addLayout(self.h2)
              self.v.addLayout(self.h3)
              self.v.addLayout(self.h4)
              
              self.setLayout(self.v)
              
              self.button1.clicked.connect(self.showall)
              self.button2.clicked.connect(self.addwords)
              self.button3.clicked.connect(self.search_options)
              self.button4.clicked.connect(self.close)
            
              
       def showall(self):
              
              d = mydictionary()
              data = d.get_all()
            
            
              if     self.table1 is None:
                     self.table1 = table1(data)
                     self.table1.show()
              else:
                     self.table1.close()
                     self.table1 = None
                     
       def addwords(self):
              
              if     self.child_dict is None:
                     self.child_dict = ChildDictionary()
                     self.child_dict.show()
              else:
                     self.child_dict.close()
                     self.child_dict = None
       def search_options(self):
              if     self.child_trans is None:
                     self.child_trans = Translation()
                     self.child_trans.show()
              else:
                     self.child_trans.close()
                     self.child_trans = None
      
                     
class table1(QWidget):
    def __init__(self, data):
        super().__init__()

        self.setWindowTitle("Translation")
        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["ENG", "UZB"])

        self.table.setStyleSheet('''
            QTableWidget {
                border: 2px solid black;
                border-radius: 5px;
            }

            QTableWidget::item {
                padding: 10px;
            }

            QTableWidget::item:selected {
                background-color: yellow;
                color: black;
            }

            QTableWidget::item:focus {
                background-color: lightblue;
                color: black;
            }
        ''')

        layout.addWidget(self.table)

        lst = [0, 1]
        line = 0

        for word in data:
            for i, j in zip(lst, word):
                self.table.setItem(line, i, QTableWidgetItem(j))
            line += 1

        self.setLayout(layout)

    def showEvent(self, event):
        super().showEvent(event)
        self.resize_to_screen()

    def resize_to_screen(self):
       available_rect = QGuiApplication.primaryScreen().availableGeometry()
       self.setGeometry(available_rect)
class ChildDictionary(QWidget):
       
       def __init__(self) -> None:
              super().__init__()
              
       
              self.child_dict = None
              
              self.linedit1 = QLineEdit()
              self.linedit2 = QLineEdit()
              
              self.linedit1.setPlaceholderText("Uzb...")
              self.linedit2.setPlaceholderText("Eng...")
              
              self.btn = QPushButton("Save")

              self.h = QHBoxLayout()
              self.h.addWidget(self.linedit1)
              
              self.h1 = QHBoxLayout()
              self.h1.addWidget(self.linedit2)
              
              self.h2 = QHBoxLayout()
              self.h2.addWidget(self.btn)

              
              self.ver = QVBoxLayout()
              self.ver.addLayout(self.h)
              self.ver.addLayout(self.h1)
              self.ver.addLayout(self.h2)
              
              
              self.setLayout(self.ver)
              
              self.btn.clicked.connect(self.addnewword)
              self.btn.setShortcut('enter')
              
   
       def addnewword(self):
         
              
              uz = self.linedit1.text()
              en = self.linedit2.text()
              d = mydictionary()
              
              d.add_words(en , uz)
              msg = QMessageBox(self)
              msg.setWindowTitle("Done!")
              msg.setText("You have added a new word !" + "\n")
              msg.setStandardButtons(QMessageBox.StandardButton.Ok)
              msg.setIcon(QMessageBox.Icon.Information)
              msg.exec()
              self.linedit1.clear()
              self.linedit2.clear()
              self.close()


class Translation(QWidget):
       
       def __init__(self) -> None:
              super().__init__()
              self.setWindowTitle("Choice")
              self.child_trans = None
              self.child_t = None
       
              self.btn1 = QPushButton("Translate into UZB")
              self.btn2 = QPushButton("Translate into ENG")
       
              self.h1 = QHBoxLayout()
              self.h1.addWidget(self.btn1)
              
              self.h2 = QHBoxLayout()
              self.h2.addWidget(self.btn2)

              
              self.ver = QVBoxLayout()
         
              self.ver.addLayout(self.h1)
              self.ver.addLayout(self.h2)
              
              
              self.setLayout(self.ver)
              
              self.btn2.clicked.connect(self.search_1)
              self.btn1.clicked.connect(self.search_2)
              self.btn1.setShortcut('enter')
              self.btn2.setShortcut('enter')
              
   
       def search_1(self):
              if     self.child_t is None:
                     self.child_t = Translation_2()
                     self.child_t.show()
              else:
                     self.child_t.close()
                     self.child_t = None
              
              
       def search_2(self):
              
              if     self.child_t is None:
                     self.child_t = Translation_2()
                     self.child_t.show()
              else:
                     self.child_t.close()
                     self.child_t = None

class Translation_2(QWidget):
       
       def __init__(self) -> None:
              super().__init__()
              
              self.child_t = None
              
              self.line_edit1 = QLineEdit()
              self.line_edit2 = QLineEdit()
              self.label1 = QLabel()
              self.label2 = QLabel()
              self.btn1 = QPushButton("SearchUz")
              self.btn2 = QPushButton("SearchEng")
              
              self.label1.setText("Uzb:")
              self.label2.setText("Eng:")

              self.h = QHBoxLayout()
              self.h.addWidget (self.label1)
              self.h.addWidget(self.line_edit1)
              self.h.addWidget(self.btn1)
              self.h.addStretch()
              
       
              self.h3 = QHBoxLayout()
              self.h3.addWidget (self.label2)
              self.h3.addWidget(self.line_edit2)
              self.h3.addWidget(self.btn2)
       
              self.ver = QVBoxLayout()
              self.ver.addLayout(self.h)
              self.ver.addLayout(self.h3)
              self.ver.addLayout(self.h3) 
              self.ver.addLayout(self.h3)
              
            
              self.btn1.clicked.connect(self.sear1)
              self.btn2.clicked.connect(self.sear2)
              
              self.setLayout(self.ver)
              
       def sear1(self):
              
              d = mydictionary()
              uz = self.line_edit1.text()
              eng = d.search(uz)
              self.line_edit2.setText(d.search(uz))
            
               
       def sear2(self):
              
              d = mydictionary()
              en = self.line_edit2.text()
              uz = d.search_2(en)
              self.line_edit1.setText(d.search_2(en))
                 
app = QApplication(sys.argv)

win = Mydictionary()
win.show()
sys.exit(app.exec())
