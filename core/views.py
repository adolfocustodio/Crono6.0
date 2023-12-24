from django.views import generic
from postagens.models import Postagem

class Home(generic.ListView):
    template_name = 'core/home.html'
    model = Postagem
    context_object_name = 'postagens'
