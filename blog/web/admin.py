from django.contrib import admin

# Register your models here. # REGISTRAR OS MODELS AQUI
from .models import Post, Contact

class PostAdmin(admin.ModelAdmin):
    
    #                  Nomes dados no Model.py
    list_display = ['title','sub_title','full_name','categories','aprovados_teste']
    search_fields = ['title']
    #fields = ('content','sub_title') # posso organiar a ordem do que mostrar

    """
    def get_queryset(self, request):
        #return Post.Objects.all() # PADRÃO vem esse
        
        # filtro do que vai mostrar, exemplo, 2 filtros eu coloquei
        return Post.objects.filter(
            aprovados_teste=True,
            #categories = 'MS' or 'DR'
            )
    """
    
admin.site.register(Post, PostAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email']
    
    


admin.site.register(Contact, ContactAdmin)

