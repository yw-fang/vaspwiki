###############################################################
vaspwikipy: an easy way to getting access to vaspwiki
###############################################################
.. image:: https://travis-ci.com/yw-fang/vaspwiki.svg?branch=master
    :target: https://travis-ci.com/yw-fang/vaspwiki

=============
Introduction
=============

The VASP team hosts a very useful
`online manual of VASP <https://cms.mpi.univie.ac.at/wiki/index.php/The_VASP_Manual>`_,
here,
I provide a python interface so that other colleagues in the community of computational
materials and physics
can get access to vaspwiki much easier via executing
commands in their terminals (Linux, Windows, and Mac OS).
The corresponding wiki page of the requested keyword will show up in your default **web browser**.
(You may need install x11 windows in some Linux systems)

=============
Installation
=============

- Step 1: install vaspwiki to your virtual environment

To install vaspwiki, use

 $ pip install vaspwiki

or

 $ git clone https://github.com/yw-fang/vaspwiki.git

 $ cd vaspwiki

 $ python setup.py install

- Step 2: check the path of vaspwiki in your computer

Open the interactive ipython interface and check the installed
path of vaspwki:

 In [1]: import vaspwiki

 In [2]: vaspwiki

 Out[2]: <module 'vaspwiki' from '/Users/ywfang/miniconda3/lib/python3.6/site-packages/vaspwiki/__init__.py'>

Exit the ipython interface.

- step 3: create a soft link of vaspwiki.py to $HOME/.local/bin so that you can run vaspwiki as a command.

Please
double check that the path of $HOME/.local/bin is indeed in your environment file .bashrc before preceding.

 $ ln -s /Users/ywfang/miniconda3/lib/python3.6/site-packages/vaspwiki/vaspwiki.py /Users/ywfang/.local/bin/vaspwiki

 $ chmod +x /Users/ywfang/.local/bin/vaspwiki

Finished.



=============
Usage
=============

Note that vaspwiki is case-sensitive.

Search for one keyword:

 $ vaspwiki INCAR

Search for multiple keywords in one shot:

 $ vaspwiki INCAR LOCPOT

We can also use vaspwiki in the interactive ipython:

 In [1]: import vaspwiki

 In [2]: from vaspwiki import vaspwiki

 In [3]: vaspwiki.help_function('INCAR')

=============
License
=============
MIT LICENSE. See LICENSE file for more details.