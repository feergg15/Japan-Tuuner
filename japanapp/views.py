from django.utils import timezone
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView

from japanapp.models import User,Coche,Escape,Llanta,Volante,Body_Kit,Suspension,Filtro,Proyecto

from .forms import RegisterForm,UserEditForm

class Index(TemplateView):
    template_name = 'index.html'


class CocheListView(ListView):
    model = Coche


class SearchResultsView(ListView):
    model = Coche
    template_name = 'search_results.html'
    def get_queryset(self): 
        query = self.request.GET.get("q")
        object_list = Coche.objects.filter(
            Q(marca__icontains=query) | Q(modelo__icontains=query)
        )
        return object_list

class CocheDetailView(DetailView):

    context_object_name = "Coches"
    queryset = Coche.objects.all()

class CocheCreateView(CreateView):
    model = Coche
    fields="__all__"


class CocheUpdateView(UpdateView):
    model = Coche
    fields = "__all__"



class CocheDeleteView(DeleteView):
    model = Coche
    success_url = reverse_lazy("coche-lista")

class EscapeListView(ListView):
    model = Escape

class EscapeDetailView(DetailView):

    context_object_name = "Escapes"
    queryset = Escape.objects.all()

class EscapeCreateView(CreateView):
    model = Escape
    fields="__all__"


class EscapeUpdateView(UpdateView):
    model = Escape
    fields = "__all__"



class EscapeDeleteView(DeleteView):
    model = Escape
    success_url = reverse_lazy("escape-lista")


class VolanteListView(ListView):
    model = Volante


class VolanteDetailView(DetailView):

    context_object_name = "Volante"
    queryset = Volante.objects.all()

class VolanteCreateView(CreateView):
    model = Volante
    fields="__all__"


class VolanteUpdateView(UpdateView):
    model = Volante
    fields = "__all__"



class VolanteDeleteView(DeleteView):
    model = Volante
    success_url = reverse_lazy("volante-lista")


class LlantaListView(ListView):
    model = Llanta

class LlantaDetailView(DetailView):

    context_object_name = "Llantas"
    queryset = Llanta.objects.all()

class LlantaCreateView(CreateView):
    model = Llanta
    fields="__all__"


class LlantaUpdateView(UpdateView):
    model = Llanta
    fields = "__all__"



class LlantaDeleteView(DeleteView):
    model = Llanta
    success_url = reverse_lazy("llanta-lista")


class Body_KitListView(ListView):
    model = Body_Kit

class Body_KitDetailView(DetailView):

    qcontext_object_name = "Body_Kits"
    queryset = Body_Kit.objects.all()

class Body_KitCreateView(CreateView):
    model = Body_Kit
    fields="__all__"


class Body_KitUpdateView(UpdateView):
    model = Body_Kit
    fields = "__all__"

class Body_KitDeleteView(DeleteView):
    model = Body_Kit
    success_url = reverse_lazy("bk-lista")

class SuspensionListView(ListView):
    model = Suspension

class SuspensionDetailView(DetailView):

    context_object_name = "suspension-detalles"
    queryset = Suspension.objects.all()

class SuspensionCreateView(CreateView):
    model = Suspension
    fields="__all__"


class SuspensionUpdateView(UpdateView):
    model = Filtro
    fields = "__all__"

class SuspensionDeleteView(DeleteView):
    model = Filtro
    success_url = reverse_lazy("suspension-lista")

class FiltroListView(ListView):
    model = Filtro

class FiltroDetailView(DetailView):

    context_object_name = "Filtro-detalles"
    queryset = Filtro.objects.all()

class FiltroCreateView(CreateView):
    model = Filtro
    fields="__all__"


class FiltroUpdateView(UpdateView):
    model = Filtro
    fields = "__all__"

class FiltroDeleteView(DeleteView):
    model = Filtro
    success_url = reverse_lazy("Filtro-lista")


@login_required
def my_account(request):
    user = request.user 

    return render(request, 'mi_cuenta.html', {'user': user})

@login_required
def editar_usuario(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('mi_cuenta')
    else:
        form = UserEditForm(instance=user)
    
    return render(request, 'editar_usuario.html', {'form': form})


class MyView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password-reset.html'  
    success_url = reverse_lazy('password_reset_done')  

    def form_valid(self, form):

        return super().form_valid(form)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al usuario a la página de inicio de sesión después del registro exitoso
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})

class ProyectoCreateView(CreateView):
    model = Proyecto
    fields = ['modelo_coche', 'modelo_escape', 'modelo_llanta', 'modelo_suspes', 'modelo_filtro', 'modelo_volante', 'modelo_bk', 'img']

    success_url = reverse_lazy("Proyecto-lista")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin

class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'proyecto_list.html' 

    def get_queryset(self):
  
        return Proyecto.objects.filter(usuario=self.request.user)
   

class ProyectoDetailView(LoginRequiredMixin,DetailView): 

   context_object_name = "Proyecto-detalles"
   queryset = Proyecto.objects.all()
   def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

def custom_404(request, exception):
    return render(request, '404.html', status=404)

#Formulario secuencial

# def crear_proyecto(request):
#     marcas = Coche.objects.values('marca').distinct().exclude(marca__isnull=True)[:5]
#     return render(request, 'crear_proyecto.html', {'marcas': marcas})

# def buscar_coches_por_marca(request, marca):
#     coches = Coche.objects.filter(marca=marca)
#     return render(request, 'listar_coches.html', {'coches': coches})

# from .forms import MarcaForm

# def crear_proyecto(request):
#     marcas = [
#         {'nombre': 'Nissan', 'imagen': 'nissan.jpg'},
#         {'nombre': 'MAZDA', 'imagen': 'Mazda.png'},
#         {'nombre': 'Honda', 'imagen': 'honda.png'},
#         {'nombre': 'Mitsubishi', 'imagen': 'Mitsubishi.png'},
#         {'nombre': 'Toyota', 'imagen': 'toyota.jpg'},
#     ]

#     if request.method == 'POST':
#         marca_seleccionada = request.POST.get('marca', '')
#         return redirect('buscar_coches_por_marca', marca=marca_seleccionada)

#     return render(request, 'crear_proyecto.html', {'marcas': marcas})