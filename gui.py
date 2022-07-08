# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import time
frequence = 0#次数，列表第一个是0
name_form = "许逸豪\n陈雨航\n蔡铭翔\n林汶锴\n蔡译慷\n蔡俊毅\n吴楠\n黄睿洋\n蔡瀚霖\n蔡柏玮\n黄语菲\n蔡昕颐\n肖钧浩\n许少骐\n许渊茹\n蔡语婷\n蔡沛龙\n邵梓扬\n蔡岷珉\n李狄轩\n王凯烨\n曾嘉鸿\n颜婧欣\n蔡俊凯\n蔡家欣\n吴耀恒\n许怡馨\n萧桠榆\n苏钲渊\n陈博升\n洪梓涵\n蔡静颖\n蔡皓程\n周苡丞\n张泽祺\n王佳期\n萧皓铭\n黄梓晨\n周家豪\n柯晴瑶\n蔡崇培\n曾景煜\n蔡良涵\n蔡铧霖\n蔡堉渝\n蔡凯铭\n施亚霖\n许耀钧\n王斯玄\n蔡瑞琪\n廖欣瑶\n黄俊翔\n许俊煌\n蔡荣权\n周天焱\n孙清萱"
#第6行代码是名字表单
name_list = name_form.split('\n')#列表
random.shuffle(name_list)#假随机列表
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setFixedSize(800,600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 100, 450, 100))
        self.label.setStyleSheet("font: 60pt \"黑体\";")
        self.label.setObjectName("label")
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(140, 480, 600, 71))
        self.label1.setStyleSheet("font: 20pt \"黑体\";")
        self.label1.setObjectName("label1")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 320, 450, 100))
        self.pushButton.setStyleSheet("font: 40pt \"幼圆\";")
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        self.pushButton.clicked['bool'].connect(self.logic)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "抽奖游戏"))
        self.label.setText(_translate("Form", ""))
        self.label1.setText(_translate("Form", "本程序由海鸽所编，要源码加QQ:1919458169"))
        self.pushButton.setText(_translate("Form", "开始抽奖"))
    def logic(self, Form):
        _translate = QtCore.QCoreApplication.translate
        global frequence
        i = 3
        while i > 0:#简易计时器
            self.label.setText(_translate("Form",f"<html><head></head><body><p align=\"center\">{str(i)}</p></body></html>"))
            i = i - 1
            self.label.repaint()
            time.sleep(1)        
        output_name = name_list[frequence]
        frequence = frequence + 1
        self.label.setText(_translate("Form",f"<html><head></head><body><p align=\"center\">{output_name}</p></body></html>"))
            
            