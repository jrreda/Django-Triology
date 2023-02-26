from django.contrib import admin
from .models import Article, Comment # new

# Register your models here.
class ComentInline(admin.TabularInline): # new
    model = Comment

class ArticleAdmin(admin.ModelAdmin):    # new
    inlines = [
        ComentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)         # new