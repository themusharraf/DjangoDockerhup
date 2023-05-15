from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from apps.models import Users, Products, Category
from apps.formas import ProductForm, CategoryForm, UserForm
from django.urls import reverse_lazy
from faker import Faker


#
# class UserView(CreateView):
#     form_class = {
#         'form1': UserForm,
#         'form2': CategoryForm,
#         'form3': ProductForm,
#     }
#     template_name = 'index.html'
#
#     def form_valid(self, form):
#         form_identifier = self.request.POST.get('form_identifier')
#         if form_identifier == 'form1':
#             pass
#         elif form_identifier == 'form2':
#             pass
#         elif form_identifier == 'form3':
#             # Process Form3 data here
#             pass
#         return super().form_valid(form)


class ProView(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'index.html'
    success_url = reverse_lazy('pro')


class CatView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'index.html'
    success_url = reverse_lazy('pro')


class UserView(CreateView):
    model = Users
    form_class = UserForm
    template_name = 'index.html'
    success_url = reverse_lazy('pro')


def fake_data(request):
    fake = Faker()
    objects = (Products(name=fake.name()) for _ in range(100_000))
    Category.objects.bulk_create(objects)
    return redirect('pro')
