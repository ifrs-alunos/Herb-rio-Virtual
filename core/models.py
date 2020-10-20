from django.db import models
from django.utils.text import slugify

# Create your models here.

def highlight_directory_path(instance, filename):

    # Transforma a string passada como parâmetro em um slug
    folder_name = slugify(instance.title)

    return 'destaques/noticias/{}/{}'.format(folder_name, filename)

class Highlight(models.Model):
    # keyword = models.CharField('Palavra-chave', blank=False, max_length=10, null=True)

    title = models.CharField('Título', blank=False, max_length=50)

    text = models.TextField('Texto', blank=False)

    image = models.ImageField('Imagem', upload_to=highlight_directory_path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Destaque'
        verbose_name_plural = 'Destaques'

def carousel_image_directory_path(instance, filename):
    folder_name = slugify(instance.image)

    return 'destaques/carrossel/{}/{}'.format(folder_name, filename)

class CarouselImage(models.Model):
    image = models.ImageField('Imagem', upload_to=carousel_image_directory_path, blank=False)

    def __str__(self):
        name = slugify(self.image.name)
        return name

    class Meta:
        verbose_name = 'Imagem do Carrossel'
        verbose_name_plural = 'Imagens do Carrossel'