from django.contrib import admin
from .models import Kind, Breed, Pet

# Register your models here.
@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment')
    fields = ('name', 'comment')


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'comment')
    fields = ('name', 'kind', 'comment')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'breed', 'description', 'placementdata', 'foto', 'comment')
    fields = ('name', 'kind', 'breed', 'description', 'foto', 'comment')
