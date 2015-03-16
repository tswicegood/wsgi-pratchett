============================
GNU Terry Pratchett for WSGI
============================

Simple WSGI middleware for adding Terry Pratchett's header to your requests.


-----
Usage
-----

WSGI middleware is pretty simple.  Wrap your WSGI application in an instance of
``GNUTerryPratchett`` and you're set.

.. code-block:: python

    from pratchett import GNUTerryPratchett

    # ... your code here, create your WSGI application
    app = GNUTerryPratchett(your_app)
