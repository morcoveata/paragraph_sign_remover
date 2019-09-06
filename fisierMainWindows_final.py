import sys
from PyQt4 import QtGui
from PyQt4 import QtCore



class Window(QtGui.QMainWindow):
  def __init__(self):
    super(Window, self).__init__()
    self.setGeometry(50, 50, 1250, 800)
    self.setWindowTitle('Paragraph Line Remover')



    # https://stackoverflow.com/questions/37304684/qwidgetsetlayout-
    # attempting-to-set-qlayout-on-mainwindow-which-already
    wid = QtGui.QWidget(self)
    self.setCentralWidget(wid)  
    
    self.b = QtGui.QPushButton(self)
    self.b.setText("Paste")
    

    self.c = QtGui.QPushButton(self)
    self.c.setText("Prelucreaza")

    self.d = QtGui.QPushButton(self)
    self.d.setText("Copy")

    self.e = QtGui.QPushButton(self)
    self.e.setText("Clear")


    # https://stackoverflow.com/questions/26600057
    #/how-to-change-the-fontsize-for-everything-inside-qtextedit-in-pyqt4
    
    self.txt = QtGui.QTextEdit(self)
    font = QtGui.QFont()
    font.setPointSize(20)
    self.txt.setFont(font)


    layoutGrid = QtGui.QGridLayout()
    layoutGrid.addWidget(self.txt, 0, 0, 1, 4)
    layoutGrid.addWidget(self.b, 1, 0)
    layoutGrid.addWidget(self.c, 1, 1)
    layoutGrid.addWidget(self.d, 1, 2)
    layoutGrid.addWidget(self.e, 1, 3)

    wid.setLayout(layoutGrid)
    

    self.b.clicked.connect(self.Paste)
    self.c.clicked.connect(self.Play)
    self.d.clicked.connect(self.Copy)
    self.e.clicked.connect(self.Clear)


  def Paste(self):
    self.txt.paste()


  def Play(self):
    self.text = self.txt.toPlainText()
    self.text = self.text.replace('\n', ' ')
    self.txt.setPlainText(self.text)


  def Clear(self):
      self.txt.clear()

  def Copy(self):
    self.text = self.txt.toPlainText()
    cb = QtGui.QApplication.clipboard()
    cb.clear(mode=cb.Clipboard )
    cb.setText(self.text, mode=cb.Clipboard)
    self.txt.copy()


if __name__ == '__main__':
  app = QtGui.QApplication([])
  gui = Window()
  gui.show()
  app.exec_()
