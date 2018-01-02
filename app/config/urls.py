from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^sso/admin/', admin.site.urls),
    url(r'^sso/cas/', include('cas_server.urls', namespace="cas_server")),
    url(r'^sso/$', RedirectView.as_view(url='/sso/admin/')),
    url(r'^$', RedirectView.as_view(url='/sso/admin/')),
]
