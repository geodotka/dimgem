from django.contrib import admin
from dimgem.models import Category, Post, Vote, NoteToPost


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date', 'author', 'text', 'dim',
                    'categories', 'old_text')


class NoteToPostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'author', 'anon_author', 'text',
                    'submited_date', 'is_accepted', 'accept_date',
                    'accept_superuser')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Vote)
admin.site.register(NoteToPost, NoteToPostAdmin)
