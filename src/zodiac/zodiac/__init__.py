from pyramid.config import Configurator
from resources import Root
import views
import os

__here__ = os.path.dirname(os.path.abspath(__file__))

def make_app():
    """ This function returns a Pyramid WSGI application.
    """
    settings = {}
    settings['mako.directories'] = os.path.join(__here__, 'templates')
    config = Configurator( root_factory=Root, settings=settings )
    
    config.add_view(views.root_view,
                    context=Root,
                    renderer='main.mako')

    #config.add_route( "create_page", "/create_page" )
    #config.add_view( views.create_page_view, route_name="create_page", renderer="create_page.mako" )

    #config.add_route( "view_page", "/view_page/{id}" )
    #config.add_view( views.view_page_view, route_name="view_page", renderer="view_page.mako" )

    config.add_static_view(name='static',
                           path=os.path.join(__here__, 'static'))
    
    return config.make_wsgi_app()

application = make_app()
