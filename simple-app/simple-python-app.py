#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SimplePythonApp:

	def __init__(self):

		# 処理開始時刻
		import datetime
		self.datetime_string=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

		# 初期化
		self.flag=0;
		self.config={};

	def run(self):
		import sys, os, getopt

		# オプションの取得
		try:
			opts, args = getopt.getopt(sys.argv[1:],"fc:",["flag","config="])
		except getopt.GetoptError, err:
			print str(err)
			self.usage()
			sys.exit(2)
		for o,a in opts:
			if o in ("-c","--config"):
				self.load_config(a)
			if o in ("-f","--flag"):
				self.flag=1

		self.disp()
		sys.exit(0)

	def disp(self):
		# PrettyPrint
		import pprint
		print "開始日時: %(datetime)s" % { 'datetime' : self.datetime_string }
		print "フラグ: %s" % ( "有効" if self.flag else "無効" )
		print "Config:"
		pprint.PrettyPrinter(indent=4).pprint(self.config)

	# YAMLで書かれた設定ファイルをロードする。
	# PyYAMLのインストールが必要
	# $ pip install PyYAML
	def load_config(self,filename):
		import os.path, yaml

		if not os.path.exists(filename):
			print "%s がありません" % filename
			return 2

		print "Load: %s" % filename	
		with open(filename,'r') as f:
			data=yaml.load(f)
			f.close()

		self.config=data
		return 0

	def usage(self):
		import sys
		print "USAGE: %s commands" % sys.argv[0]
		exit(2)

	# ファイルに書く
	def write_file(self,filename,data):
		import os
		dirname=os.path.dirname(filename)

		if not os.path.exists(dirname):
			os.makedirs(dirname)

		print "Write: %s" % filename

		with open(filename,'w') as f:
			f.write(data)

if __name__ == "__main__":

	# ライブラリ関係をlibsディレクトリに置く
	def _startup():
	    from site import addsitedir
	    from os.path import dirname, realpath
	    addsitedir( dirname( realpath(__file__)) + '/../libs')
	_startup()

	# Python3で動作しているかチェック	
	import sys
	py3 = sys.hexversion >=  0x3000000
	
	SimplePythonApp().run();

