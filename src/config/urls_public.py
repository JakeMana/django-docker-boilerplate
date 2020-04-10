"""PUBLIC ROUTING

routing for public zone

- all routes except admin use language code prefix (ex: /en/about)

"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.static import static

urlpatterns = [
    path('int/mngmt/db-admin/', admin.site.urls)
]

urlpatterns = [
    # landing for jumps from tenants to main domain
    path('', include('modules.redirections.urls_public', namespace='redirections')),
    path('', include('modules.account.urls_access', namespace='account')),
    path('', include('modules.dashboard.urls', namespace='dashboard')),  # create block for this url
    path('', include('django.contrib.auth.urls')),
    path('', include('modules.account.urls_inapp')),

    url(r'^select2/', include('django_select2.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
