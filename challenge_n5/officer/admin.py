from django.contrib import admin
from officer.models import Officer


@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    '''Admin View for Officer'''

    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

# Register your models here.
