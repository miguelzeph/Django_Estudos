from django.contrib import admin

# Register your models here. # REGISTRAR OS MODELS AQUI
from .models import Post

class PostAdmin(admin.ModelAdmin):
    
    #                  Nomes dados no Model.py
    list_display = ['title','sub_title','full_name']
    search_fields = ['title']
    fields = ('title','sub_title')

    def __str__(self):
        return self.title
    
admin.site.register(Post, PostAdmin)

