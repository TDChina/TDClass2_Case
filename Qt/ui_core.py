#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Nov 02 20:56:37 2018
#========================================
import sys
from PySide2 import QtCore, QtWidgets, QtGui
import ui_frame
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def main():
    '''
    '''
    app = QtWidgets.QApplication(sys.argv)
    
    
    
    window = QtWidgets.QMainWindow()
    ui = ui_frame.Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    
    
    
    app.exec_()


if __name__ == '__main__':
    main()
