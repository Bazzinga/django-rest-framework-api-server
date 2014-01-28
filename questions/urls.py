from django.conf.urls import patterns, include, url
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = patterns('',
    url(r'^v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/auth/token/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^v1/', include(router.urls))
)
