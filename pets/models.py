from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Kind(models.Model):  
    name = models.TextField(max_length=50, unique=True, verbose_name='Наименование')  
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид домашнего животного'
        verbose_name_plural = 'Виды домашнего животного'
        ordering = ['name']
    
    def clean(self, *args, **kwargs):
        if self.name is None:
            raise ValidationError('Не указано наименование.')

        qs = Kind.objects.filter(name=self.name).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Схожий вид уже заведен.')
        return super(PetsKind, self).clean(*args, **kwargs)


class Breed(models.Model):  
    name = models.TextField(max_length=50, unique=True, verbose_name='Наименование')  
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, verbose_name='Порода')
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Порода домашнего животного'
        verbose_name_plural = 'Породы домашнего животного'
        ordering = ['name']


class Pet(models.Model):  
    name = models.TextField(max_length=100, unique=True, verbose_name='Кличка животного')  
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, verbose_name='Вид')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')  
    placementdata = models.DateField(auto_now_add=True, verbose_name='Дата размещения объявления')
    foto = models.ImageField(upload_to='pets', null=True, blank=True, verbose_name='Фото')
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)  
    kind.empty_value_display = 'вид животного не указан'
    breed.empty_value_display = 'порода животного не указана'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'
        ordering = ['name']
