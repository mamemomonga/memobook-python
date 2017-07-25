#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

def _startup():
	from site import addsitedir
	from os.path import dirname, realpath, abspath
	basedir = abspath(dirname( realpath(__file__)) + '/.' )
	sitedir = basedir + '/libs'
	addsitedir( sitedir )
	return basedir
basedir = _startup()

def _logger():
	from logging import getLogger, StreamHandler, Formatter, DEBUG
	import sys
	logger = getLogger(__name__)
	handler = StreamHandler(sys.stderr)
	handler.setFormatter( Formatter(fmt='[%(asctime)-15s][%(levelname)-8s] %(message)s'))
	handler.setLevel(DEBUG)
	logger.setLevel(DEBUG)
	logger.addHandler(handler)
	logger.propagate = False
	return logger
logger = _logger()

from TheApplication import SampleApp
from Utils import Utils

def main():
	import argparse,sys
	logger.info("サンプルアプリケーション")

	parser = argparse.ArgumentParser(description='サンプルアプリケーション')
	parser.add_argument('-c', '--config', type=str, help='設定', required=True ) 
	parser.add_argument('-f', '--flag', help='フラグを有効にする', dest='flag', action='store_true') 
	args = parser.parse_args()

	utils = Utils(logger=logger)

	app = SampleApp(
		logger = logger,
		config = utils.load_yaml(args.config),
		flag   = args.flag
	)

	app.run()

if __name__ == '__main__':
	main()
