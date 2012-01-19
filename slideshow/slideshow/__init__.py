from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'slideshow:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_view('slideshow.views.my_view',
                    route_name='home',
                    renderer='templates/s5.pt')
                    # renderer='templates/slidy.pt')
    return config.make_wsgi_app()

