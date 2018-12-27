#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2018, Yue-Wen FANG.
License: MIT License (see LICENSE for details)
"""


__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'MIT License'
__creation_date__= 'Dec. 27, 2018'

"""
This script is used for command line mode of vaspwiki through 'entry point'.
In this method, the relevant modules of the python scripts can be used as 
command.
"""

from vaspwiki import vaspwiki

def vaspwiki_command():
    vaspwiki.main()
