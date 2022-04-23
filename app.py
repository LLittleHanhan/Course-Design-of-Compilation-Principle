#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年5月29日
@author: Irony
@site: https://pyqt.site , https://github.com/PyQt5
@email: 892768447@qq.com
@file: LeftTabWidget
@description:
"""
import re

from PyQt5 import QtWidgets
from PyQt5.uic.properties import QtCore

from CIFA import lex
from grammar import *
from semantic import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QStackedWidget, QHBoxLayout, \
    QListWidgetItem, QLabel, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu, QPushButton, \
    QVBoxLayout, QAction, QMainWindow, qApp, QMenuBar, QComboBox, QTextEdit, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl

class Child(QWidget):
    def __init__(self,type):
        super().__init__()
        self.resize(600, 300)
        layout=QVBoxLayout()
        self.text=QTextEdit()
        if type=='parse':
            self.parse()
        else:
            self.sem()
        self.text.setText(self.err)
        self.text.setReadOnly(True)
        layout.addWidget(self.text)
        self.setLayout(layout)



    def parse(self):
        self.setWindowTitle('语法错误')
        self.err = ''
        with open('rsc/grammar_result.txt', 'r', encoding='utf-8') as f:
            temp = f.read()
        self.err=str(temp)
        print(self.err)


    def sem(self):
        self.setWindowTitle('语义错误')
        self.err = ''
        with open('sem_result.txt', 'r', encoding='utf-8') as f:
            temp = f.readlines()
        self.err = str(temp[0])
        print(self.err)


dir_dict={}
class LeftTabWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(LeftTabWidget, self).__init__(*args, **kwargs)
        self.resize(1000, 800)

        # 左右布局(左边一个QListWidget + 右边QStackedWidget)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        # 左侧列表
        self.listWidget = QListWidget(self)

        # 右侧层叠窗口
        self.stackedWidget = QStackedWidget(self)
        vbox = QVBoxLayout()
        #菜单栏
        #按钮
        self.button=QPushButton()
        self.button.setText('add')
        menu=QHBoxLayout()
        menu.addWidget(self.button)
        #选项
        self.select=QComboBox()
        self.select.currentIndexChanged.connect(self.selectionChange)#连接action

        menu.addWidget(self.select)
        #封装进vbox
        content=QWidget()
        content.setLayout(menu)
        vbox.addWidget(content)
        vbox.addWidget(self.stackedWidget)
        self.initUi()


        content=QWidget()
        content.setLayout(vbox)
        #左选项 右菜单＋窗口
        layout.addWidget(self.listWidget)
        layout.addWidget(content)

        self.button.setObjectName('btn')
        self.button.clicked.connect(self.btn_clicked)

        self.setLayout(layout)

    def msg(self,type):
        self.ch = Child(type)
        self.ch.show()




    def run_program(self,directory,name):
        # 跑编译程序
        l = lex()
        l.run(directory)
        print("lex done")
        dir_dict[name] = directory
        print(dir_dict)

        flag=check_grammar(0)
        if flag==1 :
            sem_flag=sem_run(directory)
            if sem_flag == False:
                self.select.currentIndexChanged.disconnect(self.selectionChange)  # 连接action
                self.select.addItem(name)
                self.select.currentIndexChanged.connect(self.selectionChange)  # 连接action
                self.set_program(directory)
                self.set_lex()
                self.parse.load(QUrl(QFileInfo("rsc/GrammarTree.html").absoluteFilePath()))
                self.set_sem(sem_flag)
            else :
                self.msg('sem')
        else:
            self.msg('parse')



        # 存路径

        # 更新界面



    def btn_clicked(self):
        #self.restart()
        directory = QtWidgets.QFileDialog.getOpenFileName(self,
                                                          "getOpenFileName", "./",
                                                          "All Files (*);;Text Files (*.txt)")
        name=directory=directory[0]
        name=name.split('/')
        name=name[len(name)-1]
        name=name[0:-4]
        #print(name)
        self.run_program(directory,name)


    def selectionChange(self, i):
        #self.label.setText(self.cb.currentText())
        # 根据设置的文本调整尺寸
        #self.label.adjustSize()
        name=self.select.currentText()
        directory=dir_dict[name]

        print(directory)
        #重新跑
        self.run_program(directory,name)

    def set_left_list(self,text):
        item = QListWidgetItem(str(text), self.listWidget)
        # 设置item的默认宽高(这里只有高度比较有用)
        item.setSizeHint(QSize(16777215, 60))
        # 文字居中
        item.setTextAlignment(Qt.AlignCenter)

    def set_program(self,path):

        pro=''
        with open(path) as f:
            pro=f.read()
        self.program.setText(pro)

    def set_lex(self):
        with open('rsc/token.txt') as f:
            data=f.readlines()
        #print(data)
        count=len(data)
        self.LEX.setRowCount(count)
        for k,v in enumerate(data):
            v=v[0:-1]
            v=v.split()
            #print(v)
            newItem = QTableWidgetItem(v[0])
            newItem.setTextAlignment(Qt.AlignCenter)
            self.LEX.setItem(k, 0, newItem)
            newItem = QTableWidgetItem(v[1])
            newItem.setTextAlignment(Qt.AlignCenter)
            self.LEX.setItem(k, 1, newItem)
            newItem = QTableWidgetItem(v[2])
            newItem.setTextAlignment(Qt.AlignCenter)
            self.LEX.setItem(k, 2, newItem)

    def set_sem(self,flag):
        if flag==False:
            with open("sem_symtable.txt",'r') as f:
                data = f.readlines()
            count = len(data)
            self.sem_table.setRowCount(count)
            for k, v in enumerate(data):
                v = v.split()
                L=len(v)
                temp=v[2]
                if L > 4:
                    temp=temp+v[3]+v[4]+' '+v[5]+' '+v[6]
                newItem = QTableWidgetItem(v[0])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.sem_table.setItem(k, 0, newItem)
                newItem = QTableWidgetItem(v[1])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.sem_table.setItem(k, 1, newItem)
                newItem = QTableWidgetItem(temp)
                newItem.setTextAlignment(Qt.AlignCenter)
                self.sem_table.setItem(k, 2, newItem)
                newItem = QTableWidgetItem(v[-1])
                newItem.setTextAlignment(Qt.AlignCenter)
                self.sem_table.setItem(k, 3, newItem)




    def initUi(self):
        # 初始化界面
        # 通过QListWidget的当前item变化来切换QStackedWidget中的序号
        self.listWidget.currentRowChanged.connect(
            self.stackedWidget.setCurrentIndex)
        # 去掉边框
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # 隐藏滚动条
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #左侧选项
        self.set_left_list('program')
        self.set_left_list('LEX')
        self.set_left_list('parse')
        self.set_left_list('SEM')
        #程序界面
        self.program = QTextEdit()
        self.stackedWidget.addWidget(self.program)
        #词法表格
        self.LEX = QTableWidget()
        self.LEX.setColumnCount(3)
        self.LEX.setHorizontalHeaderLabels(['line', 'LEX', 'SEM'])
        # 匹配页面大小
        self.LEX.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 不可更改
        self.LEX.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选中
        self.LEX.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stackedWidget.addWidget(self.LEX)
        #语法html
        self.parse = QWebEngineView()
        self.stackedWidget.addWidget(self.parse)
        #语义分析结果
        self.sem_table=QTableWidget()
        self.sem_table.setColumnCount(4)
        self.sem_table.setHorizontalHeaderLabels(['名称', '类型', '变量类型','层数'])
        self.sem_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.sem_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sem_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stackedWidget.addWidget(self.sem_table)


# 美化样式表
Stylesheet = """
/*去掉item虚线边框*/
QListWidget, QListView, QTreeWidget, QTreeView, QMenuBar,QTextEdit,QLineEdit {
    outline: 0px;
}
/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/
QListWidget {
    min-width: 120px;
    max-width: 120px;
    color: white;
    background: gray;
}
/*被选中时的背景颜色和左边框颜色*/
QListWidget::item:selected {
    background: rgb(52, 52, 52);
    border-left: 2px solid rgb(9, 187, 7);
}
/*鼠标悬停颜色*/
HistoryPanel::item:hover {
    background: rgb(52, 52, 52);
}

/*右侧的层叠窗口的背景颜色*/
QStackedWidget {
    background: rgb(238,238,238);
}
/*模拟的页面*/
QLabel {
    color: white;
}
QMenuBar {
    background: rgb(238,238,238);
    color: rgb(#EEEEEE);
}

QTextEdit {
    font-family: "Microsoft YaHei";
    font-size: 20px;
    color: #ADADEB;
    background-color: rgb(238,238,238);
}

QMessageBox{
    color: #ADADEB;
}

"""

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    w = LeftTabWidget()
    w.show()
    sys.exit(app.exec_())


'''
        app = QApplication(sys.argv)
    w = Window()
    w.resize(400, 400)
    w.show()
        l = lex()
        a = l.run('example/c1.txt')
        for k in a:
            print(k)

'''
