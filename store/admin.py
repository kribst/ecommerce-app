from django.contrib import admin
from .models import Vetement


class VetementAdmin(admin.ModelAdmin):
    list_display = (
        'article', 'quantite', 'prix', 'nouveau_prix', 'type',
        'description_display', 'information_Technique_display', 'publié'
    )

    def description_display(self, obj):
        return (obj.description[:15] + '...') if len(obj.description) > 15 else obj.description

    def information_Technique_display(self, obj):
        return (obj.information_Technique[:15] + '...') if len(
            obj.information_Technique) > 15 else obj.information_Technique

    list_editable = ('quantite', 'prix', 'nouveau_prix', 'type')


admin.site.register(Vetement, VetementAdmin)