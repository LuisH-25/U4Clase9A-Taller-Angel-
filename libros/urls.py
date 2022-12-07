from django.urls import path

#importar la vista basada en clase
from .views import BookList

urlpatterns = [
    path('/', BookList.as_view(), name='libros'),
]
