from django.contrib import admin
from .models import Story
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.