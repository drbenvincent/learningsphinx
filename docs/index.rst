.. learningsphinx documentation master file, created by
   sphinx-quickstart on Fri Nov 11 12:45:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to learningsphinx's documentation!
==========================================

Nothing to see here. This is just a test repository for Ben to learn sphinx and to experiment without breaking docs in a real, in-production, package.

This page is written in ``.rst``.

.. toctree::
   :titlesonly:

   quickstart
   some_info.md

.. toctree::
   :caption: Examples
   :titlesonly:

   notebooks/example1.ipynb
   notebooks/example2.ipynb

.. toctree::
   :caption: API Reference
   :titlesonly:

   apidocs

This is a title
===============

sdfsdgsdg

.. note::

   This is my note


Blar Blar

.. code-block:: python

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'

Some maths

.. math::

   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2


Indices
=======

* :ref:`genindex`
* :ref:`modindex`

