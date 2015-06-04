#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  generate.py
#  Copyright Rainer Kersten and penny for the PHP-Scripts
#  Copyright 2013 - 2014 Mechtilde Stehmann <ooo@mechtilde>
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
import functions
import os
import re
import sys

def _(String):
	"""solange keine gettext Integration erfolgt ist, ist dies ein dummy"""
	return String

class Generate(object):

	def __init__(self):
		self.ARGV_GENALL = False
		self.ARGV_GENFILELIST = False
		self.ARGV_MKDIR = False

		if len(sys.argv) > 1:
			for i in range(len(sys.argv)):
				if i == "-a":
					self.ARGV_GENALL = True
				if i == "-f":
					self.ARGV_GENFILELIST = True
				if i == "-p":
					self.ARGV_MKDIR = True

		if len(sys.argv) >= 2 and (sys.argv[1] == '--help' or sys.argv[1] == '-h'):
			print(_("Usage:") +" generate [-h|--help] " + _("[-a] generate all pages, [-f] generate filelist, [-p] gereate directories"))
			sys.exit(1)

		self.mainConfig = config.main("config.txt")
		self.seitendict = config.main("seiten.txt")

	def readIndexTemplate(self):
		with open("template.index", "r") as f:
			self.IndexTemplate = f.read()

		print("<h1>WWW2.0</h1>\n<p>Ich suche aktuelle Änderungen.</p>\n")

	#def generateSitemap(self):
		"""#echo "<p>Generiere Sitemap(s) ...";
		#include($Path['global'] . "/sitemap.php");$
		#echo " <br />done.</p>\n";

		if (file_exists($Path['home'] . "/linkfeld.php")) {
			echo "<p>Generiere Linkseite(n) ...";
			include($Path['global'] . "/linklist.php");
			echo " done.</p>\n";
		}"""

	def generatePages(self):
		seitenzaehler=0;
		file_list = "";
		print("\n<p>Seiten werden geschrieben:\n")

		for Site in self.seitendict:
			s = Site.split("-")

			Site_siteid = s[0]
			Site_siteid = Site_siteid.replace("Sites", "")

			Site_language = s[1]
			Site_languagepath = config.main("sprachen.txt")[s[1] + "-pfad"]
			Site_actpath = self.seitendict[s[0] +"-" + s[1] + "-ordner"]
			Site_file = self.seitendict[s[0] +"-" + s[1] + "-datei"]

			if Site_file != "":
				if Site_languagepath[-1:] != "" and Site_languagepath[-1:] != "/":
					Site_languagepath = Site_languagepath + "/"
				if Site_actpath[-1:] != "" and Site_actpath[-1:] != "/":
					Site_actpath = Site_actpath + "/"
				Site_target = Site_languagepath + Site_actpath + Site_file

				Funktionen = functions.Funktionen()
				Funktionen.setGlobals(Site_siteid,Site_language,Site_languagepath,Site_actpath,Site_file)

				ThisSite = Funktionen.mkHead() + self.IndexTemplate
				i = 0
				while ThisSite.find("@@@") >= 0:
					ThisSite = Funktionen.subTemplates(ThisSite)

				Target = self.mainConfig["docrootpath"] + "/" + Site_target
				if self.ARGV_MKDIR and not os.path.exists(self.mainConfig["docrootpath"] + Site_languagepath + Site_actpath):

					Meldung = Funktionen.myMkDir(self.mainConfig["docrootpath"] + Site_languagepath + Site_actpath)
					print(Meldung)

				try:
					with open(Target, "r") as f:
						myOrig = f.read()
				except:
					myOrig = ""

				if (myOrig != ThisSite) or self.ARGV_GENALL:
					try:
						with open(Target, "w") as f:
							f.write(ThisSite)
					except:
						print("<p>error writing file: " + Target + "</p>\n")
						print("ThisSite: " + ThisSite)

					if self.ARGV_GENFILELIST:
						file_list += "Target "

					print(".")
					seitenzaehler += 1

		print("\n<br />"+ str(seitenzaehler) + " Seiten wurden geschrieben.</p>\n")

		if len(file_list) > 0:
			print("FILELIST: " + str(file_list) + "\n")

def main():
	g = Generate()
	g.readIndexTemplate()
	g.generatePages()
	

if __name__ == '__main__':
	main()
