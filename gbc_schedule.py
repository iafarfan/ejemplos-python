# coding: utf-8
#
# Script Python para obtener la programación de GBC TV.
# Autor: Italo Farfán Vera

import urllib
import re

def gbc():
	connection = urllib.urlopen("http://gbc.gi/television/tv-schedule.php")
	output = connection.read()
	connection.close()
	t = re.findall('class="schelude_content_time"><h2>(.*?)</h2', output)
	p = re.findall('title="">\s\t\t\t(.*?)\t\t</a>', output)	
    
    	print "Today on GBC TV"
    	print "All timings are in Central European Time (CET):"
    	print "=============================================="
    	for i in range(len(t)):
    		print t[i], p[i]

gbc()
