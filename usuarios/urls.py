from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.usuariolist, name='usuario_list'),
    path('registrarAprendiz/',views.FormularioAprendizView.index, name="registrarAprendiz"),
    path('guardarAprendiz/',views.FormularioAprendizView.procesar_formulario, name="guardarAprendiz"),
    path("editaraprendiz/<int:id_aprendiz>",views.FormularioAprendizView.edit, name="editarAprendiz"),
    path("actualizar_aprendiz/<int:id_aprendiz>",views.FormularioAprendizView.actualizar_aprendiz, name="actualizarAprendiz"),
    path("eliminar_aprendiz/<int:id_aprendiz>",views.FormularioAprendizView.eliminar_aprendiz, name="eliminarAprendiz"),
]


"""
path('', Home.as_view(), name='home')
"""