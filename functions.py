#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  functions.py
#  
#  Copyright Rainer Kersten and penny for the PHP-Scripts
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
import datetime
import os
import re

class Funktionen(object):

	def __init__(self):
		self.style = config.main("sampleProject/style.txt")
		self.mainConfig = config.main("sampleProject/config.txt")
		self.seitendict = config.main("sampleProject/seiten.txt")
		self.sprachendict =config.main("sampleProject/sprachen.txt")

		self.templates = {
		"head" : "head.py",
		"navi" : "navi.py",
#		"subnavi2" : "subnavi2.py",
		"navilang" : "navi_lang.py",
		"footer" : "footer.py",
		}

	def mkName(self, Name):
		Name = Name.strip()
		Name = Name.lower()
		Name = Name.replace("ä", "ae")
		Name = Name.replace("ö", "oe")
		Name = Name.replace("ü", "ue")
		Name = Name.replace("ß", "ss")
		Name = Name.replace(" ", "_")
		Name = Name.replace("-", "_")
		Name = Name.replace("(", "")
		Name = Name.replace(")", "")
		return Name

	def getConfig(self, Tag):

		k = self.Site_siteid + "-" + self.Site_language + "-" + Tag
		l = self.Site_language + "-" + Tag
		if k not in self.seitendict and l not in self.sprachendict and Tag not in self.mainConfig:
			return ""

		elif k in self.seitendict:
			return self.seitendict[k]
		elif l in self.sprachendict:
			return self.sprachendict[l]
		else:
			return self.mainConfig[Tag]

	def getLastModFile(self, Site_siteid, Site_language, Site_file):

		if "Sites" + Site_siteid + "-" + Site_language + "-update" in self.seitendict:
			update_date = self.seitendict["Sites" + Site_siteid + "-" + Site_language + "-update"]

		else:

			if os.path.exists(self.mainConfig['templatespath'] + "/" + Site_file):
				timestamp = os.path.getmtime(self.mainConfig['templatespath'] + "/" + Site_file)
				timestruct = datetime.date.fromtimestamp(timestamp)
			else:
				timestruct = datetime.date.today()
			y = str(timestruct)[0:4]
			m = str(timestruct)[5:7]
			d = str(timestruct)[-2:]

			update_date = d + "." + m + "." + y 

		return update_date

	def setGlobals(self, Site_siteid, Site_language, Site_languagepath, Site_actpath, Site_file):
		self.Content = ""
		self.Site_siteid = Site_siteid
		self.Site_language = Site_language
		self.Site_languagepath = Site_languagepath
		self.Site_actpath = Site_actpath
		self.Site_file = Site_file

		self.Site_domain = self.mainConfig["domain"]
		

		subdomain = self.getConfig("subdomain")

		if subdomain == "":
			subdomain = 'www'

		if self.Site_file[0:6] == "index.": 
			url = "http://" + subdomain + "." + self.Site_domain + "/" + self.Site_languagepath + self.Site_actpath
		else:
			url = 'http://' + subdomain + "." + self.Site_domain + "/" + self.Site_languagepath + self.Site_actpath + self.Site_file

		self.Global ={
			"subdomain" : subdomain,
			"url" : url,
			"description" : self.getConfig("description"),
			"title" : self.getConfig("title"),
			"title_begin" : self.getConfig("title_begin"),
			"subject" : self.getConfig("subject"),
			"author" : self.getConfig("author"),
			"publisher" : self.getConfig("publisher"),
			"location" : self.getConfig("location"),
			"robots" : self.getConfig("robots"),	
			"doctype" : self.getConfig("doctype"),
			"googlesize" : self.getConfig("googlesize"),
			"lastmod" : self.getLastModFile(self.Site_siteid, self.Site_language, self.Site_file),

			# Globals for galleries
			"gal_navi_text": self.getConfig("gal_navi_text"),
			"gal_navi_line": self.getConfig("gal_navi_line"),

			# just for testing. Might be deleted later...
			"meta_description"	: self.getConfig("meta_description"),
		}

	def myMkDir(self, directory, mode = 0o755):

		def mkdir(directory, mode = 0o755):

			if os.path.isdir(directory):
				return True
			else:
				try:
					os.mkdir(directory, mode)
					return True
				except:
					return False

		def list2path(liste):
			path = ""
			for element in liste:
				path = path + "/" + element
			return path

		adir = os.path.abspath(directory)
		if os.path.isfile(adir):
			return "Es existiert eine Datei gleichen Namens."
		elif os.path.isdir(adir):
			return "Verzeichnis existiert bereits!"
		else:
			alist = adir.split("/")

			i = 0
			olist = alist[1:]
			while i < len(alist):
				newdir = list2path(olist)
				a = mkdir(newdir, mode)
				if a == True: break
				i = i + 1
				olist = olist[0:-i]

			while len(olist) < len(alist)-1:
				olist.append(alist[len(olist)+1])
				newdir = list2path(olist)
				a = mkdir(newdir, mode)

			return "Verzeichnis "+adir+" wurde angelegt."

	def mkHead(self):

		enc = "UTF-8"
		iso = self.Site_language
		headstring = ""
		if self.Site_file[-4:] != ".php":
			headstring = "<?xml version='1.0' encoding='" + enc + "'?>\n"
			doctype = self.Global["doctype"]
		if doctype =="":
			doctype = "Transitional"

		declaration = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 ' + doctype + '//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-' + doctype.lower() + '.dtd">\n'
		declaration += '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="' + iso + '" lang="' + iso + '">\n'
		declaration += "<head>\n";

		headstring += declaration

		k = self.Site_siteid + "-" + self.Site_language + "-" + "base"
		if k in self.seitendict and self.seitendict[k] == "y":

			headstring += '  <base href="http://www.' + domain + self.Site_actpath + "/"
			if self.Site_file != "index.html":
				headstring += self.Site_file

			headstring +='" />\n'

		k = self.Site_siteid + "-" + self.Site_language +"-" + "keywords"
		if k in self.seitendict:
			headstring +='  <meta name="keywords" content="' + self.seitendict[k] + '" />\n'


		if self.Global["meta_description"] != "DC only": 
			headstring += '  <meta name="description" content="' + self.Global["description"] + '" />\n'

		headstring += '  <meta name="robots" content="' + self.Global["robots"] + '" />\n'

		headstring += '  <meta name="DC.Title" content="' + self.Global["title"] + '" />\n'

		if self.Global["author"] != "":
			headstring += '  <meta name="DC.Creator" content="' + self.Global["author"] + '" />\n'

		k = self.Site_siteid + "-" + self.Site_language +"-" + "subject"
		if k in self.seitendict:
			headstring += '  <meta name="DC.Subject" content="' + self.seitendict[k] + '" />\n'

		headstring += '  <meta name="DC.Description" content="' + self.Global["description"] + '" />\n'
		headstring += '  <meta name="DC.Publisher" content="' + self.Global['publisher'] + '" />\n'
		headstring += '  <meta name="DC.Date" content="' + self.Global['lastmod'] + '" />\n'
		headstring += '  <meta name="DC.Identifier" content="' + self.Global['url'] + '" />\n'
		headstring += '  <meta name="DC.Language" content="' + self.Site_language + '" />\n'

		if "coverage" not in self.Global and "location" in self.Global:
			headstring += '  <meta name="DC.Coverage" content="' + self.Global['location'] + '" />\n'

		headstring += '  <meta name="DC.Rights" content="' + self.Global['publisher'] + '" />\n'
		
		for style in self.style:
			path1 = self.mainConfig["docrootpath"] + self.style[style]
			path2 = self.mainConfig["docrootpath"] + self.Site_actpath  + self.style[style]
			path3 = self.mainConfig["docrootpath"] + "favicon.ico"

			if os.path.exists(path1) and os.path.isfile(path1):
				headstring += '  <link rel="stylesheet" href="/' + self.style[style] + '" type="text/css" media="' + style + '" />\n'
			elif os.path.exists(path2) and os.path.isfile(path2):
				headstring += '  <link rel="stylesheet" href="/' + self.Site_actpath + self.style[style] + '" type="text/css" media="' + style + '" />\n'

			if os.path.exists(path3):
				headstring += '  <link rel="icon" href="/favicon.ico" />\n'
				headstring += '  <link rel="shortcut.icon" href="/favicon.ico" />\n'

		if self.Global['title'] != "":
			if self.Global['title_begin'] != "":
				headstring += "  <title>" + self.Global['title_begin'] + " - " + self.Global['title'] + "</title>\n"
			else:
				headstring += "  <title>" + self.Global['title'] + "</title>\n"
		elif self.Global['description'] != "":
			headstring += "  <title>" + self.Global['description'] + "</title>\n"
		else:
			headstring += "  <title>" + self.Global['publisher'] + " - " + self.Global['location'] + "</title>\n"
		headstring += "</head>\n"
		return headstring

	"""
	def subNavi(Index, UseText = True):

		if Index.find("_") >= 0:
			Liste = Index.split("_")
			Cond = Liste[0]
			Index = Liste[1]

			if Cond[0] == "!":
				if self.Site_siteid == Cond[1:]:
					return

			else:
				if self.Site_siteid != Cond:
					return

		if UseText:
			LinkTest = self.seitendict["Sites" + Index + "-" + self.Site_language + "-text"]
		else:
			LinkText = ""

		if Index == self.Site_siteid:
			return LinkText

		urlstr = self.seitendict["Sites" + Index + "-" + self.Site_language + "-datei"]
		if urlstr[0, 7] == 'http://':
			LinkTarget = "Sites" + Index + "-" + self.Site_language + "-datei"

		else:
			LinkTarget = "/" + self.Site_languagepath + "Sites" + Index + "-" + self.Site_language + "-ordner"

			tfstr = self.seitendict["Sites" + Index + "-" + self.Site_language + "-datei"]
			if tfstr[0, 6] != "index.":
				LinkTarget += "Sites" + Index + "-" + self.Site_language + "-datei"

		return '<a href="' + LinkTarget + '\"> + LinkText + </a>'
	"""

	def subContent(self):
		target = self.Site_languagepath + self.Site_actpath + self.Site_file

		act_id = self.Site_siteid
		act_lang = self.Site_language
		act_lang_path = self.Site_languagepath
		key = self.Site_siteid + "-" + self.Site_language + "-" + "script"
		if key in self.seitendict:
			script = self.seitendict[key]
		else:
			script = ""

		ThisContent = ""
		linear_navi_code = ""

		s = self.Site_siteid + "-" + self.Site_language + "-" + "index_chapter"
		if s not in self.seitendict or self.seitendict[s] == "":
		
			linear_navi_code = '  <ul class="linear2">\n'

			NaviLinear = {
				0 : "next",
				1 : "prev",
				2 : "index_chapter",
				}

			for i in range(2):
				t = self.Site_siteid + "-" + self.Site_language + "-" + NaviLinear[i]
				if t in self.seitendict:
					target_id = self.seitendict[t]
				else:
					target_id = 0

				l = "Sites" + str(target_id) + "-" + self.Site_language
				if target_id != 0:

					link_target = act_lang_path + self.seitendict[l + "-ordner"]
					target_file = self.seitendict[l + "-datei"]

					if target_file[0:6] != "index.":
						link_target += target_file

					lexikonDict = config.main("lexikon.txt")
					linear_navi_code += '    <li><a href="/' + link_target + '">' + lexikonDict[act_lang] + "-" + NaviLinear[i]

					if "gal_navi_text" not in self.Global or self.Global["gal_navi_text"] == "":

						linear_navi_code += ": " + self.seitendict[l + "-title"]

					linear_navi_code += "</a></li>\n"

			linear_navi_code += "  </ul>\n"

		if ("linear_navi_code" != "" and self.Global['gal_navi_line'] == "top") or self.Global['gal_navi_line'] == "both":

			ThisContent += linear_navi_code

		if script != "":

			if os.path.isfile(self.mainConfig["homepath"] + "/" + script):
				script = self.mainConfig["homepath"] + "/" + script
				with open(script, "r") as f:
					exec(f.read())

			elif os.path.isfile(self.mainConfig["globalpath"] + "/" + script):
				script = self.mainConfig["globalpath"] + "/" + script
				with open(script, "r") as f:
					exec(f.read())
			else:

				print("<br /><em>WARNUNG: In ID " + act_id + " referenziertes Script " + script + " existiert nicht!</em>\n")
			self.Content = ''

		ThisContent += self.Content

		if os.path.isfile(self.mainConfig["templatespath"] + "/" + target):
			target = self.mainConfig["templatespath"] + "/" + target
			with open(target, "r") as f:
				ThisContent += f.read()
		else:
			print("<br /><em>WARNUNG: Datei " + target + " existiert nicht!</em>\n")

		if ThisContent == "":
			print("<br /><em>WARNUNG: Inhalt fuer " + self.mainConfig["templatespath"] + "/" + target + " existiert nicht!</em>\n")

		if os.path.isfile(self.mainConfig["templatespath"] + "/" + target + ".kontext"):
			kontext = self.mainConfig["templatespath"] + "/" + target + ".kontext"
			with open(kontext, "r") as f:
				ThisContent += f.read()

		if ("linear_navi_code" != "" and self.Global['gal_navi_line'] == "bottom") or self.Global['gal_navi_line'] == "both":
			ThisContent += linear_navi_code

		return ThisContent

	"""def subTag(Tag):
		ThisTemplate == ''
		if os.path.isfile(self.mainConfig["homepath"] + "/template." + Tag):
			tag = self.mainConfig["homepath"] + "/template." + Tag

			with open(tag, "r") as f:
				ThisTemplate += f.read()

		if os.path.isfile(self.mainConfig["globalpath"] + "/template." + Tag):
			tag =self.mainConfig["globalpath"] + "/template." + Tag

			with open(tag, "r") as f:
				ThisTemplate += f.read()

		return subTemplates(ThisTemplate)"""

	def subTemplates(self,ThisTemplate):

		szk = re.compile("@@@+\w+@@@")
		Matches = szk.findall(ThisTemplate)

		Matches = list(set(Matches))

		for Index in Matches:
#
#		if (strstr($Index, "@@@NAVI_")) {
#			$ThisTemplate = preg_replace("/$Index/", subNavi(substr($Index, 8, strlen($Index) - 11)), $ThisTemplate);
#			continue;
#		}
#
#		if (strstr($Index, "@@@NAVIGR_")) {
#			$ThisTemplate = preg_replace("/$Index/", subNavi(substr($Index, 10, strlen($Index) - 13), false), $ThisTemplate);
#			continue;
#		}
#
#		if (strstr($Index, "@@@INT_")) {
#			$ThisTemplate = preg_replace("/$Index/", $Globals[substr($Index, 7, strlen($Index) - 10)], $ThisTemplate);
#			continue;
#		}
#
#		if (strstr($Index, "@@@DICT_")) {
#			$ThisTemplate = preg_replace("/$Index/", $Dict[$Globals['language']][substr($Index, 8, strlen($Index) - 11)], $ThisTemplate);
#			continue;
#		}
#
#		if (strstr($Index, "@@@CONF_")) {
#			$ThisTemplate = preg_replace("/$Index/", $Config[substr($Index, 8, strlen($Index) - 11)], $ThisTemplate);
#			continue;
#		}
#
#		if (strstr($Index, "@@@TPL_")) {
#			$ThisTemplate = preg_replace("/$Index/", subTag(substr($Index, 7, strlen($Index) - 10)), $ThisTemplate);
#			continue;$

			if Index.find("@@@SCR_") >= 0:
				Tag = Index[7: -3]

				if Tag in self.templates:
					Content = ""

					paradict = {
						"act_id" : self.Site_siteid,
						"act_lang" : self.Site_language,
						"act_langpath" : self.Site_languagepath,
						"act_dir" : self.Site_actpath,
						"act_site_langpath" : self.Site_languagepath,
						"url" : self.Global['url'],
						"act_file" : self.Site_file,
						}
					if os.path.isfile(self.mainConfig["homepath"] + "/" + self.templates[Tag]):
						template = self.mainConfig["homepath"] + "/" + self.templates[Tag]
						if template[0:2]=="./":
							ai = 2
						else:
							ai = 0
						exec("import " + template[ai:-3])

					elif os.path.isfile(self.mainConfig["globalpath"] + "/" + self.templates[Tag]):
						template = self.mainConfig["globalpath"] + "/" + self.templates[Tag]
						if template[0:2]=="./":
							ai = 2
						else:
							ai = 0
						exec("import " + template[0:-3])

					Content = eval(template[ai:-3] + ".main(Content, paradict)")
					ThisTemplate = ThisTemplate.replace("@@@SCR_" + Tag + "@@@", Content)

				else:
					ThisTemplate = ThisTemplate.replace("@@@SCR_" + Tag + "@@@", "")
			if Index == "@@@CONTENT@@@":
				ThisTemplate = ThisTemplate.replace(Index, self.subContent())

		return ThisTemplate

