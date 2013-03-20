#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui


MessageGui_Error=1
MessageGui_Right=2
MessageGui_Error_IsNotImage=3


def GetLinkExeGui(errorOrRight):
    app = QtGui.QApplication(sys.argv)


 #   w = QtGui.QWidget()
 #   w.resize(250, 150)
 #   w.move(300, 300)
 #   w.setWindowTitle('Simple')
 #   w.show()	
# 默认是正确的
    tile="Message"
    message="that is OK!"
    if errorOrRight==MessageGui_Error :
        tile="Alert"
        message="something get wrong!please check the network!"
    elif errorOrRight==MessageGui_Error_IsNotImage :
        time="Alert"
        message="this is not a picture!!!!!"
    msg_box = QtGui.QMessageBox(QtGui.QMessageBox.Warning, tile, message)
    msg_box.show()
#    QtGui.QMessageBox.about(QtGui.QMessageBox.Warning,"上传成功")  
#    sys.exit(app.exec_())
    app.exec_()


if __name__ == '__main__':
    GetLinkExeGui(0)
