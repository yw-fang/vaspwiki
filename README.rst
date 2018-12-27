###############################################################
vaspwiki: an easy way to getting access to the VASP manual
###############################################################
.. image:: https://travis-ci.com/yw-fang/vaspwiki.svg?branch=master
    :target: https://travis-ci.com/yw-fang/vaspwiki

=============
Introduction
=============

The VASP team hosts a very useful
`online VASP manual <https://cms.mpi.univie.ac.at/wiki/index.php/The_VASP_Manual>`_,
here,
I provide a python interface so that other colleagues in the community of computational
materials and physics
can get access to vaspwiki much easier via executing
commands in their terminals (Linux, Windows, and Mac OS).
The corresponding wiki page of the requested keyword will show up in your default **web browser**.
(We may need install x11 windows in some terminals)
Searching for several keywords in a batch way
is supported, see details in the section of Usage.

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



=============
Usage
=============

Note that vaspwiki is case-sensitive.

Search for one keyword:

 $ vaspwiki INCAR

Search for multiple keywords in one shot:

 $ vaspwiki INCAR LOCPOT

We can also use vaspwiki in the interactive ipython:

 In [1]: from vaspwiki import vaspwiki

 In [2]: vaspwiki.help_function('INCAR')

=============
License
=============
MIT LICENSE. See LICENSE file for more details.