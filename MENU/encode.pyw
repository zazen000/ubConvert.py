import sys, os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qtpy_cfg import qblack, qbutton_dim, qtbutton, qledit, qbutton_calc
from PyQt5.QtWidgets import *
sys.path.insert( 1, 'C:\\Users\\mount\\source\\repos\\MyDashboard\\MODULES\\')
from ubEnigma import generate_key_and_code as gkc



class Communicate(QObject):
    closeApp = pyqtSignal()



class Dir_Dialog( QWidget ):

    def __init__(self, parent=None):
        super( Dir_Dialog, self ).__init__( parent )

        layout = QVBoxLayout()
        '''
        self.btn = QPushButton( "QFileDialog static method demo" )
        self.btn.clicked.connect( self.getfile )

        layout.addWidget( self.btn )
        self.le = QLabel( "Hello" )

        layout.addWidget( self.le )
        self.btn1 = QPushButton( "QFileDialog object" )
        self.btn1.clicked.connect( self.getfiles )
        layout.addWidget( self.btn1 )
        '''
        self.contents = QTextEdit()
        layout.addWidget( self.contents )
        self.setLayout( layout )
        self.setWindowTitle( "Directory" )



    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode( QFileDialog.Directory )
#        dlg.setFilter( "Text files (*.txt)" )
        filenames = QStringListModel()


        if dlg.exec_():
            filename = dlg.selectedFiles()
            return filename



class Encode(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left   = 1222
        self.top    = 23
        self.width  = 270
        self.height = 200
        self.comm   = Communicate()
        self.comm.closeApp.connect( self.close )
        self.dirView = Dir_Dialog()

        qblack(self)
        qdim   = qbutton_dim(self)
        q_ledit= qledit(self)
        canda_10 = QFont( 'Candalara', 10 )
        canda_8 = QFont( 'Candalara', 8 )
        qcalc = qbutton_calc( self )

        self.term_lbl = QLabel( self)
        self.term_lbl.setStyleSheet( "QLabel {color: rgba(80,130,255,255); background-color: black;}" )
        self.term_lbl.setFont( canda_10 )
        self.term_lbl.setText( "Enter File Name: " )
        self.term_lbl.setGeometry( 5, 60, 110, 20 )

        self.t_lbl = QLabel( self)
        self.t_lbl.setStyleSheet( "QLabel {color: rgba(80,130,255,255); background-color: black;}" )
        self.t_lbl.setFont( canda_10 )
        self.t_lbl.setText( "Enter Code String:" )
        self.t_lbl.setGeometry( 5, 5, 105, 20 )

        self.m_lbl = QLabel( self)
        self.m_lbl.setStyleSheet( "QLabel {color: rgba(80,130,255,255); background-color: black;}" )
        self.m_lbl.setFont( canda_8 )
        self.m_lbl.setAlignment(Qt.AlignCenter)
        self.m_lbl.setGeometry( 0, 120, 270, 20 )

        self.inputTxt = QLineEdit( self )
        self.inputTxt.setStyleSheet("QLineEdit {background-color: rgba(46, 46, 46, 240); color: rgba(162,201,229,255); border: black;}")
        self.inputTxt.setFont( QFont( 'Inconsolata', 10 ) )
        self.inputTxt.setGeometry( QRect( 5, 30, 260, 20 ) )
        self.inputTxt.setFocus()

        self.putTxt = QLineEdit( self )
        self.putTxt.setStyleSheet("QLineEdit {background-color: rgba(46, 46, 46, 240); color: rgba(162,201,229,255); border: black;}" )
        self.putTxt.setFont( QFont( 'Inconsolata', 10 ) )
        self.putTxt.setGeometry( QRect( 5, 85, 100, 20 ) )

        qtbutton(self, 'commit', 100, 160, 50, 30, qcalc, canda_10, 'ENCODE', self.encode )
        qtbutton(self, 'dir', 145, 85, 110, 22, qcalc, canda_10, 'Choose Directory', self.dir )

    def mousePressEvent(self):
        self.comm.closeApp.emit()

    def close_menu(self):
        self.timer1.start(6500)
        self.mousePressEvent()

    def wrap_up(self, num):
        time.sleep( num )
        self.mousePressEvent()
        self.close_menu()

    def threads(self, filename):
        self.git_thread.filename = filename
        self.git_thread.start()

    def dir(self):
        path = self.dirView.getfiles()[0] + r'/'
        self.m_lbl.setText(path)

    def encode(self):
        path = self.m_lbl.text()
        data = self.inputTxt.text()
        var  = self.putTxt.text()
        binn = f'{path}{var}.bin'
        txxt = f'{path}{var}.txt'
        gkc( binn, txxt, text=data )
        self.m_lbl.clear()
        self.inputTxt.clear()
        self.putTxt.clear()
        self.inputTxt.setFocus()



if __name__ == '__main__':
    app = QApplication([])
    ex  = Encode()
    ex.show()
    sys.exit(app.exec_())