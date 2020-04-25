from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView, ListView
from aplicacion.models import City, Person, Book
#class index(TemplateView):
#    template_name = 'index.html'

class listadoBook_all(ListView):
    model = Book
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all().values('titulo', 'author__nombres', 'author__city__nombre')
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['Books'] = self.get_queryset()
        return contexto
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,self.get_context_data())
        
        



''' 
# Hits the database with joins to the author and hometown tables.
b = Book.objects.select_related('author__hometown').get(id=4)
p = b.author         # Doesn't hit the database.
c = p.hometown       # Doesn't hit the database.

# Without select_related()...
b = Book.objects.get(id=4)  # Hits the database.
p = b.author         # Hits the database.
c = p.hometown       # Hits the database. 
'''