from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Type, Animal


class AnimalForm(ModelForm):

    class Meta:
        model = Animal
        fields = ['name', 'poster', 'latin', 'description']
        labels = {'name': 'Animal name'}