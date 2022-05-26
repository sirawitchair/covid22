from django.contrib import admin

from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

from .models import User, Unit

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'full_name']
    list_display_links = ['short_name']
    search_fields = ('short_name', 'full_name')
    ordering = [ "id",]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'FullName','mobile_phone', 'office_phone','last_login')
    list_display_links = ['FullName']
    list_filter = ( 'unit',)
    ordering = ('-last_login','unit','rank',)
    save_as = True
