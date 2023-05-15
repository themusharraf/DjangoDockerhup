from django import forms
from apps.models import Products, Category, Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
