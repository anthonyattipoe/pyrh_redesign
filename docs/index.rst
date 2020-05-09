.. pyrh_redesign documentation master file, created by
   sphinx-quickstart on Fri May  8 16:33:04 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. image:: https://imgur.com/U4A1ciD.png
   :target: https://github.com/anthonyattipoe/pyrh_redesign/
   :alt: robinhood-logo

-------------------------------------------------------------

Welcome to pyrh_redesign's documentation!
=========================================

pyrh_redesign (a pyrh API Wrapper)
**********************************


Python Framework to make trades with Unofficial Robinhood API. Supports Python 3.6+


API Reference
#############

.. toctree::
   :maxdepth: 3
   
   api

* :ref:`search`

Github Repo
###########
`Repo Here <https://github.com/anthonyattipoe/pyrh_redesign>`_

Quickstart
**********

.. code-block:: python

   import pyrh_redesign as rh

   email = YOUR_EMAIL
   password = YOUR_PASSWORD

   rh.begin_robinhood_session(email, password)
   ...
   # use robinhood
   ...
   rh.end_robinhood_session()


.. How To Install:
.. ***************

.. .. code-block::

..    pip install pyrh


Related
*******

* See the original `blog post <https://medium.com/@rohanpai25/reversing-robinhood-free-accessible-automated-stock-trading-f40fba1e7d8b>`_.
