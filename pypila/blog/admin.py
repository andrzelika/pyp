from django.contrib import admin
from blog.models import CzlonekRodziny

class CzlonekRodzinyAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'wiek', )
    search_fields = ('imie', 'nazwisko', )

admin.site.register(CzlonekRodziny, CzlonekRodzinyAdmin)
