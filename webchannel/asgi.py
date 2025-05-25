from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from echo import routing as echo_routing
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webchannel.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack( 
        URLRouter(
            echo_routing.websocket_urlpatterns
        )
    ),
})    
