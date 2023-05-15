from django.urls import path
from apps.views import ProView, CatView, UserView, fake_data

urlpatterns = [
    path('', ProView.as_view(), name='pro'),
    path('cat', CatView.as_view(), name='cat'),
    path('user', UserView.as_view(), name='user'),
    path('fakerdata', fake_data, name='faker'),
]
