from django.contrib import admin
from .models import Administrador, Aluno, Professor

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    pass

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    pass

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass
