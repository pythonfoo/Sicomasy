#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  subnavi.py
#  
#  Copyright Rainer Kersten and Penny for the PHP-Scripts
#  Copyright 2013 - 2014 Mechtilde Stehmann <ooo@mechtilde.de>
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

def main(paradict, snkey):

	act_lang = paradict["act_lang"]
	act_id = paradict["act_id"]
	act_langpath = paradict["act_langpath"]

	target_id =    ""
	target_file =  ""
	target_dir =   ""
	navi_text =    ""
	navi_target =  ""
	subnavikey = ""

	"""Subnavigation"""

	subnavidict = config.main("subnavi.txt")
	seitendict = config.main("seiten.txt")
	sprachendict =config.main("sprachen.txt")

	subnaviContent = ""

	for key in subnavidict:

		keysplit = key.split("-")
		if keysplit[0] == act_lang:
			subnavi = keysplit[1]
			if subnavidict[key] == act_id or subnavi == act_id: 
				subnavikey = keysplit[0] + "-" + keysplit[1]
				break

	subnavilist = []
	for element in subnavidict:
		elementSplitlist = element.split("-")
		if elementSplitlist[0]+ "-" + elementSplitlist[1] == subnavikey:
			subnavilist.append(int(elementSplitlist[2]))
	subnavilist.sort()

	newsubnavilist = []
	for number in subnavilist:
		newsubnavilist.append(subnavikey + "-" + str(number))
	subnavilist = newsubnavilist

	for entry in subnavilist:
		if subnavidict[entry] == snkey:
	#	Subnavigation schreiben
			target_id = "Sites" + str(subnavidict[entry])
			target_file = seitendict[target_id + "-" + act_lang + "-datei"]
			target_dir = seitendict[target_id + "-" + act_lang + "-ordner"]
			navi_text = seitendict[target_id + "-" + act_lang + "-text"]
			navi_target =  "/" + act_langpath + target_dir

			if target_file != "index.html":
				navi_target += target_file

			if target_file != "":
				if ("Sites" + str(act_id)) == target_id:
					subnaviContent = '        <li class="here">' + navi_text + '</li>\n'
				else:
					subnaviContent = '        <li><a href="' + navi_target + '">' + navi_text + "</a></li>\n"

	return subnaviContent

