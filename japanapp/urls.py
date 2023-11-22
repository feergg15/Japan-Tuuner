from django.urls import path
from . import views
from japanapp.views import *
from django.contrib.auth import views as auth_views
from django.urls import include

urlpatterns = [

    path("", Index.as_view(), name="index"),
    path("search/", SearchResultsView.as_view(), name="search_results"),

    path("Coches/", CocheListView.as_view(),name="coche-lista"),
    path("Coches/<int:pk>/", CocheDetailView.as_view(),name="coche-detalles"),
    path("Coches/add/", CocheCreateView.as_view(), name="Coche-add"),
    path("Coches/<int:pk>/delete/", CocheDeleteView.as_view(), name="Coche-delete"),
    path("Coches/<int:pk>/update", CocheUpdateView.as_view(), name="Coche-update"),
    
    
    path("Escapes/", EscapeListView.as_view(),name="escape-lista"),
    path("Escapes/<int:pk>/", EscapeDetailView.as_view(),name="escapes-detalles"),
    path("Escapes/add/", EscapeCreateView.as_view(), name="Escape-add"),
    path("Escapes/<int:pk>/update/", EscapeUpdateView.as_view(), name="Escape-update"),
    path("Escapes/<int:pk>/delete/", EscapeDeleteView.as_view(), name="Escape-delete"),


    path("Volantes/", VolanteListView.as_view(),name="volante-lista"),
    path("Volantes/", VolanteListView.as_view(),name="volante-lista"),
    path("Volantes/<int:pk>/", VolanteDetailView.as_view(),name="volante-detalles"),
    path("Volantes/add/", VolanteCreateView.as_view(), name="Volante-add"),
    path("Volantes/<int:pk>/update/", VolanteUpdateView.as_view(), name="Volante-update"),
    path("Volantes/<int:pk>/delete/", VolanteDeleteView.as_view(), name="Volante-delete"),
    
    
    path("Llantas/", LlantaListView.as_view(),name="llanta-lista"),
    path("Llantas/<int:pk>/", LlantaDetailView.as_view(),name="llanta-detalles"),
    path("Llantas/add/", LlantaCreateView.as_view(), name="Llanta-add"),
    path("Llantas/<int:pk>/update/", LlantaUpdateView.as_view(), name="Llanta-update"),
    path("Llantas/<int:pk>/delete/", LlantaDeleteView.as_view(), name="Llanta-delete"),


    path("Body_Kits/", Body_KitListView.as_view(),name="bk-lista"),
    path("Body_Kits/<int:pk>/", Body_KitDetailView.as_view(),name="bk-detalles"),
    path("Body_Kits/add/", Body_KitCreateView.as_view(), name="bk-add"),
    path("Body_Kits/<int:pk>/update/", Body_KitUpdateView.as_view(), name="bk-update"),
    path("Body_Kits/<int:pk>/delete/", Body_KitDeleteView.as_view(), name="bk-delete"),

    path("Suspension/", SuspensionListView.as_view(),name="suspension-lista"),
    path("Suspension/<int:pk>/", SuspensionDetailView.as_view(),name="suspension-detalles"),
    path("Suspension/add/", SuspensionCreateView.as_view(), name="suspension-add"),
    path("Suspension/<int:pk>/update/", SuspensionUpdateView.as_view(), name="suspension-update"),
    path("Suspension/<int:pk>/delete/", SuspensionDeleteView.as_view(), name="suspension-delete"),

    path("Filtros/", FiltroListView.as_view(),name="Filtro-lista"),
    path("Filtros/<int:pk>/", FiltroDetailView.as_view(),name="Filtro-detalles"),
    path("Filtros/add/", FiltroCreateView.as_view(), name="Filtro-add"),
    path("Filtros/<int:pk>/update/", FiltroUpdateView.as_view(), name="Filtro-update"),
    path("Filtros/<int:pk>/delete/", FiltroDeleteView.as_view(), name="Filtro-delete"),

    path('mi_cuenta/', views.my_account, name='mi_cuenta'),
    
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', register.as_view(), name='register'),
    
    path("Proyecto/", ProyectoListView.as_view(),name="Proyecto-lista"),
    path("Proyecto/<int:pk>/", ProyectoDetailView.as_view(),name="Proyecto-detalles"),
    path("Proyecto/add/", ProyectoCreateView.as_view(), name="Proyecto-add"),


    # path('crear-proyecto/', crear_proyecto, name='crear_proyecto'),
    # path('buscar-coches/<str:marca>/', buscar_coches_por_marca, name='buscar_coches_por_marca'),
]