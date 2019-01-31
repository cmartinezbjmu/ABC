from django.urls import path
from django.conf.urls import url
from . import views
from eventos.views import EventoCreate, login_view, EventoListView

app_name = 'eventos'

#from SGRD.views.recurso import RecursoCreate, RecursoListView,  RecursoDetailView, recursoBusqueda
#from eventos.views import listadoEventos

#from SGRD.views.archivo import ArchivoCreate
#from SGRD.views.clip import archivoClips, ClipCreate, ClipDelete
#from SGRD.views.planProduccion import crearPlanProduccion, EditarPlanProduccion, delete_plan, createEntradaPlan, editarEntradaPlan, verPlanProduccion, exportarPlanProduccion, delete_entrada
#from SGRD.views.descargarArchivo import planear_descarga, editar_plan_descarga, check_for_downloads
#from SGRD.views.etiqueta import manage_tags, delete_tag, remove_tag, add_tag, remove_tag_clip, add_tag_clip
#from SGRD.views.tipo import crear_tipo


urlpatterns = [
    path('', EventoListView.as_view(), name='index'),
    path('crear-evento/', EventoCreate.as_view(), name='create-evento'),
    path('login/', login_view, name='login'),
]
