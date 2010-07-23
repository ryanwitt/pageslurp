from django.contrib import admin
from models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'user_agent',
        'date_created',
    )
    list_filter = (
        'user_agent',
    )
    search_fields = (
        'url',
        'user_agent',
    )

admin.site.register(Page, PageAdmin)
