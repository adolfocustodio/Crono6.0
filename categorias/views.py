from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse_lazy

class CategoriaCriar(SuccessMessageMixin, generic.CreateView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')
    success_message = "A categoria foi criada com sucesso."

class CategoriaListar(generic.ListView):
    model = Categoria
    context_object_name = 'categorias'
    paginate_by = 10

class CategoriaEditar(SuccessMessageMixin, generic.UpdateView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')
    success_message = "A categoria foi atualizada com sucesso."

class CategoriaExcluir(SuccessMessageMixin, generic.DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias:categoria_listar')
    success_message = "A categoria foi excluída com sucesso."
