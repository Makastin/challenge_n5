from django.contrib import admin
from person.models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    '''Admin View for Person'''

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