from django import forms
from django.db import models
from django.forms import fields
from food.models import Item 

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
