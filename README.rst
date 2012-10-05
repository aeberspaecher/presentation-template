===================================
A template for a LaTeX presentation
===================================

About
=====

This is a template for a scientific LaTeX presentation created by
Alexander Eberspächer. It uses the beamer class and defines a
beautiful light style.

Build/Usage
===========

The ``waf`` build system is used for the presentation. It seems ``waf`` is smart enough to detect changed input files (and
graphics) and trigger a rebuild if necessary.

Configure & Build
-----------------

Type
::

  ./waf configure

to configure the project and
::

  ./waf build

to create output in the ``build`` folder. If you want to open the PDF via
the standard PDF viewer (found by ``xdg-open``), type ``./waf build --view``.

Cleaning up
-----------

The command
::

  ./waf distclean

removes *all* files created by ``waf``, whereas
::

  ./waf clean

removes the output only.

Notes
=====

The template uses many different LaTeX packages - most of which are only
used for convenience of the original author, Alexander Eberspächer. In your
talks, you may need less mathematical packages. However, note that all
packages are included in a full TeXlive installation.
