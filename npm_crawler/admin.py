from django.contrib import admin

from npm_crawler.models import LastNews


@admin.register(LastNews)
class LastNewsAdmin(admin.ModelAdmin):
    list_display = ["title", "sumamry", "date_published"]
    list_filter = ["date_published", "title"]
    ordering = ["-id"]
    list_per_page = 10
    search_fields = ["title"]
