#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

class Utils:

	def __init__(self,**kwargs):
		from logging import basicConfig, getLogger
		basicConfig(level='DEBUG',format='[%(levelname)-8s] %(message)s');
		self.logger = kwargs.get('logger',getLogger(__name__));

	def load_yaml(self,filename):
		import os.path, yaml
		if not os.path.exists(filename):
			self.logger.error("%s がありません" % filename)
			return 2
		self.logger.info("Read: %s" % filename)
		with open(filename,'r') as f:
			data=yaml.load(f)
			f.close()
		return data
	
	def write_yaml(self,filename,data):
		import os.path, yaml
		dirname=os.path.dirname(filename)
		if not os.path.exists(dirname):
			os.makedirs(dirname)
		self.logger.info("Write: %s" % filename)
		with open(filename,'w') as f:
			f.write(data)

