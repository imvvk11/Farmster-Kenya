"""farmster_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from farmster_server import utils
from farmster_server.api_urls import api_urlpatterns

urlpatterns = i18n_patterns(
    path('grappelli/', include('grappelli.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^auth/', include('app_auth.urls')),
    url(r'^admin/', admin.site.urls),
    path("rest-auth/", include("rest_auth.urls")),
    url(r'^', include(api_urlpatterns)),
)

# urlpatterns += i18n_patterns()

if settings.SERVE_MEDIA:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = utils.custom404
handler500 = utils.custom500
