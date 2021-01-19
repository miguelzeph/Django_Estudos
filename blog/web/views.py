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
    print(Contact.objects.all())
    post = Post.objects.get(id=id)

    # 2 - jogos, 3 - programacao, 4 - academia - 5 fut
    contacts = Contact.objects.filter(id_post = id)
    return render(request, 'post_detail.html',{'post':post,'contacts':contacts})

def save_form(request, id):

    #Cria OBjeto no DB
    Contact.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        message = request.POST['message'],
        id_post = id,
    )

    # Cria dicionário
    dados = {
        'name':request.POST['name'],
        'email':request.POST['email'],
        'message':request.POST['message']
        }

    return render(request,'form_ok.html',dados)


