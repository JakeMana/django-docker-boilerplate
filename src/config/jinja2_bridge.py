from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.utils import translation

from jinja2 import Environment, PackageLoader, select_autoescape

def environment(**options):
    env = Environment(extensions=['jinja2.ext.i18n', 'jinja2.ext.with_'], **options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.install_gettext_translations(translation)
    return env