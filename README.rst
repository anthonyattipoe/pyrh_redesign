.. image:: https://imgur.com/U4A1ciD.png
   :target: https://github.com/anthonyattipoe/pyrh_redesign/
   :alt: robinhood-logo

-------------------------------------------------------------

pyrh_redesign
*************
(a pyrh API Wrapper)
********************


Python Framework to make trades with Unofficial Robinhood API. Supports Python 3.6+


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
