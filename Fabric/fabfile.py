# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import logging
from fabric.api import *
from fabric.contrib.files import *

# SSH(paramiko)エラーを捕捉する
logging.getLogger('paramiko.transport').addHandler(logging.StreamHandler())

# .ssh/config を使うかどうか
env.use_ssh_config = False

@task
def thetask():
	pass

