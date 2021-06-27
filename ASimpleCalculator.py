#!/usr/bin/python
# -*- coding: utf-8 -*-
# 本程序为实现简易计算器功能
# worte by 星辰 on 27th, June, 2021

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import  QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
import sys
import os
from math import *

class MainUi(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.init_ui()


	class pandasModel(QAbstractTableModel):

		def __init__(self, data):
			QAbstractTableModel.__init__(self)
			self._data = data

		def rowCount(self, parent=None):
			return self._data.shape[0]

		def columnCount(self, parnet=None):
			return self._data.shape[1]

		def data(self, index, role=Qt.DisplayRole):
			if index.isValid():
				if role == Qt.DisplayRole:
					return str(self._data.iloc[index.row(), index.column()])
			return None

		def headerData(self, col, orientation, role):
			if orientation == Qt.Horizontal and role == Qt.DisplayRole:
				return self._data.columns[col]
			return None


	def init_ui(self):

		MainUi.setWindowTitle(self,"A simple calculator.exe----Author:Xingchen")
		self.setFixedSize(960,700)
		
		

		self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
		self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
		self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

		self.right_widget = QtWidgets.QWidget() # 创建右侧部件
		self.right_widget.setObjectName('right_widget')
		self.right_layout = QtWidgets.QGridLayout()
		self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格


		op = QtWidgets.QGraphicsOpacityEffect()
		op.setOpacity(0.9)
		
		self.right_widget.setGraphicsEffect(op)
		self.right_widget.setAutoFillBackground(True)

		
		self.main_layout.addWidget(self.right_widget,0,2,12,10) 
		self.setCentralWidget(self.main_widget) # 设置窗口主部件

		


		self.button_LB = QtWidgets.QPushButton("(")
		self.button_RB = QtWidgets.QPushButton(")")
		self.button_LA = QtWidgets.QPushButton("<-")
		self.button_RA = QtWidgets.QPushButton("->")
		self.button_MESSAGE = QtWidgets.QPushButton("MESSAGE")


		self.button_2P = QtWidgets.QPushButton("^2")
		self.button_3P = QtWidgets.QPushButton("^3")
		self.button_nP = QtWidgets.QPushButton("^n")
		self.button_en = QtWidgets.QPushButton("e^n")
		self.button_ROOT = QtWidgets.QPushButton("sqrt()")

		

		self.button_SIN = QtWidgets.QPushButton("sin")
		self.button_COS = QtWidgets.QPushButton("cos")
		self.button_TAN = QtWidgets.QPushButton("tan")
		self.button_LG = QtWidgets.QPushButton("lg()")
		self.button_LN = QtWidgets.QPushButton("ln()")


		self.button_7 = QtWidgets.QPushButton("7")
		self.button_8 = QtWidgets.QPushButton("8")
		self.button_9 = QtWidgets.QPushButton("9")
		self.button_ADD = QtWidgets.QPushButton("+")
		self.button_LOG = QtWidgets.QPushButton("logx()")


		self.button_4 = QtWidgets.QPushButton("4")
		self.button_5 = QtWidgets.QPushButton("5")
		self.button_6 = QtWidgets.QPushButton("6")
		self.button_SUB = QtWidgets.QPushButton("-")
		self.button_DEL = QtWidgets.QPushButton("DEL")
		

		self.button_1 = QtWidgets.QPushButton("1")
		self.button_2 = QtWidgets.QPushButton("2")
		self.button_3 = QtWidgets.QPushButton("3")
		self.button_MUL = QtWidgets.QPushButton("×")
		self.button_AC = QtWidgets.QPushButton("AC")
		

		self.button_0 = QtWidgets.QPushButton("0")
		self.button_DOT = QtWidgets.QPushButton("·")
		self.button_10x = QtWidgets.QPushButton("10^x")
		self.button_DIV = QtWidgets.QPushButton("÷")
		self.button_EQU = QtWidgets.QPushButton("=")

		





		self.right_bar_widget = QtWidgets.QWidget() # 右侧顶部搜索框部件
		self.right_bar_layout = QtWidgets.QGridLayout() # 右侧顶部搜索框网格布局
		self.right_bar_widget.setLayout(self.right_bar_layout)


		self.right_bar_widget2 = QtWidgets.QWidget() # 右侧顶部搜索框部件
		self.right_bar_layout2 = QtWidgets.QGridLayout() # 右侧顶部搜索框网格布局
		self.right_bar_widget2.setLayout(self.right_bar_layout2)
	





		self.CalPro = QtWidgets.QLineEdit()
		self.CalPro.setStyleSheet(u"background-color: rgb(170, 170, 170);")

		self.CalRes = QtWidgets.QLineEdit()
		self.CalRes.setStyleSheet(u"background-color: rgb(170, 170, 170);")

		
		self.right_bar_layout.addWidget(self.CalPro,0,0,2,3)
		self.right_bar_layout.addWidget(self.CalRes,0,4,2,3)


		self.right_bar_layout.addWidget(self.button_LB,1,0,1,1)
		self.right_bar_layout.addWidget(self.button_RB,1,1,1,1)
		self.right_bar_layout.addWidget(self.button_LA,1,2,1,1)
		self.right_bar_layout.addWidget(self.button_RA,1,3,1,1)
		self.right_bar_layout.addWidget(self.button_MESSAGE,1,4,1,1)

		self.right_bar_layout.addWidget(self.button_2P,2,0,1,1)
		self.right_bar_layout.addWidget(self.button_3P,2,1,1,1)
		self.right_bar_layout.addWidget(self.button_nP,2,2,1,1)
		self.right_bar_layout.addWidget(self.button_en,2,3,1,1)
		self.right_bar_layout.addWidget(self.button_ROOT,2,4,1,1)
		
		self.right_bar_layout.addWidget(self.button_SIN,3,0,1,1)
		self.right_bar_layout.addWidget(self.button_COS,3,1,1,1)
		self.right_bar_layout.addWidget(self.button_TAN,3,2,1,1)
		self.right_bar_layout.addWidget(self.button_LG,3,3,1,1)
		self.right_bar_layout.addWidget(self.button_LN,3,4,1,1)
		
		self.right_bar_layout.addWidget(self.button_7,4,0,1,1)
		self.right_bar_layout.addWidget(self.button_8,4,1,1,1)
		self.right_bar_layout.addWidget(self.button_9,4,2,1,1)
		self.right_bar_layout.addWidget(self.button_ADD,4,3,1,1)
		self.right_bar_layout.addWidget(self.button_LOG,4,4,1,1)

		self.right_bar_layout.addWidget(self.button_4,5,0,1,1)
		self.right_bar_layout.addWidget(self.button_5,5,1,1,1)
		self.right_bar_layout.addWidget(self.button_6,5,2,1,1)
		self.right_bar_layout.addWidget(self.button_SUB,5,3,1,1)
		self.right_bar_layout.addWidget(self.button_DEL,5,4,1,1)

		self.right_bar_layout.addWidget(self.button_1,6,0,1,1)
		self.right_bar_layout.addWidget(self.button_2,6,1,1,1)
		self.right_bar_layout.addWidget(self.button_3,6,2,1,1)
		self.right_bar_layout.addWidget(self.button_MUL,6,3,1,1)
		self.right_bar_layout.addWidget(self.button_AC,6,4,1,1)
		
		self.right_bar_layout.addWidget(self.button_0,7,0,1,1)
		self.right_bar_layout.addWidget(self.button_DOT,7,1,1,1)
		self.right_bar_layout.addWidget(self.button_10x,7,2,1,1)
		self.right_bar_layout.addWidget(self.button_DIV,7,3,1,1)
		self.right_bar_layout.addWidget(self.button_EQU,7,4,1,1)		

		self.right_bar_layout2.addWidget

		self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)


	


	

		self.right_recommend_widget = QtWidgets.QWidget() 
		self.right_recommend_layout = QtWidgets.QGridLayout()
		self.right_recommend_widget.setLayout(self.right_recommend_layout)








		
		self.right_widget.setStyleSheet('''
	QWidget#right_widget{
		color:#232C51;
		background:white;
		border-top:1px solid darkGray;
		border-bottom:1px solid darkGray;
		border-right:1px solid darkGray;
		border-top-right-radius:10px;
		border-bottom-right-radius:10px;
	}
	QLabel#right_lable{
		border:none;
		font-size:16px;
		font-weight:700;
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
	}
''')
		self.CalPro.setStyleSheet(
'''
		border:1px solid gray;
		width:300px;
		border-radius:10px;
		padding:2px 4px;
		max-height:    25px;
		background-color: rgb(170, 170, 170);
		font-size:16px;
		font-weight:700;

	
	
''')
		self.CalRes.setStyleSheet(
'''
		border:1px solid gray;
		width:300px;
		border-radius:10px;
		padding:2px 4px;
		max-height:    25px;
		background-color: rgb(170, 170, 170);
		font-size:16px;
		font-weight:700;

	
	
''')
		self.button_LB.setStyleSheet(
'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_RB.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)

		self.button_LA.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_RA.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_MESSAGE.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_2P.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_3P.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_nP.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_en.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_ROOT.setStyleSheet	(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_SIN.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_COS.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_TAN.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_LG.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_LN.setStyleSheet	(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_7.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_8.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_9.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_ADD.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_LOG.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_4.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_5.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_6.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_SUB.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_DEL.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_1.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_2.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_3.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_MUL.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_AC.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_0.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_DOT.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_10x.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_DIV.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)
		self.button_EQU.setStyleSheet(
			'''
	
	QPushButton{
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		background-color: rgb(220,220,220);
		width:120px;
		padding:2px 4px;
		max-height:    25px;
	}
	
'''
)

		


	
# 		self.setWindowOpacity(0.9) # 设置窗口透明度
# 		self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
		# self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
		self.main_widget.setStyleSheet('''
QWidget#left_widget{
background:gray;
border-top:1px solid white;
border-bottom:1px solid white;
border-left:1px solid white;
border-top-left-radius:10px;
border-bottom-left-radius:10px;
}
''')
		self.main_layout.setSpacing(0)





class mywindow(MainUi):

	def  __init__ (self):
		
		self.calprocess=''
		self.calresult=0
		self.nowflag=0
		self.ifcal=1
		super(mywindow, self).__init__()
		self.button_LB.clicked.connect(self.LB)
		self.button_RB.clicked.connect(self.RB)
		self.button_LA.clicked.connect(self.LA)
		self.button_RA.clicked.connect(self.RA)
		self.button_MESSAGE.clicked.connect(self.MESSAGE)
		self.button_2P.clicked.connect(self.P2P)
		self.button_3P.clicked.connect(self.P3P)
		self.button_nP.clicked.connect(self.nP)
		self.button_en.clicked.connect(self.en)
		self.button_ROOT.clicked.connect(self.ROOT)
		self.button_SIN.clicked.connect(self.SIN)
		self.button_COS.clicked.connect(self.COS)
		self.button_TAN.clicked.connect(self.TAN)
		self.button_LG.clicked.connect(self.LG)
		self.button_LN.clicked.connect(self.LN)
		self.button_7.clicked.connect(self.N7)
		self.button_8.clicked.connect(self.N8)
		self.button_9.clicked.connect(self.N9)
		self.button_ADD.clicked.connect(self.ADD)
		self.button_LOG.clicked.connect(self.LOG)
		self.button_4.clicked.connect(self.N4)
		self.button_5.clicked.connect(self.N5)
		self.button_6.clicked.connect(self.N6)
		self.button_SUB.clicked.connect(self.SUB)
		self.button_DEL.clicked.connect(self.DEL)
		self.button_1.clicked.connect(self.N1)
		self.button_2.clicked.connect(self.N2)
		self.button_3.clicked.connect(self.N3)
		self.button_MUL.clicked.connect(self.MUL)
		self.button_AC.clicked.connect(self.AC)
		self.button_0.clicked.connect(self.N0)
		self.button_DOT.clicked.connect(self.DOT)
		self.button_10x.clicked.connect(self.N10x)
		self.button_DIV.clicked.connect(self.DIV)
		self.button_EQU.clicked.connect(self.EQU)
		
	def MESSAGE(self):
		reply = QtWidgets.QMessageBox.about(self, '关于', '本产品开发制作者：星辰\n联系方式：邮箱2586211644@qq.com')
	def LB(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'('+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def RB(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+')'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def LA(self):
		if self.ifcal==0:
			self.ifcal=1
			self.CalRes.setText('')
			return
		self.nowflag-=1
		if self.nowflag<=0:
			self.nowflag=0
			
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		self.CalPro.setText(calprocess2)
	def RA(self):
		if self.ifcal==0:
			self.ifcal=1
			self.CalRes.setText('')
			return
		self.nowflag+=1
		if self.nowflag>=len(self.calprocess):
			self.nowflag=len(self.calprocess)
			
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		self.CalPro.setText(calprocess2)
	def P2P(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'^2'+self.calprocess[self.nowflag:]
		self.nowflag+=2
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def P3P(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'^3'+self.calprocess[self.nowflag:]
		self.nowflag+=2
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def nP(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'^('+self.calprocess[self.nowflag:]
		self.nowflag+=2
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)

	def en(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'e^('+self.calprocess[self.nowflag:]
		self.nowflag+=3
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def ROOT(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'sqrt('+self.calprocess[self.nowflag:]
		self.nowflag+=5
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def SIN(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'sin('+self.calprocess[self.nowflag:]
		self.nowflag+=4
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def COS(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'cos('+self.calprocess[self.nowflag:]
		self.nowflag+=4
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def TAN(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'tan('+self.calprocess[self.nowflag:]
		self.nowflag+=4
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def LG(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'log(,10)'+self.calprocess[self.nowflag:]
		self.nowflag+=4
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def LN(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'log()'+self.calprocess[self.nowflag:]
		self.nowflag+=4
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)

	def N7(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'7'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def N8(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'8'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def N9(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'9'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def N4(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'4'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def N5(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'5'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def N6(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'6'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def N1(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'1'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def N2(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'2'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def N3(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'3'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def N0(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'0'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def DOT(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'.'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def ADD(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'+'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def LOG(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'log(,)'+self.calprocess[self.nowflag:]
		self.nowflag+=4
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def SUB(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'-'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def DEL(self):
		if self.ifcal==0:
			self.AC()
		if self.nowflag==0:
			return
		self.calprocess=self.calprocess[:self.nowflag-1]+self.calprocess[self.nowflag:]
		self.nowflag-=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def DIV(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'/'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)

	def N10x(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'*10^('+self.calprocess[self.nowflag:]
		self.nowflag+=5
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def MUL(self):
		if self.ifcal==0:
			self.AC()
		self.calprocess=self.calprocess[:self.nowflag]+'*'+self.calprocess[self.nowflag:]
		self.nowflag+=1
		calprocess2=self.calprocess[:self.nowflag]+'#'+self.calprocess[self.nowflag:]
		
		self.CalPro.setText(calprocess2)
	def EQU(self):
		calprocess3=self.calprocess.replace('^','**')
		process='self.results='+calprocess3
		
		self.ifcal=0
		try:
			exec(process)
			a=int(self.results)
		except:
			self.CalRes.setText('数学错误')
			return
		self.CalRes.setText(str(self.results))

		
		
	def AC(self):
		self.calprocess=''
		self.calresult=0
		self.nowflag=0
		self.ifcal=1
		self.CalPro.setText(self.calprocess)
		self.CalRes.setText('')
	def closeEvent(self, event):
		"""
		对MainWindow的函数closeEvent进行重构
		退出软件时结束所有进程
		"""
		reply = QtWidgets.QMessageBox.question(self,
											   'Server_V1.exe',
											   "是否要退出程序？",
											   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
											   QtWidgets.QMessageBox.No)
		if reply == QtWidgets.QMessageBox.Yes:
			event.accept()
			os._exit(0)
		else:
			event.ignore()

	
		

def main():
	app = QtWidgets.QApplication(sys.argv)
	ui = mywindow()
	ui.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()