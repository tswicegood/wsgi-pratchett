============================
GNU Terry Pratchett for WSGI
============================

Simple WSGI middleware for adding Terry Pratchett's header to your requests per
the conversation that's happening `on reddit`_

.. _on reddit: https://www.reddit.com/r/discworld/comments/2yt9j6/gnu_terry_pratchett


-----
Usage
-----

WSGI middleware is pretty simple.  Wrap your WSGI application in an instance of
``GNUTerryPratchett`` and you're set.

.. code-block:: python

    from pratchett import GNUTerryPratchett

    # ... your code here, create your WSGI application
    app = GNUTerryPratchett(your_app)


When using PasteDeploy configuration files you can also add the middleware there.

.. code-block:: ini

    # Your main application
    [app:main]
    filter-with = pratchett

    [filter:pratchett]
    use = egg:wsgi-pratchett
