from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length =200)
    content = models.TextField()

    # Vai mostrar no Admin por título agora
    def __str__(self):
        return self.title

    def full_name(self): # inventei essa função
        return self.title + self.sub_title
    full_name.admin_order_field = 'title' # Permite fazer o Filtro