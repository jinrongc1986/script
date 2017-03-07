#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import sys,time,os
from openpyxl import Workbook
from openpyxl import load_workbook
#星域提供的节点信息
f=open('university.txt')
lista=[]
listb=[]
for line in f.readlines():
	lista.append(line.strip('\n'))
#本地保存的节点信息
wb = load_workbook('CDS设备信息.xlsx')
sheetname='VPE'
ws=wb[sheetname]
row=len(ws.columns)
print row
#比对并写入excel
for i in range(len(lista)):
	print lista[i]
