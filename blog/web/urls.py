from django.urls import path

from .views import hello_blog, post_detail, save_form

urlpatterns = [
    path('', hello_blog, name='home'), #      Esse name, é o que você chama no HTML via Jinja2
    path('post/<int:id>', post_detail, name = 'post_detail'),
    path('save-form/',save_form, name = 'save-form')
]
