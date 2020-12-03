import datetime
import io
import urllib,base64
from random import randint
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from datetime import datetime, timezone, timedelta
from math import cos, asin, sqrt
import time
import matplotlib.pyplot as plt
from django.http import HttpResponse

from django.shortcuts import render

import io
import urllib, base64

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect
import time
from datetime import date


from core.models import Evento, Rodada, Dinheiro,Avaliacao_teste,Online_esta,Localizacao

from django.http import HttpResponse

'''
def some_view(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse('application/pdf')
    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = canvas.Canvas(response)

    # Desenhe coisas no PDF. Aqui é onde a geração do PDF acontece.
    # Veja a documentação do ReportLab para a lista completa de
    # funcionalidades.
    rodada2 = Rodada.objects.all()
    evento3 = []

    variavel1 = 0
    variavel6 = 0
    for aleatorio9 in rodada2:
        variavel6 = variavel6 + 1
        print(variavel6)
    while variavel1 < variavel6:
        print("valor de variavel {}".format(variavel1))

        print("o valor de variavel3 {}".format(variavel6))

        if variavel1 + 1 == variavel6:
            rodada = float(Rodada.get_rodada(rodada2[variavel1])) + 1
            print(rodada)
        if variavel1 + 1 != variavel6:
            rodada = 0
            print(rodada)

        variavel1 = variavel1 + 1
    

    evento2 = Evento.objects.all ()

    variavel1 = 0
    variavel6 = 0
    for aleatorio5 in evento2:
        variavel6 = variavel6 + 1
        print ( variavel6 )
    validar = 0
    while variavel1 < variavel6:

        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )
        if request.user == Evento.get_usuario ( evento2[variavel1] ) and rodada == Evento.get_rodada (
                evento2[variavel1] ):

            milhar = float ( Evento.get_milhar ( evento2[variavel1] ) )
            aposta = float ( Evento.get_valor ( evento2[variavel1] ) )

            evento3.append ( "Esta é a milhar: " + str ( milhar ) )
            evento3.append ( "Está é a aposta: " + str ( aposta ) + " da milhar:" + str ( milhar ) )
            pule = float ( Evento.get_pule ( evento2[variavel1] ) )
            validar = 1

        variavel1 = variavel1 + 1
    if validar == 0:
        milhar = 0
        aposta = 0
        pule = 0

    evento3.append ( "A rodada é a: " + str ( rodada ) )
    evento3.append ( "O pule é: " + str ( pule ) )

    evento3 = {'eventos': evento3}
    
    try:
        evento = Evento.objects.filter(rodada=rodada)
    except:
        evento = "Você não jogou nessa rodada"

    try:
        pule = Evento.get_pule(evento[0])
    except:
        pule = "Você não jogou nessa rodada"

    dados = {'eventos': evento, 'pule': pule}
    p.drawString(100, 100, str(dados))

    # Feche o objeto PDF, e está feito.
    p.showPage()
    p.save()
    return response
'''

# Create your views here.

def funcao_ver_dinheiro(usuario):
    dinheiro2 = Dinheiro.objects.all()
    validar = 0

    data_hora = date.today()
    print(data_hora)
    variavel1 = 0
    variavel6 = 0

    for aleatorio5 in dinheiro2:
        variavel6 = variavel6 + 1
        print(variavel6)
    while variavel1 < variavel6:
        print("valor de variavel {}".format(variavel1))

        print("o valor de variavel3 {}".format(variavel6))

        if Dinheiro.get_usuario(dinheiro2[variavel1]) == usuario:
            dinheiro5 = float(Dinheiro.get_valor(dinheiro2[variavel1]))
            validar = 1

        variavel1 = variavel1 + 1
    if validar == 0:
        dinheiro5 = 600
    return dinheiro5
#função para criar ou diferenciar a ultima data que o usuario entrou, sendo necessária para fazer um chat ou algo do tipo
def funcao_para_dar_resultado(usuario):
    evento = Rodada.objects.all()
    valor = 0
    try:
        for eventinhos in evento:
            if eventinhos.id > valor:
                valor = eventinhos.id

    except:
        Evento.objects.create(milhar=100,
                              rodada=0,
                              valor=0,
                              usuario="",
                              conferir=0,
                              pule=0)
        evento = Rodada.objects.all()

        for eventinhos in evento:
            if eventinhos.id > valor:
                valor = eventinhos.id
                evento3 = eventinhos

    variavel1 = 0
    online = ""
    vetor_que_vai = []
    contador = 0
    data_dia1 = ""
    data_mes1 = ""
    data_ano1 = ""
    data_dia2 = ""
    data_mes2 = ""
    data_ano2 = ""
    if online == "":
        variavel1 = variavel1 + 1


        vetor2 = []
        try:



            for teste2 in eventinhos.data:
                contador = contador + 1
                #data
                if contador == 1:
                    data_dia1 = data_dia1 + teste2
                if contador == 2:
                    data_dia1 = data_dia1 + teste2
                #mes
                if contador == 4:
                    data_mes1 = data_mes1+ teste2
                if contador == 5:
                    data_mes1 = data_mes1 + teste2

                if contador == 7:
                    data_ano1 = data_ano1 + teste2
                if contador == 8:
                    data_ano1 = data_ano1 + teste2
                if contador == 9:
                    data_ano1 = data_ano1 + teste2
                if contador == 10:
                    data_ano1 = data_ano1 + teste2
                vetor2.append(teste2)

        except:
            eventinhos = "13/21/2020 15:20"
            for teste2 in eventinhos:

                vetor2.append(teste2)


        data_e_hora_atuais = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
        data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y")
        print(data_e_hora_sao_paulo_em_texto)
        contador = 0
        a = 0
        tempo = 6
        contador = 0
        for variavel_in_data_e_hora_atual in data_e_hora_sao_paulo_em_texto:
            contador = contador + 1
            # data
            if contador == 1:
                data_dia2 = data_dia2 + variavel_in_data_e_hora_atual
            if contador == 2:
                data_dia2 = data_dia2 + variavel_in_data_e_hora_atual
            # mes
            if contador == 4:
                data_mes2 = data_mes2 + variavel_in_data_e_hora_atual
            if contador == 5:
                data_mes2 = data_mes2 + variavel_in_data_e_hora_atual

            if contador == 7:
                data_ano2 = data_ano2 + variavel_in_data_e_hora_atual
            if contador == 8:
                data_ano2 = data_ano2 + variavel_in_data_e_hora_atual
            if contador == 9:
                data_ano2 = data_ano2 + variavel_in_data_e_hora_atual
            if contador == 10:
                data_ano2 = data_ano2 + variavel_in_data_e_hora_atual


        data1 = str(data_ano1) + "-" + str(data_mes1) + "-" + str(data_dia1)
        data2 = str(data_ano2) + "-" + str(data_mes2) + "-" + str(data_dia2)
        d1 = datetime.strptime(data1, '%Y-%m-%d')
        d2 = datetime.strptime(data2, '%Y-%m-%d')
        quantidade_dias = abs((d2 - d1).days)
        print("quantida de dias" + str(quantidade_dias))
        d = date(int(data_ano1), int(data_mes1), int(data_dia1))

        if  quantidade_dias > 0:
            sopranaoidentar = 0
            contar = 0
            for quantidade_dias_variavel in range(quantidade_dias):
                contar = contar + 1
                if sopranaoidentar == 0:

                            a = 3600 * 12

                            primeiro_lugar = randint(1, 9999)
                            segundo_lugar = randint(1, 9999)
                            terceiro_lugar = randint(1, 9999)
                            quarto_lugar = randint(1, 9999)
                            quinto_lugar = randint(1, 9999)

                            rodada = Rodada.objects.all()
                            dados5 = {'rodada': rodada}
                            print(rodada)

                            variavel1 = 0
                            variavel6 = 0
                            for aleatorio9 in rodada:
                                variavel6 = variavel6 + 1
                                print(variavel6)

                            if variavel6 == 0:
                                data_que_vai = d + timedelta(days=int(contar))
                                print("sou eu aqui data que vai")
                                print(data_que_vai)
                                data_que_vai = data_que_vai.strftime("%d/%m/%Y")

                                Rodada.objects.create(
                                    rodada=1,
                                    primeira_milhar=primeiro_lugar,
                                    segunda_milhar=segundo_lugar,
                                    terceira_milhar=terceiro_lugar,
                                    quarta_milhar=quarto_lugar,
                                    quinta_milhar=quinto_lugar,
                                    data=data_que_vai

                                )
                            else:
                                while variavel1 < variavel6:
                                    print("valor de variavel {}".format(variavel1))

                                    print("o valor de variavel3 {}".format(variavel6))

                                    if variavel1 + 1 == variavel6:
                                        rodada = float(Rodada.get_rodada(rodada[variavel1]))
                                        print(rodada)

                                    variavel1 = variavel1 + 1
                                variavel1 = 0
                                variavel6 = 0
                                rodada2 = Rodada.objects.all()
                                dados5 = {'rodada': rodada2}
                                for aleatorio9 in rodada2:
                                    variavel6 = variavel6 + 1
                                    print(variavel6)
                                while variavel1 < variavel6:
                                    print("valor de variavel {}".format(variavel1))

                                    print("o valor de variavel3 {}".format(variavel6))

                                    if variavel1 + 1 == variavel6:
                                        rodada = float(Rodada.get_rodada(rodada2[variavel1]))
                                        primeira_milhar = float(Rodada.get_primeira_milhar(rodada2[variavel1]))

                                        segunda_milhar = float(Rodada.get_segunda_milhar(rodada2[variavel1]))
                                        terceira_milhar = float(Rodada.get_terceira_milhar(rodada2[variavel1]))
                                        quarta_milhar = float(Rodada.get_quarta_milhar(rodada2[variavel1]))
                                        quinta_milhar = float(Rodada.get_quinta_milhar(rodada2[variavel1]))
                                        print(rodada)

                                    variavel1 = variavel1 + 1
                                print(rodada)
                                print(primeira_milhar)
                                print(primeira_milhar == -1)
                                print(rodada == 1)
                                if rodada == 1 and primeira_milhar == -1:
                                    ultimo_id = Rodada.objects.get(rodada=rodada).id
                                    rodada_id = Rodada.objects.get(id=ultimo_id)
                                    print(ultimo_id)
                                    print(rodada_id)
                                    rodada_id.primeira_milhar = primeiro_lugar
                                    rodada_id.segunda_milhar = segundo_lugar
                                    rodada_id.terceira_milhar = terceiro_lugar
                                    rodada_id.quarta_milhar = quarto_lugar
                                    rodada_id.quinta_milhar = quinto_lugar
                                    rodada_id.data = data_e_hora_sao_paulo_em_texto
                                    rodada_id.save()


                                else:
                                    data_que_vai = d + timedelta(days=int(contar))
                                    print("sou eu aqui data que vai")
                                    print(data_que_vai)
                                    data_que_vai = data_que_vai.strftime("%d/%m/%Y")
                                    Rodada.objects.create(
                                        rodada=rodada + 1,
                                        primeira_milhar=primeiro_lugar,
                                        segunda_milhar=segundo_lugar,
                                        terceira_milhar=terceiro_lugar,
                                        quarta_milhar=quarto_lugar,
                                        quinta_milhar=quinto_lugar,
                                        data=data_que_vai

                                    )
            print("data e ano")
            print(data_ano1)
            print(data_dia1)
            print(data_mes1)
            print(data_ano2)
            print(data_dia2)
            print(data_mes2)

            contador = contador + 1


def ver_se_esta_online(usuario):
    try:
        ver_data = Online_esta.objects.get(usuario=usuario)
        print(ver_data.data)
        data_e_hora_atuais = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
        data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")
        ver_data.data = data_e_hora_sao_paulo_em_texto
        ver_data.save()
    except:

        data_e_hora_atuais = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
        data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")

        a = Online_esta.objects.create(usuario=usuario,
                                       data=data_e_hora_sao_paulo_em_texto
                                       )


def quantidade_de_rodadas(aindanaosei):
    rodada = Rodada.objects.all()

    variavel6 = 0
    variavel1 = 0
    for aleatorio9 in rodada:
        variavel6 = variavel6 + 1

    while variavel1 < variavel6:
        variavel1 = variavel1 + 1
    rodadas = variavel1
    return rodadas

def pegar_ultimo_valor_jogado(usuario):
    evento = Evento.objects.all()

    contar_se_tem_pule = 0
    variavel1 = 0
    variavel6 = 0
    for aleatorio9 in evento:
        variavel6 = variavel6 + 1

    while variavel1 < variavel6:

        if usuario == Evento.get_usuario(evento[variavel1]):
            aposta = float(Evento.get_valor(evento[variavel1]))
            contar_se_tem_pule = 1
        if contar_se_tem_pule == 0:
            if variavel1 + 1 == variavel6:
                aposta = int(Evento.get_valor(evento[variavel1])) + 1

        variavel1 = variavel1 + 1
    if variavel6 == 0:
        aposta = 1

    return aposta
# Create your views here
def login_user(request):
    return render(request,'login.html')
def logout_user(request):
    logout(request)
    return redirect('/')
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário ou senha invalido")


    return  redirect('/')
@login_required(login_url='/login/')
def resultado(request):
    while True:
        print ( "passou 3 minutos" )

        usuario = request.user
        ver_se_esta_online(usuario)
        #essa variavel faz aparecer o botão ou não aparecer o botão de conferir no resultado.html
        validar = 0
        rodada = Rodada.objects.all()
        rodadas = quantidade_de_rodadas(validar)
        dados = {'resultados':rodada,'validar':validar,'rodadas':rodadas}


        return render(request,'resultado.html',dados)
        time.sleep(180)
@login_required(login_url='/login/')
def jogar(request):
    while True:
        print ( "passou 3 minutos" )
        usuario = request.user
        ver_se_esta_online(usuario)
        aposta = pegar_ultimo_valor_jogado(usuario)

        dados2 = {'valor': aposta}

        return render(request,'jogar.html',dados2)
        time.sleep(180)


@login_required(login_url='/login/')
def inicio(request):
    while True:
        print ( "passou 3 minutos" )
        usuario = request.user
        ver_se_esta_online(usuario)
        funcao_para_dar_resultado(usuario)


        dinheiro = funcao_ver_dinheiro(usuario)
        dinheiro3 = []
        dinheiro3.append ( str ( dinheiro ) )
        dinheiro3 = {'dinheiros': dinheiro3}

        return render(request,'inicio.html',dinheiro3)
        time.sleep ( 180 )  # A cada hora ele executa o print

@login_required ( login_url = '/login/' )
def jogar_valor(request):

    if request.POST:
        evento = Evento.objects.all()
        contar_se_tem_pule = 0
        dados5 = {'evento': evento}
        milhar = 0

        variavel1 = 0
        variavel6 = 0
        for aleatorio9 in evento:
            variavel6 = variavel6 + 1

        while variavel1 < variavel6:

            if request.user == Evento.get_usuario(evento[variavel1]):

                pule = float ( Evento.get_pule ( evento[variavel1] ) )
                rodada_teste = float(Evento.get_rodada(evento[variavel1]))
                contar_se_tem_pule = 1
            if contar_se_tem_pule == 0:
                if variavel1 + 1 == variavel6:
                    pule = int(Evento.get_pule(evento[variavel1]))




            variavel1 = variavel1 + 1
        if variavel6 == 0:
            pule = 1

        milhar = request.POST.get('milhar')
        try:
            milhar = int(milhar)

        except ValueError:
            return HttpResponse ( '<h1> Milhar tem que ser inteiro e não texto <h1>' )

        aposta = request.POST.get('aposta')
        aposta = str(aposta).replace("[","")
        aposta = str(aposta).replace("]","")
        aposta = str ( aposta ).replace ( ",", "." )

        try:
            aposta =float( aposta )

        except ValueError:
            return HttpResponse ( '<h1> Aposta tem que ser numero e não texto <h1>' )
        print(aposta)
        dinheiro2 = Dinheiro.objects.all ()
        dados5 = {'dinheiro': dinheiro2}

        variavel1 = 0
        variavel6 = 0
        for aleatorio5 in dinheiro2:
            variavel6 = variavel6 + 1
            print ( variavel6 )
        while variavel1 < variavel6:
            print ( "valor de variavel {}".format ( variavel1 ) )

            print ( "o valor de variavel3 {}".format ( variavel6 ) )

            if variavel1 + 1 == variavel6:
                dinheiro2 = float ( Dinheiro.get_valor ( dinheiro2[variavel1] ) )

            variavel1 = variavel1 + 1
        usuario = request.user
        try:
            ultimo_id2 = Dinheiro.objects.get ( usuario = usuario ).id

            dinheiro_id = Dinheiro.objects.get ( id = ultimo_id2 )
            dinheiro_id = dinheiro2 - float ( aposta )
            if dinheiro_id < 0:
                print ( "caiu aqui" )
                return HttpResponse ( '<h1> Seu dinheiro não pode ser negativo <h1>' )
        except:
            print("falhou")



        if float (milhar) > 9999:
            return HttpResponse ( '<h1> Hey, não exagera. O máximo é 9999 <h1>' )

        if float(milhar) > 0 and float(aposta) > 0 :


            usuario = request.user
            teste = 0

            resultado  = Rodada.objects.all ()
            dados2 = {'resultado': resultado}

            variavel = 0
            variavel3 = 0
            for aleatorio2 in resultado:
                variavel3 = variavel3 + 1
                print ( variavel3 )
            while variavel < variavel3:
                print ( "valor de variavel {}".format ( variavel ) )
                print ( "valor de teste {}".format ( teste ) )
                print ( "o valor de variavel3 {}".format ( variavel3 ) )

                if variavel + 1 == variavel3:
                    a = int ( Rodada.get_primeira_milhar ( resultado[variavel] ) )




                variavel = variavel + 1
            print(milhar)
            print(aposta)
            print(pule)

            tem = Dinheiro.objects.all ()
            dados2 = {'resultado': tem}
            validando = 0

            variavel = 0
            variavel3 = 0
            for aleatorio20 in tem:
                variavel3 = variavel3 + 1
                print ( variavel3 )
            while variavel < variavel3:
                if usuario  == Dinheiro.get_usuario(tem[variavel]):
                    validando = 1

                variavel = variavel + 1
            print(validando)
            print(pule)
            print(variavel3)

            if variavel3 == 0 or validando == 0:
                quantidade = 0
                cheio = 5000
                if variavel3 ==0:

                    Rodada.objects.create ( rodada = 1,
                                           primeira_milhar = -1,
                                           segunda_milhar = 0,
                                           terceira_milhar = 0,
                                           quarta_milhar = 0,
                                            quinta_milhar = 0,
                                           )

                    Evento.objects.create(
                            milhar = milhar,
                            rodada = 1,
                            valor = aposta,
                            usuario = usuario,
                            conferir = 0,
                            conferir2 = 0,
                            conferir3 = 0,
                            conferir4 = 0,
                            conferir5 = 0,
                            pule = pule,


                        )
                    Dinheiro.objects.create(
                        usuario = usuario,
                        valor = 600 - float(aposta),
                    )
                else:
                    try:
                        rodada5 = Rodada.objects.all ()
                        dados5 = {'rodada': rodada5}

                        variavel1 = 0
                        variavel6 = 0
                        print ( rodada5 )

                        for aleatorio9 in rodada5:
                            variavel6 = variavel6 + 1
                            print ( variavel6 )
                            print ( "safawq" )
                        while variavel1 < variavel6:
                            print ( "valor de variavel1 {}".format ( variavel1 ) )

                            print ( "o valor de variavel6 {}".format ( variavel6 ) )

                            if variavel1 + 1 == variavel6:
                                rodada = float ( Rodada.get_rodada ( rodada5[variavel1] ) )
                                print ( "aqui está a rodada:" + str ( rodada ) )

                            variavel1 = variavel1 + 1
                    except:
                        rodada = 1
                    Evento.objects.create (
                        milhar = milhar,
                        rodada = rodada + 1,
                        valor = aposta,
                        usuario = usuario,
                        conferir = 0,
                        conferir2 = 0,
                        conferir3 = 0,
                        conferir4 = 0,
                        conferir5 = 0,
                        pule = pule,

                    )
                    Dinheiro.objects.create (
                        usuario = usuario,
                        valor = 600 - float ( aposta ),
                    )

            else:
                rodada5 = Rodada.objects.all ()
                dados5 = {'rodada': rodada5}

                variavel1 = 0
                variavel6 = 0
                print(rodada5)

                for aleatorio9 in rodada5:
                    variavel6 = variavel6 + 1
                    print ( variavel6 )
                    print("safawq")
                while variavel1 < variavel6:
                    print ( "valor de variavel1 {}".format ( variavel1 ) )

                    print ( "o valor de variavel6 {}".format ( variavel6 ) )

                    if variavel1 + 1 == variavel6:
                        rodada = float ( Rodada.get_rodada ( rodada5[variavel1 ] ) )
                        print ( "aqui está a rodada:" + str(rodada) )

                    variavel1 = variavel1 + 1
                teste1213 = 5
                if rodada + 1 != rodada_teste:
                    pule = pule + 1

                try:

                    ultimo_id4 = Evento.objects.get ( usuario = usuario,
                                                      milhar = milhar,
                                                      rodada = rodada + 1).id

                    evento_id = Evento.objects.get ( id = ultimo_id4 )
                    print("vamos lá")
                    evento_id.valor = float(aposta) + float(evento_id.valor)
                    print("estou aqui")
                    evento_id.save ()

                    dinheiro2 = Dinheiro.objects.all ()
                    dados5 = {'dinheiro': dinheiro2}

                    variavel1 = 0
                    variavel6 = 0
                    for aleatorio5 in dinheiro2:
                        variavel6 = variavel6 + 1
                        print ( variavel6 )
                    while variavel1 < variavel6:
                        print ( "valor de variavel {}".format ( variavel1 ) )

                        print ( "o valor de variavel3 {}".format ( variavel6 ) )

                        if variavel1 + 1 == variavel6:
                            dinheiro2 = float ( Dinheiro.get_valor ( dinheiro2[variavel1] ) )

                        variavel1 = variavel1 + 1
                    ultimo_id2 = Dinheiro.objects.get ( usuario = usuario ).id

                    dinheiro_id = Dinheiro.objects.get ( id = ultimo_id2 )
                    dinheiro_id.valor = dinheiro2 - float ( aposta )
                    dinheiro_id.save ()
                except:


                    Evento.objects.create(
                        milhar = milhar,
                        rodada = rodada + 1,
                        valor = aposta,
                        usuario = usuario,
                        conferir = 0,
                        conferir2 = 0,
                        conferir3 = 0,
                        conferir4 = 0,
                        conferir5 = 0,
                        pule = pule,
                    )
                    dinheiro2 = Dinheiro.objects.all ()
                    dados5 = {'dinheiro': dinheiro2}

                    variavel1 = 0
                    variavel6 = 0
                    for aleatorio5 in dinheiro2:
                        variavel6 = variavel6 + 1
                        print ( variavel6 )
                    while variavel1 < variavel6:
                        print ( "valor de variavel {}".format ( variavel1 ) )

                        print ( "o valor de variavel3 {}".format ( variavel6 ) )

                        if variavel1 + 1 == variavel6:
                            dinheiro2 = float ( Dinheiro.get_valor ( dinheiro2[variavel1] ) )


                        variavel1 = variavel1 + 1
                    ultimo_id2 = Dinheiro.objects.get ( usuario = usuario ).id

                    dinheiro_id = Dinheiro.objects.get ( id = ultimo_id2 )
                    dinheiro_id.valor = dinheiro2 - float(aposta)
                    dinheiro_id.save ()




            return redirect('/inicio/jogar/')
        if float ( milhar ) <= 0:
            return HttpResponse ( '<h1> A milhar tem que ser maior que 0, clique na seta para voltar <h1>' )

        if float ( aposta ) <= 0:

            return HttpResponse('<h1> A aposta tem que ser maior que 0, clique na seta para voltar <h1>')
@login_required(login_url='/login/')
def jogadas(request):
    while True:
        print ( "passou 3 minutos" )
        usuario = request.user
        ver_se_esta_online(usuario)
        pule = 0
        valor = 0
        rodada_que_vai = 0
        rodada = 0


        evento = Evento.objects.filter (usuario = usuario)
        dados = {'eventos':evento}
        variavel6 = 0
        variavel1 = 0
        vetor = []
        for aleatorio9 in evento:
            variavel6 = variavel6 + 1

        while variavel1 < variavel6:
            print("aqui3")
            print(Evento.get_pule(evento[variavel1]))
            if variavel1 == 0:
                print("variavel1 = 0")
                pule = int(Evento.get_pule(evento[variavel1]))
                rodada = int(Evento.get_rodada(evento[variavel1]))

                vetor.append(Evento.get_milhar(evento[variavel1]))
                print(Evento.get_milhar(evento[variavel1]))
                valor = float(Evento.get_valor(evento[variavel1]))
            else:
                print("variavel1 != 0")

                if pule == int(Evento.get_pule(evento[variavel1])):
                    pule = int(Evento.get_pule(evento[variavel1]))
                    rodada = int(Evento.get_rodada(evento[variavel1]))


                    valor = valor + float(Evento.get_valor(evento[variavel1]))
                    vetor.append(Evento.get_milhar(evento[variavel1]))
                    rodada_que_vai = float(Evento.get_rodada(evento[variavel1]))
                else:
                    print("pule != pule")
                    vetor.append("Até agora no pule " + str(pule) + " você gastou apenas " + str(
                        valor) + " Reais na rodada " + str(rodada))

                    pule = int(Evento.get_pule(evento[variavel1]))


                    vetor.append(Evento.get_milhar(evento[variavel1]))
                    print(Evento.get_pule(evento[variavel1]))
                    valor = float(Evento.get_valor(evento[variavel1]))
                    rodada_que_vai = float(Evento.get_rodada(evento[variavel1]))

            variavel1 = variavel1 + 1


        vetor.append("Até agora no pule " + str(pule) + " você gastou apenas " + str(valor) + " Reais na rodada " + str(rodada) )

        dados = {'eventos':evento, 'teste':vetor}




        return render(request,'jogadas.html',dados)
        time.sleep(180)

def girar(request):
        if not request.user.has_perm('poll.change_poll'):
            return HttpResponseForbidden('Nope!')
        sopranaoidentar = 0
        if sopranaoidentar==0:


                    a = 3600*12

                    primeiro_lugar = randint(1,9999)
                    segundo_lugar = randint(1,9999)
                    terceiro_lugar = randint(1,9999)
                    quarto_lugar = randint(1,9999)
                    quinto_lugar = randint(1,9999)

                    rodada = Rodada.objects.all ()
                    dados5 = {'rodada': rodada}



                    variavel1 = 0
                    variavel6 = 0
                    for aleatorio9 in rodada:
                        variavel6 = variavel6 + 1
                        print ( variavel6 )


                    if variavel6 == 0 :
                        Rodada.objects.create (
                            rodada = 1,
                            primeira_milhar = primeiro_lugar,
                            segunda_milhar = segundo_lugar,
                            terceira_milhar = terceiro_lugar,
                            quarta_milhar = quarto_lugar,
                            quinta_milhar = quinto_lugar,

                        )
                    else:
                        while variavel1 < variavel6:
                            print ( "valor de variavel {}".format ( variavel1 ) )

                            print ( "o valor de variavel3 {}".format ( variavel6 ) )

                            if variavel1 + 1 == variavel6:
                                rodada = float ( Rodada.get_rodada ( rodada[variavel1] ) )
                                print ( rodada )

                            variavel1 = variavel1 + 1
                        variavel1 = 0
                        variavel6 = 0
                        rodada2 = Rodada.objects.all ()
                        dados5 = {'rodada': rodada2}
                        for aleatorio9 in rodada2:
                            variavel6 = variavel6 + 1
                            print ( variavel6 )
                        while variavel1 < variavel6:
                            print ( "valor de variavel {}".format ( variavel1 ) )

                            print ( "o valor de variavel3 {}".format ( variavel6 ) )

                            if variavel1 + 1 == variavel6:
                                rodada = float ( Rodada.get_rodada ( rodada2[variavel1] ) )
                                primeira_milhar = float ( Rodada.get_primeira_milhar ( rodada2[variavel1] ) )

                                segunda_milhar = float ( Rodada.get_segunda_milhar ( rodada2[variavel1] ) )
                                terceira_milhar = float ( Rodada.get_terceira_milhar ( rodada2[variavel1] ) )
                                quarta_milhar = float ( Rodada.get_quarta_milhar ( rodada2[variavel1] ) )
                                quinta_milhar = float ( Rodada.get_quinta_milhar ( rodada2[variavel1] ) )
                                print ( rodada )

                            variavel1 = variavel1 + 1
                        print(rodada)
                        print(primeira_milhar)
                        print(primeira_milhar == -1)
                        print(rodada == 1)
                        if rodada == 1 and primeira_milhar == -1:
                            ultimo_id = Rodada.objects.get ( rodada = rodada ).id
                            rodada_id = Rodada.objects.get(id = ultimo_id)
                            print(ultimo_id)
                            print(rodada_id)
                            rodada_id.primeira_milhar = primeiro_lugar
                            rodada_id.segunda_milhar = segundo_lugar
                            rodada_id.terceira_milhar = terceiro_lugar
                            rodada_id.quarta_milhar = quarto_lugar
                            rodada_id.quinta_milhar = quinto_lugar
                            rodada_id.save()


                        else:
                            Rodada.objects.create(
                                rodada = rodada + 1,
                                primeira_milhar = primeiro_lugar,
                                segunda_milhar = segundo_lugar,
                                terceira_milhar = terceiro_lugar,
                                quarta_milhar = quarto_lugar,
                                quinta_milhar = quinto_lugar,

                            )

        return redirect('/')
@login_required(login_url='/login/')
def dinheiro(request):
    usuario = request.user
    dinheiro2 = funcao_ver_dinheiro(usuario)
    dinheiro3 = []
    dinheiro3.append(str(dinheiro2))
    dinheiro3 = {'dinheiros':dinheiro3}
    return render(request,'dinheiro.html',dinheiro3)
@login_required(login_url='/login/')
def conferir_resultado(request):
    dinheiro2 = Dinheiro.objects.all ()
    dados5 = {'dinheiro': dinheiro2}
    usuario = request.user

    variavel1 = 0
    variavel6 = 0
    for aleatorio5 in dinheiro2:
        variavel6 = variavel6 + 1
        print ( variavel6 )
    rodadas = variavel6
    while variavel1 < variavel6:
        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )

        if variavel1 + 1 == variavel6:
            dinheiro2 = float ( Dinheiro.get_valor ( dinheiro2[variavel1] ) )

        variavel1 = variavel1 + 1
    dinheiro3 = []
    dinheiro3.append ( str ( dinheiro2 ) )
    dinheiro3 = {'dinheiros': dinheiro3}
    rodada2 = Rodada.objects.all ()
    dados5 = {'rodada2': rodada2}

    variavel1 = 0
    variavel6 = 0
    for aleatorio9 in rodada2:
        variavel6 = variavel6 + 1
        print ( variavel6 )
    while variavel1 < variavel6:
        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )

        if variavel1 + 1 == variavel6:
            rodada = float ( Rodada.get_rodada ( rodada2[variavel1] ) )
            primeira_milhar = float(Rodada.get_primeira_milhar(rodada2[variavel1]))

            segunda_milhar = float(Rodada.get_segunda_milhar(rodada2[variavel1]))
            terceira_milhar = float(Rodada.get_terceira_milhar(rodada2[variavel1]))
            quarta_milhar = float(Rodada.get_quarta_milhar(rodada2[variavel1]))
            quinta_milhar = float(Rodada.get_quinta_milhar(rodada2[variavel1]))
            print ( rodada )

        variavel1 = variavel1 + 1
    evento = Evento.objects.all()
    dados5 = {'evento': evento}

    variavel1 = 0
    variavel6 = 0
    for aleatorio9 in evento:
        variavel6 = variavel6 + 1
        print ( variavel6 )
    while variavel1 < variavel6:
        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )
        rodada = Evento.get_rodada(evento[variavel1])
        usuario_evento = Evento.get_usuario(evento[variavel1])
        milhar = float(Evento.get_milhar(evento[variavel1]))
        aposta = float(Evento.get_valor(evento[variavel1]))
        conferir_resultado = float(Evento.get_conferir(evento[variavel1]))
        conferir_resultado2 = float(Evento.get_conferir2(evento[variavel1]))
        conferir_resultado3 = float ( Evento.get_conferir3 ( evento[variavel1] ) )
        conferir_resultado4 = float ( Evento.get_conferir4 ( evento[variavel1] ) )
        conferir_resultado5 = float ( Evento.get_conferir5 ( evento[variavel1] ) )
        dinheiro = 0
        try:
            ultimo_id2 = Dinheiro.objects.get(usuario = usuario).id
        except:
            return HttpResponse('você ainda não jogou')
        print("aqui")
        print(milhar)
        print(primeira_milhar)
        print(conferir_resultado)
        print(usuario_evento)
        print(usuario)
        voce_ganhou = ""
        if milhar  == primeira_milhar and conferir_resultado == 0:
            ultimo_id = Evento.objects.get ( milhar = milhar,
                                             rodada = rodada,
                                             usuario = usuario, ).id
            if usuario_evento == usuario:
                dinheiro = aposta * 9000 + dinheiro2 + dinheiro
                usuario = request.user


                evento2 = Evento.objects.get ( id = ultimo_id )
                evento2.conferir = 1
                evento2.save ()
                dinheiro_id = Dinheiro.objects.get(id = ultimo_id2)
                dinheiro_id.valor = dinheiro
                dinheiro_id.save ()
                voce_ganhou = "Parabéns"

        if milhar  == segunda_milhar and conferir_resultado2 == 0:
            ultimo_id = Evento.objects.get ( milhar = milhar,
                                             rodada = rodada,
                                             usuario = usuario, ).id


            evento2 = Evento.objects.get ( id = ultimo_id )
            if usuario_evento == usuario:
                dinheiro = aposta * 9000 + dinheiro2 + dinheiro
                usuario = request.user
                evento2.conferir2 = 1
                evento2.save ()
                dinheiro_id = Dinheiro.objects.get ( id = ultimo_id2 )
                dinheiro_id.valor = dinheiro
                dinheiro_id.save ()
                voce_ganhou = "Parabéns"



        if milhar  == terceira_milhar and conferir_resultado3 == 0:
            ultimo_id = Evento.objects.get ( milhar = milhar,
                                             rodada = rodada,
                                             usuario = usuario, ).id

            evento2 = Evento.objects.get ( id = ultimo_id )
            if usuario_evento == usuario:
                dinheiro = aposta * 9000 + dinheiro2 + dinheiro
                usuario = request.user
                evento2.conferir3 = 1
                evento2.save ()
                dinheiro_id = Dinheiro.objects.get ( id = ultimo_id2 )
                dinheiro_id.valor = dinheiro
                dinheiro_id.save ()
                voce_ganhou = "Parabéns"

        if milhar  == quarta_milhar and conferir_resultado4 == 0:
            ultimo_id = Evento.objects.get ( milhar = milhar,
                                             rodada = rodada,
                                             usuario = usuario, ).id


            evento = Evento.objects.get ( id = ultimo_id )
            if usuario_evento == usuario:
                dinheiro = aposta * 9000 + dinheiro2 + dinheiro
                usuario = request.user
                evento2.conferir4 = 1
                evento2.save ()
                dinheiro_id = Dinheiro.objects.get ( id = ultimo_id2 )
                dinheiro_id.valor = dinheiro
                dinheiro_id.save ()
                voce_ganhou = "Parabéns"

        if milhar  == quinta_milhar and conferir_resultado5 == 0:
            ultimo_id = Evento.objects.get ( milhar = milhar,
                                             rodada = rodada,
                                             usuario = usuario, ).id

            evento2 = Evento.objects.get ( id = ultimo_id )
            if usuario_evento == usuario:
                dinheiro = aposta * 9000 + dinheiro2 + dinheiro
                usuario = request.user
                evento2.conferir5 = 1
                evento2.save ()
                dinheiro_id = Dinheiro.objects.get ( id = ultimo_id2 )
                dinheiro_id.valor = dinheiro
                dinheiro_id.save()
                voce_ganhou = "Parabéns"



        variavel1 = variavel1 + 1
    if voce_ganhou != "Parabéns":
        voce_ganhou = "Você não ganhou ainda"
    rodada = Rodada.objects.all ()
    print(rodadas)
    validar = 1

    dados = {'resultados': rodada,'voce_ganhou': voce_ganhou,'validar': validar}
    print(dados)
    print(voce_ganhou)
    return render ( request, 'resultado.html', dados )
'''
@login_required(login_url='/login/')
def ver_pule(request):
    rodada2 = Rodada.objects.all ()
    evento3 = []

    variavel1 = 0
    variavel6 = 0
    for aleatorio9 in rodada2:
        variavel6 = variavel6 + 1
        print ( variavel6 )
    while variavel1 < variavel6:
        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )

        if variavel1 + 1 == variavel6:
            rodada = float ( Rodada.get_rodada ( rodada2[variavel1] ) ) + 1
            print ( rodada )
        if variavel1 + 1 != variavel6:
            rodada = 0
            print(rodada)

        variavel1 = variavel1 + 1
    evento2 = Evento.objects.all ()


    variavel1 = 0
    variavel6 = 0
    for aleatorio5 in evento2:
        variavel6 = variavel6 + 1
        print ( variavel6 )
    validar = 0
    while variavel1 < variavel6:
        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )
        if request.user == Evento.get_usuario(evento2[variavel1]) and rodada == Evento.get_rodada(evento2[variavel1]):
            milhar = float(Evento.get_milhar(evento2[variavel1]))
            aposta = float ( Evento.get_valor ( evento2[variavel1] ) )
            evento3.append("Esta é a milhar: " + str(milhar))
            evento3.append("Está é a aposta: " + str(aposta)  + " da milhar:" + str(milhar))
            pule = float(Evento.get_pule(evento2[variavel1]))
            validar = 1




        variavel1 = variavel1 + 1
    if validar == 0:
        milhar = 0
        aposta = 0
        pule = 0

    evento3.append("A rodada é a: " + str(rodada))
    evento3.append("O pule é: " + str(pule))

    evento3 = {'eventos':evento3}
    return render(request,'pule.html',evento3)
'''


@login_required(login_url='/login/')
def ver_pule(request):

    rodada2 = Rodada.objects.all ()
    evento3 = []

    variavel1 = 0
    variavel6 = 0
    for aleatorio9 in rodada2:
        variavel6 = variavel6 + 1
        print ( variavel6 )
    while variavel1 < variavel6:
        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )

        if variavel1 + 1 == variavel6:
            rodada = float ( Rodada.get_rodada ( rodada2[variavel1] ) ) + 1
            print ( rodada )
        if variavel1 + 1 != variavel6:
            rodada = 0
            print ( rodada )

        variavel1 = variavel1 + 1
    '''

    evento2 = Evento.objects.all ()

    variavel1 = 0
    variavel6 = 0
    for aleatorio5 in evento2:
        variavel6 = variavel6 + 1
        print ( variavel6 )
    validar = 0
    while variavel1 < variavel6:

        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )
        if request.user == Evento.get_usuario ( evento2[variavel1] ) and rodada == Evento.get_rodada (
                evento2[variavel1] ):

            milhar = float ( Evento.get_milhar ( evento2[variavel1] ) )
            aposta = float ( Evento.get_valor ( evento2[variavel1] ) )

            evento3.append ( "Esta é a milhar: " + str ( milhar ) )
            evento3.append ( "Está é a aposta: " + str ( aposta ) + " da milhar:" + str ( milhar ) )
            pule = float ( Evento.get_pule ( evento2[variavel1] ) )
            validar = 1

        variavel1 = variavel1 + 1
    if validar == 0:
        milhar = 0
        aposta = 0
        pule = 0

    evento3.append ( "A rodada é a: " + str ( rodada ) )
    evento3.append ( "O pule é: " + str ( pule ) )

    evento3 = {'eventos': evento3}
    '''
    try:
        evento = Evento.objects.filter (rodada = rodada)
    except:
        evento = "Você não jogou nessa rodada"

    try:
        pule = Evento.get_pule(evento[0])
        rodada = Evento.get_rodada(evento[0])
    except:
        pule = "Você não jogou nessa rodada"

    dados = {'eventos':evento, 'pule': pule,'rodada':rodada}


    return render(request,'pule.html',dados)

@login_required(login_url='/login/')
def teste(request):
    rodada2 = Rodada.objects.all ()
    evento3 = []

    variavel1 = 0
    variavel6 = 0
    for aleatorio9 in rodada2:
        variavel6 = variavel6 + 1
        print ( variavel6 )
    while variavel1 < variavel6:
        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )

        if variavel1 + 1 == variavel6:
            rodada = float ( Rodada.get_rodada ( rodada2[variavel1] ) ) + 1
            print ( rodada )
        if variavel1 + 1 != variavel6:
            rodada = 0
            print ( rodada )

        variavel1 = variavel1 + 1
    evento = Evento.objects.filter ( usuario = request.user,
        rodada = rodada )

    variavel1 = 0
    variavel6 = 0
    for aleatorio9 in evento:
        variavel6 = variavel6 + 1
        print ( variavel6 )
    while variavel1 < variavel6:
        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )


        pule = float ( Evento.get_pule ( evento[variavel1] ) ) + 1
        variavel1 = variavel1 + 1

    if variavel6 == 0:
        pule = 0


    testando = []
    testando.append(pule)
    pule = testando
    pule = {'pules': pule}
    print(pule)



    return render(request,'testando.html',pule)

@login_required(login_url='/login/')
def teste_script(request):
    rodada2 = Rodada.objects.all ()

    rodada = []

    variavel1 = 0
    variavel6 = 0
    print("aqui2")

    for indo in rodada2:
        print(indo)
        variavel6 = variavel6 + 1
        print ( variavel6 )
    while variavel1 < variavel6:
        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )


        rodada.append( int ( Rodada.get_rodada ( rodada2[variavel1] ) )  )
        print ( rodada )


        variavel1 = variavel1 + 1
    print("aqui")
    apostas = []
    dinheiro2 = []
    contando = 0
    aposta = 0
    contador = 0
    for contar_rodadas in rodada:
        evento = Evento.objects.filter ( usuario = request.user,
                                         rodada = contar_rodadas
                                      )

        for aleatorio9 in evento:
            aposta = float(Evento.get_valor(evento[contando])) + aposta
            print(aposta)
            print(contando)

            contando = contando + 1
        apostas.append(aposta)
        contador = float(contador) + 1
        if aposta == 1:

            dinheiro2.append("Você gastou: " + str(aposta) + " Real "
                                                         "na rodada de numero: " + str(contador))
        else:
            dinheiro2.append ( "Você gastou: " + str ( aposta ) + " Reais "
                                                                  "na rodada de numero: " + str ( contador ) )
        aposta = 0
        contando = 0
    print(apostas)



    if len(apostas) != len(rodada):
        apostas.append(aposta)
    print("printando apostas")
    print(apostas)
    print("printando rodadas")
    print(rodada)
    if variavel6 != 0:
        x = rodada
        y = apostas
    else:
        x = [0,1]
        y = [0,1]
    plt.title ( 'O seu dinheiro gasto por rodada' )
    plt.xlabel ( 'Rodada' )
    plt.ylabel ( 'Dinheiro gasto' )
    plt.plot ( x, y, color = 'green' )
    plt.scatter ( x, y, color = 'red' )

    fig = plt.gcf ()
    # convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO ()
    fig.savefig ( buf, format = 'png' )
    buf.seek ( 0 )
    string = base64.b64encode ( buf.read () )
    uri = urllib.parse.quote ( string )
    return render ( request, 'testando2.html', {'data': uri, 'dinheiro2': dinheiro2} )




'''
    plt.rcParams['figure.figsize'] = (11,7)


    x = [1,2,3,4,5,6,7,8,9,10]
    y = [2,4,6,8,10,12,14,16,18,20]
    plt.plot(x, y)
    plt.title('SEU TÍTULO')
    plt.xlabel('NOME DO EIXO X')
    plt.ylabel('NOME DO EIXO Y')
    plt.show()
    '''

'''
import pip
pip.main(["install","matplotlib"])
'''

@login_required(login_url='/login/')
def dinheiro_rodada(request):
    rodada2 = Rodada.objects.all ()

    rodada = []

    variavel1 = 0
    variavel6 = 0
    print("aqui2")

    for indo in rodada2:
        print(indo)
        variavel6 = variavel6 + 1
        print ( variavel6 )
    while variavel1 < variavel6:
        print ( "valor de variavel {}".format ( variavel1 ) )

        print ( "o valor de variavel3 {}".format ( variavel6 ) )


        rodada.append( float ( Rodada.get_rodada ( rodada2[variavel1] ) )  )
        print ( rodada )


        variavel1 = variavel1 + 1
    print("aqui")
    apostas = []
    contando = 0
    aposta = 0
    for contar_rodadas in rodada:
        evento = Evento.objects.filter ( usuario = request.user,
                                         rodada = contar_rodadas
                                      )

        for aleatorio9 in evento:
            aposta = float(Evento.get_valor(evento[contando])) + aposta
            print(aposta)
            print(contando)

            contando = contando + 1
        apostas.append(aposta)
        aposta = 0
        contando = 0
    print(apostas)



    if len(apostas) != len(rodada):
        apostas.append(aposta)
    dinheiro = 600
    dinheiro_rodada = []
    dinheiro_rodada2 = []
    contador = 0
    for dinheiro_perdido in apostas:
        dinheiro = dinheiro - dinheiro_perdido

        contador = float(contador) + 1
        if dinheiro != 1:
            dinheiro_rodada2.append("Você estava com: "+str(dinheiro) + " Reais" + " na rodada de numero: " + str(contador))
            dinheiro_rodada.append ( float ( dinheiro ) )




    print("printando apostas")
    print(apostas)
    print("printando rodadas")
    print(rodada)
    print(dinheiro_rodada)
    if variavel6 != 0:
        x = rodada
        y = dinheiro_rodada
    else:
        x = [0,1]
        y = [0,1]
    plt.rcParams['figure.figsize'] = (5 , 4)

    plt.title ( 'O seu dinheiro gasto por rodada' )
    plt.xlabel ( 'Rodada' )
    plt.ylabel ( 'Dinheiro gasto' )
    plt.plot ( x, y, color = 'green' )
    plt.scatter ( x, y, color = 'red' )

    fig = plt.gcf ()
    # convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO ()
    fig.savefig ( buf, format = 'png' )
    buf.seek ( 0 )
    string = base64.b64encode ( buf.read () )
    uri = urllib.parse.quote ( string )
    print(dinheiro_rodada)
    return render ( request, 'testando2.html', {'data': uri, 'dinheiro':dinheiro_rodada2, 'validar': dinheiro_rodada} )
@login_required(login_url='/login/')
def conteiner(request):
    return render(request,'modelo.html')

@login_required(login_url = '/login/')
def avaliacao(request):

    return render(request,'avaliacao.html')
@login_required(login_url = '/login/')
def comojogar(request):

    return render(request,'comojogar.html')

@login_required(login_url = '/login/')
def submit_avaliacao(request):
    if request.POST:
        usuario = request.user

        avaliacao = Avaliacao_teste.objects.filter(usuario = usuario)

        variavel1 = 0
        avaliacao_variavel = request.POST.get ( 'rating' )
        descricao = request.POST.get('descricao')
        try:
            avaliacao_variavel = int(avaliacao_variavel)
        except:
            avaliacao_variavel = 0
        for teste in avaliacao:
            variavel1 = variavel1 + 1
        print(avaliacao)
        if variavel1 == 0:

            Avaliacao_teste.objects.create(avaliacao = avaliacao_variavel,
                                           usuario = usuario)
        else:
            ultimo_id = Avaliacao_teste.objects.get (
                                             usuario = usuario ).id
            classificacao_id = Avaliacao_teste.objects.get ( id = ultimo_id )
            classificacao_id.avaliacao = avaliacao_variavel
            classificacao_id.descricao = descricao
            classificacao_id.save ()
        print(usuario)


    return redirect ( '/' )

def cadastrar_usuario(request):
    return render(request, "registro.html")
def voltar(request):
    return redirect( "/" )
def cadastrar_confirmar(request):
    print(request.POST)

    if request.POST:
        print("entrou aqui?")

        usuario = request.POST.get ( 'usuario' )
        senha = request.POST.get ( 'senha' )
        email = request.POST.get('email')
        sexo = request.POST.get('sexo')

        try:
            print("e aqui?")
            user = User.objects.create_user ( str(usuario), str(email),  str(senha) )
            print("chegou aqui23")

        except:
            User.objects.get(usuario = usuario)
            print("aqui")


            return HttpResponse('<h1> Usuario já cadastrado </h1>')

        print("hey")
        return redirect('/')
    return HttpResponse('<h1> Digite o correto </h1>')

@login_required(login_url='/login/')
def online(request):
    while True:
        print ( "passou 3 minutos" )
        usuario = request.user

        try:
            ver_data = Online_esta.objects.get(usuario = usuario)
            print(ver_data.data)
            data_e_hora_atuais = datetime.now ()
            diferenca = timedelta ( hours = -3 )
            fuso_horario = timezone ( diferenca )
            data_e_hora_sao_paulo = data_e_hora_atuais.astimezone ( fuso_horario )
            data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime ( "%d/%m/%Y %H:%M" )
            ver_data.data = data_e_hora_sao_paulo_em_texto
            ver_data.save()
        except:

            data_e_hora_atuais = datetime.now ()
            diferenca = timedelta ( hours = -3 )
            fuso_horario = timezone ( diferenca )
            data_e_hora_sao_paulo = data_e_hora_atuais.astimezone ( fuso_horario )
            data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime ( "%d/%m/%Y %H:%M" )

            a = Online_esta.objects.create(usuario = usuario,
                                      data = data_e_hora_sao_paulo_em_texto
                                  )
        dados = Online_esta.objects.all()
        print(dados)
        variavel1 = 0
        online = ""
        vetor_que_vai = []
        for variavel in dados:
            variavel1 = variavel1 + 1
            usuario = request.user
            print(variavel)
            print(variavel.usuario)
            vetor2 = []
            for teste2 in variavel.data:
                vetor2.append(teste2)




            data_e_hora_atuais = datetime.now ()
            diferenca = timedelta ( hours = -3 )
            fuso_horario = timezone ( diferenca )
            data_e_hora_sao_paulo = data_e_hora_atuais.astimezone ( fuso_horario )
            data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime ( "%d/%m/%Y %H:%M" )
            print(data_e_hora_sao_paulo_em_texto)
            contador = 0
            a = 0
            tempo = 6

            for teste in data_e_hora_sao_paulo_em_texto:
                print ( "teste :" + str ( teste ) )
                print ( "vetor2: " + str ( vetor2[contador] ) )

                print(contador)
                if str ( teste ) == vetor2[contador]:
                    print ( "são iguais" + str(teste) + str(contador))
                    a = a + 1
                    print("a: " + str(a))

                if contador == 14:
                    contador14 = int(teste)
                    contado14 = int(vetor2[contador])


                if contador == 15:
                    if int(contador14) == int(contado14):
                        valor = int(teste) - int(vetor2[contador])
                        print("usuario + 14" + str(variavel.usuario) )
                        print(valor)
                        print("ei eu sou o valor:" + str(valor))
                        if valor <= 5:
                            online = variavel.usuario
                            vetor_que_vai.append(online)
                            print("ei, eu entrei aqui o online é :" + str(online))

                    if int(contador14) == int(contado14) + 1:
                        valor = int(vetor2[contador]) + 5
                        if valor >= int(teste) + 10:
                            online = variavel.usuario
                            vetor_que_vai.append(online)
                            print("não chegou aqui? : " + str(online)  +  " " + str(vetor_que_vai) )


                contador = contador + 1

        print(online)
        print(vetor_que_vai)
        dados = {'dados':dados, 'onlines':vetor_que_vai}



        return render(request, 'online.html',dados)
        time.sleep(180)


@login_required(login_url='/login/')
def localizacao_submit(request):
    contador = 0
    while True:
        contador = contador + 1

        if request.POST:
            a1 = request.POST.get('txtstart')
            a2 = request.POST.get('txtstart2')
            print(a1)
            print(a2)

            Localizacao.objects.create(latitude=a1,
                                       longitude=a2,
                                       usuario = request.user )
            a3 = -8.078881899999999
            a4 = -34.93801080000001
            a2 = float(a2)
            a1 = float(a1)
            a = distance(a1,a2,a3,a4)
            print(a)

        return redirect('/localizacao/')
        time.sleep(5)
    print("to vindo aqui" + str(contador))


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...

@login_required(login_url='/login/')
def posicao(request):
    if not request.user.has_perm('poll.change_poll'):
        return HttpResponseForbidden('Nope!')
    localizacao2 = Localizacao.objects.all()
    dados = {'localizacoes':localizacao2}
    variavel1 = 0
    variavel6 = 0
    for aleatorio9 in localizacao2:
        variavel6 = variavel6 + 1
    print("hey sou variavel6: " + str(variavel6))
    c = []

    while variavel1 < variavel6:
        if variavel1 > 0:
            c.append(distance(a,b,float(Localizacao.get_latitude(localizacao2[variavel1])),float(Localizacao.get_longitude(localizacao2[variavel1]))))


        print(Localizacao.get_latitude(localizacao2[variavel1]))
        a = float(Localizacao.get_latitude(localizacao2[variavel1]))
        print(Localizacao.get_longitude(localizacao2[variavel1]))
        b = float(Localizacao.get_longitude(localizacao2[variavel1]))

        variavel1 = variavel1 + 1


    if variavel6 == 0:
        print("alo")

    dados = {'localizacoes': localizacao2,'posicao': c}

    print(str(localizacao))
    return render(request, 'posicao.html',dados)


def localizacao(request):
    while True:
        print("alo2")

        return render(request,'localizacao.html')
        time.sleep(180)

def localizacaolocalizacao(request):
    while True:
        print("alo2")

        return render(request,'ver_localizacao.html')
        time.sleep(180)


def imagem(request):
    return render(request,'teste_imagens.html')


@login_required(login_url='/login/')
def comparar(request,rodada):
    rodada = int(rodada)
    print(rodada)

    evento = Evento.objects.filter(usuario=request.user,
                                   rodada=rodada)
    print(evento)
    rodada = Rodada.objects.filter(rodada=rodada)
    print(rodada)
    variavel6 = 0
    variavel1 = 0
    for aleatorio9 in evento:
        variavel6 = variavel6 + 1
    print("hey sou variavel6: " + str(variavel6))
    c = []

    while variavel1 < variavel6:
        if variavel1 > 0:
            pule = int(Evento.get_pule(evento[variavel1]))
        pule = int(Evento.get_pule(evento[variavel1]))

        variavel1 = variavel1 + 1


    try:
        dados = {'eventos':evento,'rodada':rodada,'pule':pule}
    except:
        return HttpResponse('<h1> Parece que você não jogou nessa rodada >: <h1>')

    return render(request, 'comparar.html',dados)



@login_required(login_url='/login/')
def submit_rodada_inicio(request):
    if request.POST:
        rodada = request.POST.get('rodada')


    return  redirect('/inicio/comparar/'+ str(rodada))



@login_required(login_url='/login/')
def rodada_filtrar(request):
    if request.POST:
        rodada = request.POST.get('rodada')


    return  redirect('/inicio/resultado/'+ str(rodada))

@login_required(login_url='/login/')
def resultado_filtro(request,rodada):
    while True:
        print ( "passou 3 minutos" )

        usuario = request.user
        ver_se_esta_online(usuario)
        #essa variavel faz aparecer o botão ou não aparecer o botão de conferir no resultado.html
        validar = 0
        rodada = Rodada.objects.filter(rodada=rodada)
        rodadas = quantidade_de_rodadas(validar)
        dados = {'resultados':rodada,'validar':validar,'rodadas':rodadas}


        return render(request,'resultado.html',dados)