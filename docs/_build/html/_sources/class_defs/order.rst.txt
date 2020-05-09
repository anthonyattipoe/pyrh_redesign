pyrh_redesign.order
===================

.. automodule:: order

.. autoclass:: Order

   .. rubric:: Methods


   .. autosummary::

      ~Order.__init__

      ~Order.__str__

      ~Order.place

      ~Order.cancel

      ~Order.status

   .. autoclass:: order::Order.Type

   .. rubric:: Types

   =============================== ===========
   Types                           Defintion
   =============================== ===========
   BUY                             Buy an order at the current value
   SELL                            Sell an order at the current value
   LIMIT_BUY_ORDER                 Buy an order at or below a specified maximum price level
   LIMIT_SELL_ORDER                Sell an order at or above a specified minimum price level
   MARKET_BUY_ORDER                Buy an order at the current market value
   MARKET_SELL_ORDER               Sell an order at the current market value
   STOP_LIMIT_BUY_ORDER            Once the designated stop price is reached, a stop-limit order becomes a limit order that will be executed at a specified price or lower
   STOP_LIMIT_SELL_ORDER           Once the designated stop price is reached, a stop-limit order becomes a limit order that will be executed at a specified price or higher
   STOP_LOSS_BUY_ORDER             Buy an order once the stock reaches a certain market price
   STOP_LOSS_SELL_ORDER            Sell an order once the stock reaches a certain market price
   =============================== ===========

   .. autoclass:: order::Order.TimeInForce

   .. rubric:: Time in Forces

   ============ ================
   Duration     Definition
   ============ ================
   GFD          Good for Day - Good until end of market hours
   GTC          Good til Cancelled - Good until the user cancels the order
   ============ ================

   .. autoclass:: order::Order.Status

   .. rubric:: Statuses

   ============ ================
   Status       Definition
   ============ ================
   UNPLACED     Order has been made but not placed
   UNCONFIRMED  Order has not been confirmed
   UNFILLED     Order has not been filled
   FILLED       Order has been completed and filled
   CANCELLED    Order has been cancelled by Robinhood or User
   UNKNOWN      Default value if none other matches
   ============ ================


   .. automethod:: __init__

   .. automethod:: __str__

   .. automethod:: place

   .. automethod:: cancel

   .. automethod:: status


