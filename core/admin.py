from django.contrib import admin
from core.models import Evento
from core.models import Rodada
from core.models import Dinheiro
from core.models import Aposta,Avaliacao_teste,Online_esta,Localizacao


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','usuario','milhar','rodada')
    list_filter = ('usuario','id','rodada','rodada')




admin.site.register(Evento,EventoAdmin)
admin.site.register(Rodada)
admin.site.register(Dinheiro)
admin.site.register(Aposta)
admin.site.register(Avaliacao_teste)
admin.site.register(Online_esta)
admin.site.register(Localizacao)



# Register your modelpythos here.
