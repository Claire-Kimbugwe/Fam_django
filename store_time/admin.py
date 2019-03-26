from django.contrib import admin
from store_time.models import Family

class FamilyAdmin(admin.ModelAdmin):
    model = Family
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Family, FamilyAdmin)