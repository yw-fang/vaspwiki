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

import webbrowser
import sys

index_wiki = "https://cms.mpi.univie.ac.at/wiki/index.php/"


def help_function(pattern):
    url = index_wiki + pattern
    newtab = 2
    webbrowser.get().open(url, new=newtab)


def main():
    pattern_list = sys.argv[1:]
    for pattern in pattern_list:
        help_function(pattern)


if __name__ == "__main__":
    main()