from django.contrib import admin
from django.contrib.admin import ModelAdmin
from photojournal.models import Blog


def change_genre(modeladmin, request, queryset):
    queryset.update(genre='GM')
change_genre.short_description = "Change genre for some posts"

@admin.register(Blog)

class BlogAdmin(ModelAdmin):
    list_display = ('title', 'genre', 'description', 'slug')
    search_field = ('genre', )
    actions = [change_genre]
    prepopulated_fields= {"slug": ("title",)    }



