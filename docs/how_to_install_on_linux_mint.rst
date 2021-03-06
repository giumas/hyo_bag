BAG library on Linux Mint
=========================

This document describes a tested configuration to install the BAG library on Linux Mint.

For use with a VM image:

* Download from here: http://www.osboxes.org/linux-mint/#linuxmint-173-rosa-vmware
* Change Display resolution *[optional]*
* Install VM Tools using Software Manager (select open-vm-tools-desktop) *[optional]*


Installation:

* Download 64-bit Python 3.6 miniconda: http://conda.pydata.org/miniconda.html
* Install it from terminal: ``bash Miniconda-latest-Linux-x86_64.sh``
* Install dependencies using conda (since with pip they may fail): ``conda install numpy matplotlib gdal lxml spyder``
* Finally use pip for hyo.bag: ``pip install hyo.bag``


Test:

* Open Spyder using the terminal: ``spyder``
* Write in the temp.py:

.. code-block:: python

   from hydroffice import bag
   print("BAG version: %s" % bag.__version__)

* Run the script and you should get the library version without errors:

.. image:: ./_static/linux_mint_spyder.png
    :align: center
    :alt: Spyder

.. NOTE::
   If you get issues on the installation, you may open a ticket:

   * https://bitbucket.org/ccomjhc/hyo_bag/issues?status=new&status=open
   * https://github.com/giumas/hyo_bag/issues
