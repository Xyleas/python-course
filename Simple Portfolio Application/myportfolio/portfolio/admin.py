from django.contrib import admin
from . models import PortfolioItem

# Register your models here.
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')