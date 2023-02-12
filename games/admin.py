from django.contrib import admin

from .models import *

class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title', 'photo')
    search_fields = ('title', 'content')
    list_editable = ['is_published']
    list_filter = ['is_published', 'time_create']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name', )
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Games, GamesAdmin)
admin.site.register(Category, CategoryAdmin)
