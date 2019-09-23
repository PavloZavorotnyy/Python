#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import pickle
import matplotlib.pyplot as plt
import array as arr
import numpy as np
from enum import Enum

class OSTYPE(Enum):
	OS_TYPE_WIN   = 0
	OS_TYPE_LINUX = 1
	OS_UNKNOWN    = 2

class DataContainer:
	def __init__(self):
		self.arg = arr.array('d', [0.0])
		self.fun = arr.array('d', [0.0])
		self.size = 1

	def fromfile_txt(self, filename):
		f = open(filename, 'r')
		i = 0
		while True:
			str_read = f.readline()
			if(str_read == ""):
				break
			_str_lst = f.readline().strip('\n').split('\t')
			self.add_simple(float(_str_lst[0]), float(_str_lst[1]))
			i += 1
		f.close()

	def add_simple(self, arg, fun):
		self.arg.append(arg)
		self.fun.append(fun)
		self.size = self.size + 1

def check_os():
	if sys.platform == 'linux2' : return OSTYPE.OS_TYPE_LINUX
	elif sys.platform == 'linux' : return OSTYPE.OS_TYPE_LINUX
	elif sys.platform == 'win32' : return OSTYPE.OS_TYPE_WIN
	else : return OSTYPE.OS_UNKNOWN

if check_os() == OSTYPE.OS_TYPE_LINUX:
	print("Linux")
elif check_os() == OSTYPE.OS_TYPE_WIN:
	print("Windows")
elif check_os() == OSTYPE.OS_UNKNOWN:
	print("Unknown os system")
	exit()
else:
	print("Script internal error.")
	exit()

# Check runing this script
if len(sys.argv) != 2:
	print("Error running this script.")
	print("ARGV : ", sys.argv)
	print("Use : python ex_07.py <Argument>")
	print("Example: python ex_07.py Argument")
	exit()

# Рисуем график с помощью библиотеки matplotlib
# Устанавливаем пакет: pip install matplotlib
# https://matplotlib.org/users/pyplot_tutorial.html
# считываем данные для графика
data = DataContainer()
data.fromfile_txt("data.txt")

# рисуем график
# 1. данные для графика
plt.plot(data.arg, data.fun)
# 2. надпись по оси Y
plt.ylabel('Пропускание атмосферы tau(lamda)')
# 3. надпись по оси X
plt.xlabel('Длина волны lamda[mkm]')
# 4. открываем окно для отображения графика
# окно блокирует выполнение скрипта, пока не будет закрыто
plt.show()

# Сохранение рисунка без отображения в окне
# создаем данные для отображения
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
# рисуем и сохраняем в файл формата PNG
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(t, s)
fig.savefig('cos-01.png')

