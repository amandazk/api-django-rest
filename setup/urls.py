from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matrículas')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view())
]
