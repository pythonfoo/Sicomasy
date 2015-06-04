#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  navi_lang.py
#  
#  Copyright Rainer Kersten and Penny for the PHP-Scripts
#  Copyright 2013 -2014 Mechtilde Stehmann <ooo@mechtilde.de>
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

class NaviLang(object):

	def __init__(self, paradict):

		self.act_lang = paradict["act_lang"]
		self.act_lang_path  = paradict["act_langpath"]
		self.act_dir  = paradict["act_dir"]
		self.act_file  = paradict["act_file"]
		self.act_id = paradict["act_id"]

		self.target_dir  = ""
		self.target_lang_path  = ""
		self.target_lang = ""

		self.navi_text  = ""
		self.navi_target  = ""
		self.end = ""
		self.switch = ""
		return

	def naviLangContent(self):
		configdict = config.main("config.txt")
		langstring = configdict["lang"]
		langlist = langstring.split(",")
		seitendict = config.main("seiten.txt")
		sprachendict = config.main("sprachen.txt")

		for target_lang in langlist:
			target_lang_path = sprachendict[target_lang + "-pfad"]
#			navi_text = sprachendict[$target_lang][text]
			target_dir = seitendict["Sites"+ self.act_id + "-" + target_lang + "ordner"]
			target_file = seitendict["Sites" + self.act_id + "-" + target_lang + "datei"]

			if target_file != "" and  self.act_lang_path != target_lang_path:
				
				if self.switch == "":
					self.switch = 1
					Content += '  <ul class="navi-lang">\n'
					end = "  </ul>\n"

				self.navi_target = "/" + target_lang_path + target_dir
				if target_file[0:6] != "index.": 
					self.navi_target += target_file
				Content += '    <li><a href="' + self.navi_target + '">' + self.navi_text + "</a></li>\n"

		Content += end + "\n"
		return Content 


def main(Content, paradict):

	nl = NaviLang(paradict)
	Content = nl.naviLangContent()

	return Content


if __name__ == '__main__':
	nl = NaviLang()
	nl.naviLangContent()
