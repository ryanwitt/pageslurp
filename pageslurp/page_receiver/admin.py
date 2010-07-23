from django.contrib import admin
from models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'user_agent',
        'page_file',
        'date_created',
    )
    list_filter = (
        'url',
        'user_agent',
    )

admin.site.register(Page, PageAdmin)
