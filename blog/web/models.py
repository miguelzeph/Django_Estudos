from django.db import models


#                Escolher os textos
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    # 2 - jogos, 3 - programacao, 4 - academia - 5 fut
    id_post = models.IntegerField(default = 2)

    def __str__(self):
        return self.name


class Categorias(models.TextChoices):
    DR = 'DR','Doutorado'
    MS = 'MS','Mestrado'
    GD = 'GD','Graduado'
    IC = 'IC','Iniciação Cientifica' 

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length =200)
    content = models.TextField()

    categories = models.CharField(
        max_length=2,
        choices = Categorias.choices,
        default = Categorias.IC
    )

    aprovados_teste = models.BooleanField(default = True)

    imagem = models.ImageField(
        upload_to = 'post',
        null = True,
        blank = True
    )



    # Vai mostrar no Admin por título agora
    def __str__(self):
        return self.title

    def full_name(self): # inventei essa função
        return self.title + self.sub_title
    full_name.admin_order_field = 'title' # Permite fazer o Filtro