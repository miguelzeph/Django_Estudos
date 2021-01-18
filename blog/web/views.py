from django.shortcuts import render

# Create your views here.
from .models import Post, Contact
def hello_blog(request):

    data = {
        'nome': 'Miguel',
        'lista': [0,1,2,3,4],#        Pode colocar Filtro do que vai aparecer...
        'posts': Post.objects.all() # Post.objects.filter(aprovados_teste=True)
    }

    return render(request, 'index.html',data)


def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html',{'post':post})

def save_form(request):

    #Cria OBjeto no DB
    Contact.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        message = request.POST['message']
    )

    # Cria dicionário
    dados = {
        'name':request.POST['name'],
        'email':request.POST['email'],
        'message':request.POST['message']
        }

    return render(request,'form_ok.html',dados)


