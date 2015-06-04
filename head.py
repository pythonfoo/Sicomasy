#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  head.py
#  
#  Copyright Rainer Kersten and Penny for the PHP-Scripts
#  Copyright 2013-2014 Mechtilde Stehmann <ooo@mechtilde.de>
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

import config

class makeHead(object):

	def __init__(self, act_site_langpath, act_title):
		self.act_site_langpath = act_site_langpath
		self.act_title = act_title

	def file2open(self, act_id):
		if act_id != 1:
			self.fileRead("head.html")
			self.replaceContent()
		else:
			self.fileRead("head_index.html")
		return self.Content

	def replaceContent(self):
		self.Content = self.Content.replace("@@@HEAD_index_lang@@@", self.act_site_langpath)
		self.Content = self.Content.replace("@@@HEAD_title@@@", self.act_title)


	def fileRead(self, filename):
		fobj = open(filename, "r")
		self.Content = fobj.read()
		fobj.close()

def main(Content, paradict):

	act_id = paradict["act_id"]
	act_site_langpath = paradict["act_site_langpath"]
	act_lang = paradict["act_lang"]
	lexikonDict = config.main("lexikon.txt")
	act_title = lexikonDict[act_lang + "-link"] + ': ' + lexikonDict[act_lang + "-home"]
	act_id = int(act_id)

	mh = makeHead(act_site_langpath, act_title)
	Content += mh.file2open(act_id)

	return Content
