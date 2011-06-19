js.jqgrid
*********

Introduction
============

This library packages `jqgrid`_ for `fanstatic`_.

.. _`fanstatic`: http://fanstatic.org
.. _`jqgrid`: http://www.trirand.com/jqgridwiki/

To include the grid, call 

    js.jqgrid.jqgrid.need()

then you also need to add
a language, for example 

    js.jqgrid.jqgrid_i18n_en.need()

This requires integration between your web framework and ``fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``js.jqgrid``) are published to some URL.

The provided jqgrid code is licenced under MIT and GPL, the integration code
uses a BSD Licence.

