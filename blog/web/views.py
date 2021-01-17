from django.shortcuts import render

# Create your views here.
from .models import Post
def hello_blog(request):

    data = {
        'nome': 'Miguel',
        'lista': [0,1,2,3,4],
        'posts': Post.objects.all()
    }

    return render(request, 'index.html',data)

