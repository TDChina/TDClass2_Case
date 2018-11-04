#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Sun Nov 04 19:16:45 2018
#========================================
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
window_class, base_class = uic.loadUiType('D:/repo/TDClass2_Case/Qt_Signal_Slot/case_qt.ui')

def func(args):
    '''
    '''
    print args 
    
    
    
class CaseWindow(window_class, base_class):
    '''
    '''
    custom_signal = QtCore.pyqtSignal(str)
    
    def __init__(self, parent=None):
        '''
        '''
        super(CaseWindow, self).__init__(parent)
        self.setupUi(self)
        
   
    
    def showEvent(self, event):
        '''
        '''
        print 'show', event
    


    def closeEvent(self, event):
        '''
        '''
        print 'close', event
    
    def moveEvent (self, event):
        '''
        '''
        pass

    
    
    # @QtCore.Slot(bool)
    @QtCore.pyqtSlot(bool) #- pyqt
    def on_btn_A_clicked(self, args=None):
        '''
        '''
        self.custom_signal.emit('ssss')



def main():
    '''
    '''
    app = QtWidgets.QApplication(sys.argv)
    
    window = CaseWindow()
    window.show()
    
    app.exec_()


if __name__ == '__main__':
    main()
