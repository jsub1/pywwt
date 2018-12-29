About
=====

Scripts to make conda distributions that include pywwt and all dependencies.
This is provided for convenience for e.g. tutorials where the internet may not
be good enough for a regular conda installation.

Current built versions can be found [here](https://www.dropbox.com/sh/xb38lj17o8sdq6s/AAB6V4stHprY4RT7TV2JNBHla?dl=0>).

Usage
=====

About
-----

The **pywwtconda** distribution is a standalone conda distribution/environment that
includes Python and PyWWT (along with all its dependencies). This is not the
recommended method of installation for regular use if you already have other
Python installations (instead you should try and install PyWWT into your existing
installations using instructions [here](https://pywwt.readthedocs.io/en/stable/installation.html)), but it can provide
an easy way to get started, especially during workshops/tutorials.

Important note
---------------

Using the installers below will create a ``pywwtconda`` folder in your home
directory and will optionally add ``pywwtconda/bin`` to your path. Since
``pywwtconda/bin`` contains a ``python`` executable, this may take precedence
over other Python installations, hence why it is preferable if possible to
install PyWWT into your existing Python environments. See lower down for
instructions about removing pywwtconda.

Installing
----------

On MacOS X and Linux, run the installers using e.g.:

    bash pywwtconda-stable-Linux-x86.sh

On Windows, download and run the installer.

Uninstalling
------------

To uninstall, remove the ``pywwtconda`` folder from your home directory.

Updating packages
-----------------

If you decide to continue using **pywwtconda**, and a new version of PyWWT or
other packages becomes available, you can easily update all packages using::

    conda update -c pywwt --all
