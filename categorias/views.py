from django.views import generic
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse_lazy

class CategoriaCriar(generic.CreateView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')

class CategoriaListar(generic.ListView):
    model = Categoria
    context_object_name = 'categorias'
    paginate_by = 10

class CategoriaEditar(generic.UpdateView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')

class CategoriaExcluir(generic.DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')
