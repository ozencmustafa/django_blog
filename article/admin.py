from django.contrib import admin
from .models import Article

# Register your models here.
'''
Normally admin.site.register(Article) command can be used to register but we want to personolize our admin panel.
We are going to use decorators and ModelAdmin class.
'''
# admin.site.register(Article)
'''
We used Meta class to combine the Article class with ArticleAdmin class
'''
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date"]
    list_display_links = ["title", "created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Article
