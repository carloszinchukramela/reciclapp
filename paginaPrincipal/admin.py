from django.contrib import admin

from paginaPrincipal.models import TipoDesecho
from paginaPrincipal.models import Oferente

# Register your models here.

admin.site.register(TipoDesecho)
admin.site.register(Oferente)