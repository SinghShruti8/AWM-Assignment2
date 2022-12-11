from django.contrib.gis import admin
from .models import WorldBorder, Search

admin.site.register(WorldBorder, admin.GISModelAdmin)
admin.site.register(Search)
