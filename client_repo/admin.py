from django.conf.urls import patterns
from django.contrib import admin
from client_repo import models
from client_repo.views import HostDetailView

class HostAdmin(admin.ModelAdmin):
    list_display = ('lfd_nr', 'hostname', 'typ', 'ip', 'mac')
    search_fields = ("hostname", "ip", "mac", "users__firstname", "users__lastname", "users__username")
    filter_horizontal = ("users",)
    list_filter = ('typ', 'os_installiert', 'hersteller', 'haus')

    def get_urls(self):
        urls = super(HostAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^host_detail/(?P<pk>\d+)', HostDetailView.as_view())
        )
        return my_urls + urls

admin.site.register(models.Host, HostAdmin)

class UserAdmin(admin.ModelAdmin):
    fields = ("firstname", "lastname", "username", "phone", "mobile", "host_list")
    readonly_fields = ("host_list",)
    list_display = ("firstname", "lastname", "username", "phone", "mobile")
    search_fields = ("firstname", "lastname", "username", "phone", "mobile", "hosts__hostname")

admin.site.register(models.User, UserAdmin)

class StockwerkAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Stockwerk, StockwerkAdmin)

class HausAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Haus, HausAdmin)

class StandortAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Standort, StandortAdmin)

class AbteilungAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Abteilung, AbteilungAdmin)

class GeraetetypAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Geraetetyp, GeraetetypAdmin)

class HerstellerAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Hersteller, HerstellerAdmin)

class ModellAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Modell, ModellAdmin)

class LieferantAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Lieferant, LieferantAdmin)

class OsAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Os, OsAdmin)

class WarrantyAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Warranty, WarrantyAdmin)

class VirtuelleUmgebungAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.VirtuelleUmgebung, VirtuelleUmgebungAdmin)
