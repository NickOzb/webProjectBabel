from django.contrib import admin
from .models import *

# Register your models here.
class KategoriiAdmin(admin.ModelAdmin):
    list_display = ('namekategorii',)
admin.site.register(Kategoriitovara, KategoriiAdmin)

class TovarAdmin(admin.ModelAdmin):
    list_display = ('name','edizm','kodkategorii')
admin.site.register(Tovar, TovarAdmin)

class BankAdmin(admin.ModelAdmin):
    list_display = ('namebanka',)
admin.site.register(Bank, BankAdmin)

class NalogiAdmin(admin.ModelAdmin):
    list_display = ('namenaloga','percent')
admin.site.register(Nalogi, NalogiAdmin)

class DvizhenieAdmin(admin.ModelAdmin):
    list_display = ('articul','kolvotovara','cena')
admin.site.register(Dvizhenie,DvizhenieAdmin)

class OrganizatsiyaAdmin(admin.ModelAdmin):
    list_display = ('nameorg','kodbanka','schetorg','adress','fioruk','phone')
admin.site.register(Organizatsiya, OrganizatsiyaAdmin)

class NakladnieAdmin(admin.ModelAdmin):
    list_display = ('nnakladnoy','date','priznak','kodorg')
admin.site.register(Nakladnie, NakladnieAdmin)

class PodrazdeleniyaAdmin(admin.ModelAdmin):
    list_display = ('kodsklada','namesklada','fio')
admin.site.register(Podrazdeleniya, PodrazdeleniyaAdmin)

class TaksirovkaAdmin(admin.ModelAdmin):
    list_display = ('nnakladnoy','kodnaloga','sumnaloga')
admin.site.register(Taksirovka, TaksirovkaAdmin)

class OstatkiAdmin(admin.ModelAdmin):
    list_display = ('articul','srcena','kolvotovarananachalo','kolvoprihod','kolvorashod')
admin.site.register(Ostatki, OstatkiAdmin)
