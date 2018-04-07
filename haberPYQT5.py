#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

import sys
import os

from PyQt5.QtCore import QDate, QTime, Qt #Gerekli importlarý yaptýk

#þimdiki zamaný aldýk. #gün ay yýl günismi ni yazdýracaz

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
        #buraya kadar internetten veri çekme iþlemini yaptýk


        self.yazi_alani = QTextEdit()
        self.setGeometry(675, 300, 500, 500)
        self.goster = QPushButton("Haberleri Göster")
        self.sil=QPushButton("Temizle")
        self.tarih=QLabel(QDate.currentDate().toString(Qt.DefaultLocaleLongDate))#tarihi yazdýrmak için.
        #burada buton ve labelleri atadýk.

        v_box = QVBoxLayout()
        v_box.addWidget(self.tarih)
        v_box.addWidget(self.goster) # önce haberleri göster butonu
        v_box.addWidget(self.yazi_alani) # sonra haber yazýsý alaný
        v_box.addWidget(self.sil) # en altta temizle butonu
        #sýralama ve biçim verdik

        self.setWindowTitle("Güncel Haber Baþlýklarý")
        self.setLayout(v_box)
        self.goster.clicked.connect(self.click) #gostere týklanýrsa clik fonk. çalýþsýn
        self.sil.clicked.connect(self.supur) #temizleye týklanýrsa supur fonk. çalýþsýn
        self.show()
        #buraya kadar koþullar vs.




    def click(self):
        file = open("../haberler.txt", "w",encoding="utf-8")#belgeyi yeniden oluþtursun.
        for i in self.bist:

                i=i.text
                file = open("../haberler.txt", "a",encoding="utf-8")  # Yaz
                file.write(i)

                print(i) #test için
        with open("../haberler.txt", "r",encoding="utf-8") as file: #Oku
            self.yazi_alani.setText(file.read())


    def supur(self):
        self.yazi_alani.clear() # yazi alanýný temizle


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
