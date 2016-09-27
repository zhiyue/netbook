from __future__ import absolute_import
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = 'zhiyue'
__copyright__ = "Copyright 2016"
__credits__ = ["zhiyue"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "zhiyue"
__email__ = "cszhiyue@gmail.com"
__status__ = "Production"


from celery import Celery

app = Celery('netbook', include=['tasks'])

app.config_from_object('config')

if __name__ == '__main__':
    app.start()