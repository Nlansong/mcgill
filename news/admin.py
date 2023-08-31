from django.contrib import admin
from .models import Category, PostModel

# Register your models here.
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = PostModel
        
    list_display = [
        'title',
        'author',
        'created_on',
    ]
    
    search_fields = [
        'title',
        'body',
    ]
    
    prepopulated_fields = {
        'slug':('title',)
    }

admin.site.register(PostModel, PostAdmin)
