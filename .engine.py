#! /bin/env python
#- coding: utf-8 -#
#- Import Libraries -#
import os
import sys
from search_engine_parser.core.engines.yandex import Search as YandexSearch
from search_engine_parser.core.engines.yahoo import Search as YahooSearch
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.bing import Search as BingSearch
from search_engine_parser.core.engines.ask import Search as AskSearch

import pprint
import time
import socket
os.system('clear')
#- check internet Connection -#
def connect():
   try:
      ip = socket.gethostbyname("www.google.com")
      con = socket.create_connection((ip, 80), 2)
      return True
   except socket.error:
         pass
   return False
if connect() !=True:
        os.system('printf "\e[1;31m"')
        print("Error: Please Check Your Intenrnet Connection ")
        exit(1)
from optparse import OptionParser
optparse = OptionParser("""
this script was written by Saeed Ahmeed
https://www.youtube.com/c/thebandblue
type python engine.py -h for more help
engine.py [Options]
-d / --domin :: domin
-e / --engine :: engine
example:
python engine.py -d sudani.sd -e yahoo
python engine.py --domim zain.sd --engine google
python engine.py -d mtn.play.sd -e all
""")
optparse.add_option("-d","--domin",dest="domin",type="string",help="Domain to search or company name")
optparse.add_option("-e","--engine",dest="engine",type="string",help="Engine: google, yahoo, baidu, aol, bing, ask, all")
(option,args) = optparse.parse_args()
if option.domin == None and option.engine == None:
	print(optparse.usage)
	exit(0)
elif option.engine not in ("google", "yahoo", "bing", "ask", "yandex", "all"):
	os.system('printf "\e[1;31m"')
	print ("Invalid search engine, try with: google, yahoo, bing, ask, yandex, all")
	exit(0)
else:
	if option.engine == "google":
		print ("[-] Searching in Google:")
		gsearch = GoogleSearch()
		gresults = gsearch.search(option.domin ,1)
		a = {
			"Google": gresults}
		for k, v in a.items():
			os.system('printf "\e[1;35m"')
			print(f"-------------{k}------------")
			#pprint.pprint(a[k]['links'])
			data_list = (a[k]['links'])
			data = '\n'.join(data_list)
			with open("google.txt","a") as f:
				f.write(f"-------------{k}------------\n")
				f.write(data)
	elif option.engine == "yahoo":
		print ("[-] Searching in Yahoo:")
		yasearch = YahooSearch()
		yaresults = yasearch.search(option.domin ,1)
		a = {
			"Yahoo": yaresults}
		for k, v in a.items():
			os.system('printf "\e[1;35m"')
			print(f"-------------{k}------------")
			#pprint.pprint(a[k]['links'])
			data_list = (a[k]['links'])
			data = '\n'.join(data_list)
			with open("yahoo.txt","a") as f:
				f.write(f"-------------{k}------------\n") 
				f.write(data)
	elif option.engine == "bing":
		print ("[-] Searching in Bing:")
		bsearch = BingSearch()
		bresults = bsearch.search(option.domin ,1)
		a = {
			"Bing": bresults}
		for k, v in a.items():
			os.system('printf "\e[1;35m"')
			print(f"-------------{k}------------")
			#pprint.pprint(a[k]['links'])
			data_list = (a[k]['links'])
			data = '\n'.join(data_list)
			with open("bing.txt","a") as f:
				f.write(f"-------------{k}------------\n") 
				f.write(data)
	elif option.engine == "ask":
		print ("[-] Searching in Ask:")
		asearch = AskSearch()
		aresults = asearch.search(option.domin ,1)
		a = {
			"Ask": aresults}
		for k, v in a.items():
			os.system('printf "\e[1;35m"')
			print(f"-------------{k}------------")
			#pprint.pprint(a[k]['links'])
			data_list = (a[k]['links'])
			data = '\n'.join(data_list)
			with open("ask.txt","a") as f:
				f.write(f"-------------{k}------------\n") 
				f.write(data)
	elif option.engine == "yandex":
		print ("[-] Searching in Yandex:")
		ysearch = YandexSearch()
		yresults = ysearch.search(option.domin ,1)
		a = {
			"Yandex": yresults}
		for k, v in a.items():
			os.system('printf "\e[1;35m"')
			print(f"-------------{k}------------")
			#pprint.pprint(a[k]['links'])
			data_list = (a[k]['links'])
			data = '\n'.join(data_list)
			with open("yandex.txt","a") as f:
				f.write(f"-------------{k}------------\n") 
				f.write(data)
	elif option.engine == "all":
		os.system('printf "\e[1;34m"')
		print ("[-] Searching in All Engies:")
		gsearch = GoogleSearch()
		yasearch = YahooSearch()
		bsearch = BingSearch()
		asearch = AskSearch()
		ysearch = YandexSearch()
		gresults = gsearch.search(option.domin ,1)
		yaresults = yasearch.search(option.domin ,1)
		bresults = bsearch.search(option.domin ,1)
		aresults = asearch.search(option.domin ,1)
		yresults = ysearch.search(option.domin ,1)
		a = {
			"Google": gresults,
			"Yahoo": yaresults,
			"Bing": bresults,
			"Ask": aresults,
			"Yandex":yresults}
			# pretty print the result from each engine
		for k, v in a.items():
			os.system('printf "\e[1;40m"')
			#print(f"\n-------------{k}------------")
			#pprint.pprint(a[k]['links'])
			data_list = (a[k]['links'])
			data = '\n'.join(data_list)
			with open("all.txt","a") as f:
				f.write(f"\n-------------{k}------------\n") 
				f.write(data)
