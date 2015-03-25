HEADER = ("X-Clacks-Overhead", "GNU Terry Pratchett")


class GNUTerryPratchett(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        def clacker(status, headers, *args, **kwargs):
            if HEADER not in headers:
                headers.append(HEADER)
            return start_response(status, headers, *args, **kwargs)

        return self.app(environ, clacker)


def make_filter(global_conf):
    return GNUTerryPratchett
