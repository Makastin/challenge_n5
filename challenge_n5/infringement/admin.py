from django.contrib import admin
from infringement.models import Infringement


@admin.register(Infringement)
class InfringementAdmin(admin.ModelAdmin):
    '''Admin View for Infringement'''

#     list_display = ('',)
#     list_filter = ('',)
#     inlines = [
#         Inline,
#     ]
#     raw_id_fields = ('',)
#     readonly_fields = ('',)
#     search_fields = ('',)
#     date_hierarchy = ''
#     ordering = ('',)

# # Register your models here.
