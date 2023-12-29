from django.views import generic
from postagens.models import Postagem, Categoria

class Home(generic.ListView):
    template_name = 'core/home.html'
    model = Postagem
    context_object_name = 'postagens'
    paginate_by = 5

class Dashboard(generic.TemplateView):
    template_name = "core/dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_categorias'] = Categoria.objects.count()
        context['total_postagens'] = Postagem.objects.count()
        return context
        