from django.contrib import admin
from . import models
# Register your models here.

#ADMIN INTERFACE ARE ABILITATEA DE A EDITA MODELELE PE ACEEASI PAGINA CA MODELUL PARINTE -> INLINES
#POT EDITA MEMBRII GRUPULUI
class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
