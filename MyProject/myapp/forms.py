from django import forms
from django.forms import ModelForm
from myapp.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name' : 'nome',
            'description': 'descricao',
            'price': 'preco',
            'image': 'imagem',
            'stored': 'estoque'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Excel'
                }
            ),
            'descripion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Madeira'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 100.00'
                }
            ),
            'stored': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 5'
                }
            ),
            'image': forms.ClearableFileInput(),
        }

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'
#         labels = {
#             'date' : 'data',
#             'user' : 'usuario',
#         }
#         widgets = {
#             'date': forms.DateInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Ex: 01/01/2024'
#                 }
#             ),
#             'user': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Ex: Raphael'
#                 }
#             )
#         }

# class ItemOrderForm(forms.ModelForm):
#     class Meta:
#         model = ItemOrder
#         fields = '__all__'
#         labels = {
#             'order'   : 'numero pedido',
#             'product' : 'produto',
#             'quantity': 'quantidade'
#         }
#         widgets = {
#             'order': forms.DateInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Ex: 01/01/2024'
#                 }
#             ),
#             'product': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Ex: Raphael'
#                 }
#             ),
#             'quantity': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Ex: Raphael'
#                 }
#             )
#         }