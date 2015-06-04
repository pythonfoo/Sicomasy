#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  tk-generate.py
#  
#  Copyright 2013 Mechtilde Stehmann <mechtilde@stephan>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import tkinter.simpledialog
import config

def _(String):
	"""solange keine gettext Integration erfolgt ist, ist dies ein dummy"""
	return String

class createWindow(object):

	def __init__(self, tk, master=None):
		self.master = master
		self.createWidgets()
		pass

	def createWidgets(self):
		"""Build and show the GUI elements."""
		Label(self.master, text=_("Konfigurationsdatei:")).grid(row=0, sticky=E)
		self.configfile = Entry(self.master)
		self.configfile.grid(columnspan=2, row=0, column=1, sticky=E+W)

		self.auswahl = Button(self.master)
		self.auswahl.bind("<Button-1>", self.master)
		self.auswahl["text"] = "Auswahl"
		self.auswahl.grid(row=1, column=1, sticky=E+W)

		Label(self.master, text=_("Search path:")).grid(row=3, sticky=E)
		self.ooo_path1 = Entry(self.master)
		self.ooo_path1.grid(columnspan=2, row=3, column=1, sticky=E+W)

		Label(self.master, text=_("Search terms:")).grid(row=4, sticky=E+W)
		self.ooo_path2 = Entry(self.master)
		self.ooo_path2.grid(columnspan=2, row=4, column=1, sticky=E+W)

		Label(self.master, text=_("Mode:")).grid(row=5, sticky=E)
		self.ooo_path3 = Entry(self.master)
		self.ooo_path3.grid(columnspan=2, row=5, column=1, sticky=E+W)

		Label(self.master, text=_("Matches:")).grid(row=7, sticky=N+E)
		self.ooo_path5 = Button(self.master, width = 20)
		self.ooo_path5.bind("<Button-1>", self.master)
#		self.ooo_path5["width"] = 10
		self.ooo_path5["text"] = "S T A R T"
		self.ooo_path5.grid(columnspan=2, row=6, column=1, sticky=W)

		dictc = config.main("config.txt")
		liste = []
		for element in dictc:
			liste.append(element + ":" + dictc[element])
		self.ooo_path4 = self.listbox(liste, 100, 7, 1)
#		self.ooo_path4.grid(columnspan=2, row=6, column=1, sticky=E+W)

	def listbox(self, liste, w, r, c):
		"""Erzeugt ein Listenfeld"""

		self.listbox = Listbox(self.master, width=w)
		for i in range(0,len(liste)):
			self.listbox.insert("end", " "+liste[i])
			self.listbox.grid(row=r, column=c, padx=5)
		return self.listbox

def main():
	tk = Tk()
	tk.minsize(380,200)
	tk.title("Sicomasy")
	tk.columnconfigure(1, weight=1)
	tk.rowconfigure(5, weight=1)
	tk.columnconfigure(1, weight=1)
	tk.rowconfigure(6, weight=0)

	app = createWindow(tk)
#	tk.protocol("WM_DELETE_WINDOW", app.doQuit)
	tk.mainloop()

	return 0

if __name__ == '__main__':
	main()

