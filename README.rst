============================
GNU Terry Pratchett for WSGI
============================

Simple WSGI middleware for adding Terry Pratchett's header to your requests.


-----
Usage
-----

.. code-block:: python
    from pratchett import GNUTerryPratchett

    # ... your code here, create your WSGI application
    app = GNUTerryPratchett(your_app)
