#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  config.py
#  
#  Copyright Rainer Kersten and Penny for the PHP-Scripts
#  Copyright 2013, 2014 Mechtilde Stehmann <ooo@mechtilde.de>
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

import os

class makeConfig(object):

	def __init__(self):
		pass

	def fileRead(self, rfile):
		items = {}
		if os.path.exists(rfile) and os.path.isfile(rfile):
			fobj = open(rfile, "r")
			lineslist = fobj.readlines()
			for line in lineslist:
				line = line.strip()
				line = self.dealComments(line)
				if line != "":
					entry = line.split(":")
					if len(entry) >= 2:
						items[entry[0].strip()] = entry[1].strip()
			fobj.close()
		else:
			items = {}
			print(rfile + " existiert nicht!")
		return items

	def dealComments(self, line):
		entry = line.split("#")
		return entry[0]


def main(ConfigFile):

	mc = makeConfig()
	configdict = mc.fileRead(ConfigFile)

	return configdict

if __name__ == '__main__':
#	a = main("style.txt")
	b = main("config.txt")
#	c = main("lexikon.txt")
#	print(a)
	print(b)
#	print(c)
