#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  footer.py
#  
#  Copyright Rainer Kersten and penny for the PHP-Scripts
#  Copyright 2013-2014 Mechtilde Stehmann <ooo@mechtilde>
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

import functions

class makeFooter(object):

	def __init__(self, LastMod, Url):
		self.LastMod = LastMod
		self.Url = Url

	def replaceContent(self):
		self.Content = self.Content.replace("@@@FOOTER_LastMod@@@", self.LastMod)
		self.Content = self.Content.replace("@@@FOOTER_Url@@@", self.Url)


	def fileRead(self):
		fobj = open("footer.html", "r")
		self.Content = fobj.read()
		fobj.close()
		self.replaceContent()
		return self.Content

def main(Content, paradict):

	Funktionen = functions.Funktionen()
	LastMod = Funktionen.getLastModFile(paradict["act_id"], paradict["act_lang"], paradict["act_file"])

	mf = makeFooter(LastMod, paradict["url"])
	Content += mf.fileRead()

	return Content
