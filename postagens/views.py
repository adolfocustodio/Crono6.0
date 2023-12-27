from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .models import Postagem
from .forms import PostagemForm
from django.urls import reverse_lazy

class PostagemCriar(SuccessMessageMixin, generic.CreateView):
    form_class = PostagemForm
    model = Postagem
    success_url = reverse_lazy('postagens:postagem_listar')
    success_message = "A postagem foi criada com sucesso."

class PostagemListar(generic.ListView):
    model = Postagem
    context_object_name = 'postagens'
    paginate_by = 10

class PostagemEditar(SuccessMessageMixin, generic.UpdateView):
    form_class = PostagemForm
    model = Postagem
    success_url = reverse_lazy('postagens:postagem_listar')
    success_message = "A postagem foi atualizada com sucesso."

class PostagemExcluir(SuccessMessageMixin, generic.DeleteView):
    model = Postagem
    success_url = reverse_lazy('postagens:postagem_listar')
    success_message = "A postagem foi excluída com sucesso."
