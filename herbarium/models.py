from django.db import models

'''
#Create your models here.
class Division(models.Model):
    # Cria divisão de plantas: por Dicotiledôneas e Monocotiledôneas

    # Cria uma variável do tipo texto com máximo de 100 caracteres que pode estar vazio
    # name = models.CharField('Nome', blank=True, max_length=100) (TROCAR BLANK = TRUE)
    name = models.CharField('Nome', blank=False, max_length=50)

    # Retorna variável name caso seja dado um print do objeto
    def __str__(self):
        return self.name

    # Configurações do model (Como aparece no admin)
    class Meta:
        verbose_name = 'Divisão'
        verbose_name_plural = 'Divisões'
        ordering = ['name'] #ordena por ordem alfabética
'''

class Family(models.Model):
    # Cria famílias de plantas

    # Cria uma variável do tipo texto com máximo de 100 caracteres
    name = models.CharField('Nome', blank=False, max_length=100)

    # Relação de 1 para muitos entre família e divisão
    # on_delete = se deletar 1 divisão, deleta todas as famílias que são daquela divisão
    # related_name = ObjetivoTipoDivision.families retorna todas as famílias daquela divisao 
    # division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='families')


    # Retorna variável name caso seja dado um print do objeto
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Família'
        verbose_name_plural = 'Famílias'
        ordering = ['name']


class Plant(models.Model):
    # Define o que é uma planta

    #Escolha de família separa por divisão a qual a família pertence.

    # Objetivo: tirar
    '''
    FAMILY_CHOICES = [
        ('Dicotiledôneas' ,
            (
                ('amaranthaceae', 'Amaranthaceae'),
                ('asteraceae', 'Asteraceae'),
                ('brassicaceae', 'Brassicaceae'),
                ('caryophyllaceae', 'Caryophyllaceae'),
                ('cyperaceae', 'Cyperaceae'),
                ('convolvulaceae', 'Convolvulaceae'),
                ('euphobiaceae', 'Euphobiaceae'),
                ('malvaceae', 'Malvaceae'),

            )

        ),

        ('Monocotiledôneas',

            (
                ('plantaginaceae', 'Plantaginaceae'),
                ('poaceae', 'Poaceae'),
                ('polygonaceae', 'Polygonaceae'),
                ('rubiaceae', 'Rubiaceae'),
                ('sapindaceae', 'Sapindaceae'),
                ('solanaceae', 'Solanaceae'),

            )



        )


    ]
    '''

    # Quando plantas forem cadastradas, deverá conter todas as informações a seguir???

    name = models.CharField('Nome', blank=False, max_length=100)
    scientific_name = models.CharField('Nome científico', blank=False, max_length=200)

    # MODIFICAR: relacionar a planta com a sua família (classe Family) e com isso, automaticamente, será relacionada com a Division 
    # family = models.CharField('Família', blank=True, max_length=100, choices=FAMILY_CHOICES)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="plants")

    # Objetivo: tirar
    # division = models.CharField("Divisão", blank=True, editable=False, max_length=100)

    # Torna um conjunto de palavras passíveis para serem usadas como um URL
    # O slug não pode ser repetido, logo unique = True
    slug = models.SlugField('Identificador', blank=False, null=True, unique=True)
    description = models.TextField('Descrição', blank=False)

    # Usado para fazer imagem 3D
    # fyuseimage = models.TextField('ID imagem do Fyuse', blank=False, max_length=1000)

    created_at = models.DateField('Criado em', auto_now_add=True, null=False)
    updated_at = models.DateField('Criado em', auto_now=True, null=False)

    # Objetivo: tirar
    '''
    def save( self, *args, **kw ):
        #Define a divisão baseado na família selecionada
        family = (self.family, self.family.capitalize()) #para que a tupla fique igual a que está no choices
        if family in  self.FAMILY_CHOICES[0][1]:
            self.division = self.FAMILY_CHOICES[0][0]
        elif family in self.FAMILY_CHOICES[1][1]:
            self.division = self.FAMILY_CHOICES[1][0]
        else:
            self.division = 'Não registrado'

        super( Plant, self ).save( *args, **kw )
    '''

    def __str__(self):

        return self.name

    class Meta:
        verbose_name = 'Planta'
        verbose_name_plural = 'Plantas'
        ordering = ['name']


# Função que retorna onde imagens devem ser guardadas
def plant_directory_path(instance, filename):

    return 'images/plantas/{}/{}'.format(instance.plant.name, filename)


#Modelo de foto para que seja possível a planta ter multiplas imagens

class Photo(models.Model):
    # Cria modelo para fotos das plantas

    # Relaciona as fotos com a planta
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name= 'photos')

    # Campo que contém uma imagem e indica a função que retorna onde a imagem deve ser guardada
    image = models.ImageField(upload_to= plant_directory_path)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
