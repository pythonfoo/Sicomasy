#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  navi.py
#  
#  Copyright Rainer Kersten and penny for the PHP-Scripts
#  Copyright 2013 - 2014 Mechtilde Stehmann <mechtilde@stephan>
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
import subnavi

class Navigation(object):

	def __init__ (self, paradict):
		self.act_id = paradict["act_id"]
		self.act_lang = paradict["act_lang"]
		self.act_langpath = paradict["act_langpath"]
#		self.act_dir = paradict["act_dir"]

		self.subnavidict = config.main("subnavi.txt")
		configdict = config.main("config.txt")
		langstring = configdict["lang"]
		self.langlist = langstring.split(",")
		self.navidict = config.main("navi.txt")
		self.seitendict = config.main("seiten.txt")
		self.sprachendict =config.main("sprachen.txt")

		self.subnaviID = ""
		self.target_id =    ""
		self.target_file =  ""
		self.target_dir =   ""

	def subnaviList1(self):

		subnavilist=[]
		for key in self.subnavidict:
			keysplit = key.split("-")
			if keysplit[0] == self.act_lang:
				subnaviElement = keysplit[1]
				subnavilist.append(subnaviElement)
			subnavilist.append(self.subnavidict[key])
		subnavilist = list(set(subnavilist))

		return subnavilist

	def navi(self, Content):

		Content += "      <!-- Hier beginnt die Navigation --> \n"
		Content += "      <ul>       <!-- bar1 -->\n "

		for i in range(len(self.langlist)):
			navilist = []

			for element in self.navidict:
				elementSplitlist = element.split("-")
				if elementSplitlist[0] == self.langlist[i]:
					navilist.append(int(elementSplitlist[1]))
			navilist.sort()

			newnavilist = []
			for number in navilist:
				newnavilist.append(self.langlist[i] + "-" + str(number))
			navilist = newnavilist

			if navilist != []:
				for entry in navilist:
				#	snContent = ""
				#	subnaviContent = ""
					self.target_id = "Sites" + str(self.navidict[entry])
					self.targetid2 = str(self.navidict[entry])

					self.target_file = self.seitendict[self.target_id + "-" + self.langlist[i] + "-datei"]
					self.target_dir = self.seitendict[self.target_id + "-" + self.langlist[i] + "-ordner"]
					link_text = self.seitendict[self.target_id + "-" + self.langlist[i] + "-text"]

					link_target = "/" + self.sprachendict[self.langlist[i] + "-pfad"] + self.target_dir 

					if self.target_file != "index.html":
						link_target += self.target_file

					if self.target_file != "":

						if self.act_id == self.targetid2:
							naviContent = '       <li class="here">' + link_text
							naviContent += self.subNavi(entry)

						else:
							naviContent = '      <li><a href="' + link_target + '">' + link_text + '</a>'
							naviContent += self.subNavi(entry)

						naviContent += "    </li>\n"

					Content += naviContent
		Content += "     </ul><!-- foo -->"

		return Content

	def subNavi(self, entry):

		subnavicontentdict = {}
		subnavicontentlist = []
		subnaviContent = ""

		snContent = "\n     <!-- Subnavigation --> \n"
		snContent += "     <ul>\n"

		for key in self.subnavidict:
			snkeysplit = key.split("-")
			subnaviElement = snkeysplit[1]
			subnaviPosition = snkeysplit[2]

			subnavilist = self.subnaviList1()
			if self.targetid2 in subnavilist and self.navidict[entry] == subnaviElement:

				subnaviContent = self.subnaviLines(self.subnavidict[key])
				subnavicontentdict.update({subnaviPosition : subnaviContent})
				for key in subnavicontentdict:
					subnavicontentlist.append(key)
				subnavicontentlist = list(set(subnavicontentlist))
				subnavicontentlist.sort()

		for position in subnavicontentlist:
			snContent += subnavicontentdict[position]

		snContent += "     </ul>\n    <!-- Ende Subnavigation --> \n"
		if subnaviContent == "":
			snContent = ""
		naviContent = snContent

		return naviContent

	def subnaviList2(self):

		subnavilist = []
		for element in self.subnavidict:
			elementSplitlist = element.split("-")
			if elementSplitlist[0]+ "-" + elementSplitlist[1] == self.subnavikey:
				subnavilist.append(int(elementSplitlist[2]))
		subnavilist.sort()

		newsubnavilist = []
		for number in subnavilist:
			newsubnavilist.append(self.subnavikey + "-" + str(number))
		subnavilist = newsubnavilist

		return subnavilist

	def subnaviLines(self, snkey):

		navi_text =    ""
		navi_target =  ""
		self.subnavikey = ""

		"""Subnavigation"""
		subnaviContent = ""

		for key in self.subnavidict:

			keysplit = key.split("-")
			if keysplit[0] == self.act_lang:
				subnavi = keysplit[1]
				if self.subnavidict[key] == self.act_id or subnavi == self.act_id: 
					self.subnavikey = keysplit[0] + "-" + keysplit[1]
					break

		subnavilist = self.subnaviList2()
		for entry in subnavilist:
			if self.subnavidict[entry] == snkey:
		#	Subnavigation schreiben
				self.target_id = "Sites" + str(self.subnavidict[entry])
				self.target_file = self.seitendict[self.target_id + "-" + self.act_lang + "-datei"]
				self.target_dir = self.seitendict[self.target_id + "-" + self.act_lang + "-ordner"]
				navi_text = self.seitendict[self.target_id + "-" + self.act_lang + "-text"]
				navi_target =  "/" + self.act_langpath + self.target_dir

				if self.target_file != "index.html":
					navi_target += self.target_file

				if self.target_file != "":
					if ("Sites" + str(self.act_id)) == self.target_id:
						subnaviContent = '        <li class="here">' + navi_text + '</li>\n'
					else:
						subnaviContent = '        <li><a href="' + navi_target + '">' + navi_text + "</a></li>\n"

		return subnaviContent

def main(Content, paradict):
	n = Navigation(paradict)
	Content += n.navi(Content)
	return Content

if __name__ == '__main__':
	main("<!-- Navigation -->", {'act_file': 'Erstellung.html', 'url': 'http://www.mechtilde.neu/ooodatenbank/Erstellung.html', 'act_lang': 'de', 'act_dir': 'ooodatenbank/', 'act_site_langpath': '', 'act_id': '214', 'act_langpath': ''})
