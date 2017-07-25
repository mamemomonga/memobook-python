#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

class SimplePythonApp2:

	def __init__(self,**kwargs):
		from logging import basicConfig, getLogger
		basicConfig(level='DEBUG',format='[%(levelname)-8s] %(message)s');
		self.logger = kwargs.get('logger',getLogger(__name__));

		self.flag   = kwargs.get('flag',False)
		self.config = kwargs.get('config',{})

		self._set_start_time()

	def _set_start_time(self):
		import datetime
		self.datetime_string=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

	def _dump(self):
		import pprint
		print "Config:"
		pprint.PrettyPrinter(indent=4).pprint(self.config)

	def run(self):
		self.logger.info("開始日時: %(datetime)s" % { 'datetime' : self.datetime_string })
		self.logger.info("フラグ: %s" % ( "有効" if self.flag else "無効" ))
		self._dump()


