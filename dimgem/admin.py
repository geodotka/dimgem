from django.contrib import admin
from dimgem.models import Category, Post, Vote, NoteToPost


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date', 'author', 'text', 'dim',
                    'categories', 'old_text')

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Vote)
admin.site.register(NoteToPost)
