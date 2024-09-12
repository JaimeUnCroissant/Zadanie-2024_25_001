from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Application(object):
    
    def __init__(self,  app):
        
        self.app = app
        self.ui = uic.loadUi('pliczek.ui')
        
        self.ui.pushButton.clicked.connect(self.increment)
        
        self.ui.show()
        self.run()
    def run(self):
        self.app.exec()
        
    def increment(self):
        
        current = self.ui.label.text()
        current = str(int(current) + 1)
        self.ui.label.setText(current)
        print("przycisk klikniety: " + current + " razy")
        
if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application(app)