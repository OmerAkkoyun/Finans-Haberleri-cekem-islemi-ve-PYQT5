#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

import sys
import os

from PyQt5.QtCore import QDate, QTime, Qt #Gerekli importlar� yapt�k

#�imdiki zaman� ald�k. #g�n ay y�l g�nismi ni yazd�racaz

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout



class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()



    def init_ui(self):

        url = "https://finans.haberler.com/haberler/"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        self.bist = soup.find_all("div", {"class": "general w130 h100"})
        #buraya kadar internetten veri �ekme i�lemini yapt�k


        self.yazi_alani = QTextEdit()
        self.setGeometry(675, 300, 500, 500)
        self.goster = QPushButton("Haberleri G�ster")
        self.sil=QPushButton("Temizle")
        self.tarih=QLabel(QDate.currentDate().toString(Qt.DefaultLocaleLongDate))#tarihi yazd�rmak i�in.
        #burada buton ve labelleri atad�k.

        v_box = QVBoxLayout()
        v_box.addWidget(self.tarih)
        v_box.addWidget(self.goster) # �nce haberleri g�ster butonu
        v_box.addWidget(self.yazi_alani) # sonra haber yaz�s� alan�
        v_box.addWidget(self.sil) # en altta temizle butonu
        #s�ralama ve bi�im verdik

        self.setWindowTitle("G�ncel Haber Ba�l�klar�")
        self.setLayout(v_box)
        self.goster.clicked.connect(self.click) #gostere t�klan�rsa clik fonk. �al��s�n
        self.sil.clicked.connect(self.supur) #temizleye t�klan�rsa supur fonk. �al��s�n
        self.show()
        #buraya kadar ko�ullar vs.




    def click(self):
        file = open("../haberler.txt", "w",encoding="utf-8")#belgeyi yeniden olu�tursun.
        for i in self.bist:

                i=i.text
                file = open("../haberler.txt", "a",encoding="utf-8")  # Yaz
                file.write(i)

                print(i) #test i�in
        with open("../haberler.txt", "r",encoding="utf-8") as file: #Oku
            self.yazi_alani.setText(file.read())


    def supur(self):
        self.yazi_alani.clear() # yazi alan�n� temizle




app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())


