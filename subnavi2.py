#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  subnavi2.py
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

import textfeld

# include($Path['home'] . "/navidata.php");

def main(Content, paradict):

#	act_lang = paradict["act_lang"]
#	act_id = paradict["act_id"]
#	act_dir = paradict["act_dir"]
#
#	target_id =    ""
#	target_file =  ""
#	target_dir =   ""
#	navi_text =    ""
#	navi_target =  ""
#	end =          ""
	Content = "<!-- Subnavigation2 --> \n"

	"""Subnavigation2"""

#	if "Sites" + act_id + "-" + act_lang + "-prev" in textfeld.Seiten:
#		target_id = textfeld.Seiten["Sites" + act_id + "-" + act_lang + "-prev"]
#		target_id = "Sites" + target_id
#		target_file = textfeld.Seiten[target_id + "-" + act_lang + "-datei"]
#		target_dir = textfeld.Seiten[target_id + "-" + act_lang + "-ordner"]
#		navi_text = textfeld.Seiten[target_id + "-" + act_lang + "-text"]
#		navi_target =  "/" + act_langpath + target_dir
#
#		if target_file[0:6] != "index.":
#			navi_target += target_file

#               if (($act_id == $subnavi2[$act_lang][$act_dir][$i]) || (empty($target_file))) {
#                        Content += '      <li class="here">' + navi_text + "</li>\n"
#               } else {
#                        Content += '      <li><a href="' + navi_target + '\">' + navi_text + "</a></li>\n"
#                }
#        }
#}

#	Content += end
	#// $Content .= implode("",file($Path['home'] . "/google-ad-160x600.js"));$

	return Content

