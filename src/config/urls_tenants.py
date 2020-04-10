"""TENANTS ROUTING

routing for tenants zone

- all routes use language code prefix (ex: /en/dashboard)

"""


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.static import static


urlpatterns = [
    path('api/', include('modules.lists.api_urls', namespace='list_api')),
    path('api/', include('modules.address_book.api_urls', namespace='addressbook_api')),
    path('api/', include('modules.profile_page.api_urls', namespace='user_lists_api')),
    path('api/', include('modules.articles.api_urls', namespace='articles_api')),
    path('api/', include('modules.branches.api_urls', namespace='branches_api')),
    path('api/', include('modules.warehouse.api_urls', namespace='warehouses_api')),
    path('api/', include('modules.settings.api_urls', namespace='settings_api')),

    url(r'^select2/', include('django_select2.urls')),

    path('', include('modules.account.urls_inapp')),
    path('', include('modules.lists.urls_inapp')),
    path('', include('modules.address_book.urls_inapp', namespace='addressbook')),
    path('', include('modules.redirections.urls_tenants', namespace='redirections')),
    path('', include('modules.dashboard.urls', namespace='dashboard')),
    path('', include('modules.profile_page.urls_inapp', namespace='profile_page')),
    path('', include('modules.branches.urls_inapp', namespace='branches')),
    path('', include('modules.articles.urls_inapp', namespace='articles')),
    path('', include('modules.settings.urls_inapp', namespace='settings')),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
