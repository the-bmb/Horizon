from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet
from .views import FlightViewSet
from .views import TravelersViewSet
from .views import TravelViewSet
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'travelers', TravelersViewSet)
router.register(r'travel', TravelViewSet)

urlpatterns = [
    path('', include_docs_urls(title='TNS API')),
    path('api/v1/', include(router.urls)),
]
