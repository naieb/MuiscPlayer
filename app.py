# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backup0.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import sys , os , random

import sqlite3


from mutagen.mp3 import MP3

from PyQt5 import QtCore, QtGui, QtWidgets 

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog ,QMessageBox ,QAction

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent 
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette 
from PyQt5.QtCore import Qt, QUrl  


import Queue
import DB

class Ui_MainWindow(object):

    def __init__(self):

        super().__init__()   

        #create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)        
        self.playlist = []

        #defin for number of music in playlist(index)
        self.curent = -1

        # define var for shuffle and repeat
        self.repeat = False
        self.shuffle = False  
        self.s = 1
        self.r = 1  
            
         # create DB if not exist
        if DB.check() == 0:                      
            DB.createTable()

    def setupUi(self, MainWindow) :

            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(835, 439)
            MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
            MainWindow.setAccessibleName("")
            MainWindow.setStyleSheet("")
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            
            self.centralwidget.setObjectName("centralwidget")
            self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
            self.groupBox.setGeometry(QtCore.QRect(0, 70, 551, 371))
            self.groupBox.setAlignment(QtCore.Qt.AlignCenter)

            self.groupBox.setObjectName("groupBox")
            self.btnplay = QtWidgets.QPushButton(self.groupBox)
            self.btnplay.setGeometry(QtCore.QRect(180, 310, 71, 25))
            self.btnplay.setFocusPolicy(QtCore.Qt.ClickFocus)
            self.btnplay.setCheckable(False)

            self.btnplay.setObjectName("btnplay")
            self.btnpuase = QtWidgets.QPushButton(self.groupBox)
            self.btnpuase.setGeometry(QtCore.QRect(250, 310, 71, 25))
            self.btnpuase.setFocusPolicy(QtCore.Qt.ClickFocus)
            self.btnpuase.setCheckable(True)
            # Add event        
            self.btnplay.clicked.connect(self.play)

            self.btnpuase.setObjectName("btnpuase")
            self.btnstop = QtWidgets.QPushButton(self.groupBox)
            self.btnstop.setGeometry(QtCore.QRect(320, 310, 61, 25))
            self.btnstop.setFocusPolicy(QtCore.Qt.ClickFocus)
            self.btnstop.setCheckable(False)
            # Added event
            self.btnpuase.clicked.connect(self.puase)

            self.btnstop.setObjectName("btnstop")
            self.btnnext = QtWidgets.QPushButton(self.groupBox)
            self.btnnext.setGeometry(QtCore.QRect(460, 270, 81, 25))
            self.btnnext.setFocusPolicy(QtCore.Qt.ClickFocus)
            # Added event
            self.btnstop.clicked.connect(self.stop)

            self.btnnext.setObjectName("btnnext")
            self.btnback = QtWidgets.QPushButton(self.groupBox)
            self.btnback.setGeometry(QtCore.QRect(460, 300, 81, 25))
            self.btnback.setFocusPolicy(QtCore.Qt.ClickFocus)
            # added event
            self.btnnext.clicked.connect(self.nextItemPlaylist)

            self.btnback.setObjectName("btnback")
            # added event
            self.btnback.clicked.connect(self.prevItemPlaylist)

            self.label_1 = QtWidgets.QLabel(self.groupBox)
            self.label_1.setEnabled(True)
            self.label_1.setGeometry(QtCore.QRect(10, 30, 531, 201))
            self.label_1.setText("")        
            # Added Animation for Lable
            movie = QtGui.QMovie(("Gif/4.gif"))
            self.label_1.setMovie(movie)
            movie.start()

            self.label_1.setScaledContents(True)
            self.label_1.setAlignment(QtCore.Qt.AlignCenter)
            self.label_1.setObjectName("label_1")

            self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 250, 261, 21))

            self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

            self.horizontalLayout.setObjectName("horizontalLayout")
            self.seek = QtWidgets.QSlider(self.horizontalLayoutWidget)
            self.seek.setFocusPolicy(QtCore.Qt.WheelFocus)
            self.seek.setOrientation(QtCore.Qt.Horizontal)

            self.seek.setObjectName("seek")
            self.horizontalLayout.addWidget(self.seek)
            self.label_3 = QtWidgets.QLabel(self.groupBox)
            self.label_3.setGeometry(QtCore.QRect(100, 250, 41, 17))
            # Set Rang For Horizontal
            self.seek.setRange(0,0)
            # added event
            self.seek.sliderMoved.connect(self.set_position)

            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.groupBox)
            self.label_4.setGeometry(QtCore.QRect(420, 250, 41, 17))

            self.label_4.setObjectName("label_4")
            self.lblPause = QtWidgets.QLabel(self.groupBox)
            self.lblPause.setGeometry(QtCore.QRect(10, 350, 101, 17))
            self.lblPause.setText("")

            self.lblPause.setObjectName("lblPause")
            self.btnshuffle = QtWidgets.QPushButton(self.groupBox)
            self.btnshuffle.setGeometry(QtCore.QRect(10, 270, 81, 25))
            self.btnshuffle.setFocusPolicy(QtCore.Qt.ClickFocus)

            self.btnshuffle.setObjectName("btnshuffle")
            self.btnrepeat = QtWidgets.QPushButton(self.groupBox)
            self.btnrepeat.setGeometry(QtCore.QRect(10, 300, 81, 25))
            self.btnrepeat.setFocusPolicy(QtCore.Qt.ClickFocus)
            #add event
            self.btnshuffle.clicked.connect(self.Shuffle)

            self.btnrepeat.setObjectName("btnrepeat")
            self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
            self.groupBox_2.setGeometry(QtCore.QRect(550, 70, 281, 371))
            self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)

            self.groupBox_2.setObjectName("groupBox_2")
            self.List = QtWidgets.QListWidget(self.groupBox_2)
            self.List.setGeometry(QtCore.QRect(10, 30, 261, 291))
            #add event
            self.btnshuffle.clicked.connect(self.Repeat)

            self.List.setObjectName("List")           

            self.btnSave = QtWidgets.QPushButton(self.groupBox_2)
            self.btnSave.setGeometry(QtCore.QRect(150, 330, 101, 31))

            self.btnSave.setObjectName("btnSave")
            self.btnLoad = QtWidgets.QPushButton(self.groupBox_2)
            self.btnLoad.setGeometry(QtCore.QRect(30, 330, 101, 31))
            #add event
            self.btnSave.clicked.connect(self.insert)

            self.btnLoad.setObjectName("btnLoad")
            self.btnremove = QtWidgets.QPushButton(self.centralwidget)
            self.btnremove.setGeometry(QtCore.QRect(620, 40, 141, 21))        
            self.btnremove.setFocusPolicy(QtCore.Qt.ClickFocus)
            # add event
            self.btnLoad.clicked.connect(self.select)                    

            self.btnremove.setObjectName("btnremove")
            self.btnadd = QtWidgets.QPushButton(self.centralwidget)
            self.btnadd.setGeometry(QtCore.QRect(620, 10, 141, 21))
            self.btnadd.setFocusPolicy(QtCore.Qt.ClickFocus)
        #     add event
            self.btnremove.clicked.connect(self.remove)

            self.btnadd.setObjectName("btnadd")
            self.txtname = QtWidgets.QTextEdit(self.centralwidget)
            self.txtname.setEnabled(False)
            self.txtname.setGeometry(QtCore.QRect(120, 40, 411, 21))
            self.txtname.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.txtname.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            # added event        
            self.btnadd.clicked.connect(self.open_file)

            self.txtname.setObjectName("txtname")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(6, 40, 121, 20))

            self.label_2.setObjectName("label_2")
            self.btninfo = QtWidgets.QPushButton(self.centralwidget)
            self.btninfo.setGeometry(QtCore.QRect(210, 10, 131, 21))        
            self.btninfo.setFocusPolicy(QtCore.Qt.ClickFocus)

            self.btninfo.setObjectName("btninfo")
            # added event        
            self.btninfo.clicked.connect(self.info)

            MainWindow.setCentralWidget(self.centralwidget)
            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.groupBox.setTitle(_translate("MainWindow", "Music Player"))
            self.btnplay.setText(_translate("MainWindow", "play"))
            self.btnpuase.setText(_translate("MainWindow", "puase"))
            self.btnstop.setText(_translate("MainWindow", "stop"))
            self.btnnext.setText(_translate("MainWindow", "Next"))
            self.btnback.setText(_translate("MainWindow", "Previouse"))
            self.label_3.setText(_translate("MainWindow", "00:00"))
            self.label_4.setText(_translate("MainWindow", "00:00"))
            self.btnshuffle.setText(_translate("MainWindow", "Shuffle"))
            self.btnrepeat.setText(_translate("MainWindow", "Repeat"))
            self.groupBox_2.setTitle(_translate("MainWindow", "Music Lsit"))
            self.btnSave.setText(_translate("MainWindow", "Save playList"))
            self.btnLoad.setText(_translate("MainWindow", "Load playList"))
            self.btnremove.setText(_translate("MainWindow", "Remove Music"))
            self.btnadd.setText(_translate("MainWindow", "Add Music"))
            self.label_2.setText(_translate("MainWindow", "Music Selected :"))
            self.btninfo.setText(_translate("MainWindow", "Music Info"))

            # define it for handling Seek
            self.mediaPlayer.positionChanged.connect(self.position_changed)
            self.mediaPlayer.durationChanged.connect(self.duration_changed)
            

# -----------------------------------Create Event Function For GUI -----------------------------------------------------------------



    def open_file(self):
            filename, _  = QFileDialog.getOpenFileName(filter='*.mp3 *.wav')

            if filename != '':
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))                    
                self.playlist.append(filename)
                self.List.addItem(filename)        

                Queue.put(filename)     

                info = QMessageBox()            
                info.setText("The music was successfully added to the list")
                info.exec()
                info.show()
                
                


    def play(self):
        index = self.playlist.index(Queue.get())
        self.curent = index
        self.txtname.append(str(self.playlist[index]))  
        

        if  self.shuffle :
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(str(self.playlist[self.curent]))))     

        if self.repeat:
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(str(self.playlist[self.curent]))))     

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(str(self.playlist[index]))))      
        
        audio =  MP3 (self.playlist[index])
        time = (audio.info.length)                   
        min,second = divmod(time,60)        
        min = round(min)
        second = round(second)
        times = '{:2d}:{:2d}'.format(min,second)
        self.label_4.setText( str(times) )

        self.txtname.append( str(self.playlist[index]))
        self.mediaPlayer.play() 

        self.lblPause.setText("")           

            
            


    def puase(self):
        self.mediaPlayer.pause()
        self.lblPause.setText("Music is Puase")


    def stop(self):
        self.mediaPlayer.stop()
        self.lblPause.setText("Music is Stop")


    def position_changed(self, position):
        self.seek.setValue(position) 
        
        #update the text label
        self.label_3.setText('%d:%02d'%(int(position/60000),int((position/1000)%60))) 
            

                                 

    def duration_changed(self, duration):
        self.seek.setRange(0, duration)
        

    def set_position(self, position ,senderType=False):
        self.mediaPlayer.setPosition(position)    

        #update the text label
        self.label_3.setText('%d:%02d'%(int(position/60000),int((position/1000)%60)))

        if(self.label_3.text() == self.label_4.text()):
                print('1')                
            

    def info(self):
            metaDataKeyList = self.mediaPlayer.availableMetaData()
            fullText =  '<table class="tftable" border="0">'            
            for key in metaDataKeyList:
                value = self.mediaPlayer.metaData(key)
                fullText = fullText + '<tr><td>' + key + '</td><td>' + str(value) + '</td></tr>'
            fullText = fullText + '</table>'
            infoBox = QMessageBox()
            infoBox.setWindowTitle('Detailed Song Information')
            infoBox.setTextFormat(Qt.RichText)
            infoBox.setText(fullText)
            infoBox.addButton('OK',QMessageBox.AcceptRole)
            infoBox.exec()
            infoBox.show()

    def prevItemPlaylist(self):
        index = self.curent -1
        self.curent = index
        temp = self.playlist[index]
        self.txtname.append("")
        self.txtname.append( temp )

        if  self.shuffle :
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(str(self.playlist[self.curent]))))     
                
        if self.repeat:
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(str(self.playlist[self.curent]))))     

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(temp)))  
        self.mediaPlayer.play()

        audio =  MP3 (self.playlist[index])
        time = (audio.info.length)                   
        min,second = divmod(time,60)        
        min = round(min)
        second = round(second)
        times = '{:2d}:{:2d}'.format(min,second)
        self.label_4.setText( str(times) )

    def nextItemPlaylist(self):
        index = self.curent +1
        self.curent = index
        temp = self.playlist[index]
        self.txtname.append("")
        self.txtname.append( temp )

        if  self.shuffle :
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(str(self.playlist[self.curent]))))     
                        
        if self.repeat:
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(str(self.playlist[self.curent]))))     

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(temp)))  
        self.mediaPlayer.play()

        audio =  MP3 (self.playlist[index])
        time = (audio.info.length)                   
        min,second = divmod(time,60)        
        min = round(min)
        second = round(second)
        times = '{:2d}:{:2d}'.format(min,second)
        self.label_4.setText( str(times) )
    
    def  insert(self):
        for address in self.playlist:                           
                DB.insert(address)           

    def  select(self):
        rows = DB.select()
        for row in rows:
                a = str(row).replace('(',"")
                a = str(a).replace("'","")
                a = str(a).replace(",","")
                a = str(a).replace(")","")
                Queue.put(str(a))
                self.playlist.append(str(a))
                self.List.addItem(str(a))                  
                  

    def remove(self):
        index = self.curent
        self.playlist.remove(self.playlist[index])
        
        for item in self.playlist:
                self.List.clear()
                self.List.addItem(item) 
        
    def Shuffle(self):
        self.s = 1

        if   self.s % 2 == 0:
                self.shuffle = True
                self.s =   self.s +1
                index = len(self.playlist)
                ran = random.randint(0,index)
                self.curent = ran
                self.lblPause.setText("Random number is :{}".format(ran))
                        
        self.s =  self.s +1       

    def Repeat(self):
        self.r = 1

        if self.r % 2 == 0:
            self.repeat = True
            self.r = self.r+1
        self.r = self.r+1        


    # ----------------------------------------------------------------------------------------------------- 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
