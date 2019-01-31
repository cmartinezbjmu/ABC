from django.urls import path
from django.conf.urls import url
from . import views

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
    url(r'^login/$', views.login_view, name='login'),
   #path('', listadoEventos, name='index'),
]
