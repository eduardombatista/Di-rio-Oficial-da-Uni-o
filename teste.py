from bs4 import BeautifulSoup as bs
import requests
from _datetime import datetime
import DOU
import os
import csv

class infoDou:

    def tipoAviso(self): #função para extrair o conteúdo do Tipo de Ato Aviso
        os.chdir('C:\\Users\\reinan.oliveira\\Documents\\Dou') #caminho onde o arquivo está salvo
        now = datetime.now() #pegando a data  atual
        url = [] #criando uma lista vazia

        url.append(DOU.link)   # adicionando os links capturados no documento Dou.py em uma outra lista
        for url in DOU.link:   # lendo os links capturados
            page = requests.get(url) #fazendo a requisição da página através do link
            soup = bs(page.text, 'html.parser') #buscando o conteúdo html da página

            # conteinerInfo = soup.find(class_='texto-dou')
            identificacao = soup.find_all(class_='identifica') #buscando o título do conteúdo, através do nome da classe no html
            paragrafo = soup.find_all(class_='dou-paragraph') #buscando o texto do parágrafo do conteúdo, através do nome da classe no html

            titulo = identificacao[0].contents #buscando o título do conteúdo
            subTitulo = identificacao[1].contents #buscando o subtítulo do conteúdo

            processo = paragrafo[0].contents #buscando o número do processo do conteúdo
            corpoParagraph = paragrafo[1].contents #buscando o texto do parágrafo do conteúdo

            titulo = str(titulo) #convertendo a variável para string
            subTitulo = str(subTitulo) #convertendo a variável para string
            processo = str(processo) #convertendo a variável para string
            corpoParagraph = str(corpoParagraph) #convertendo a variável para string

            textoIdentificacao = titulo[2:-2] +'\n'+ subTitulo[2:-2] #eliminando letras e símbolos do início e final do conteúdo da variável
            textoParagraph = processo[2:-2] +'\n'+ corpoParagraph[2:-2] #eliminando letras e símbolos do início e final do conteúdo da variável

            textoIdentificacao = str(textoIdentificacao) #convertendo a variável para string
            textoParagraph = str(textoParagraph) #convertendo a variável para string

            '''print(textoIdentificacao)
            print(textoParagraph)
            print('----'*50)'''

            ultAtualizacao = os.path.getmtime('Diário Oficial.txt') #pegando a data da última atualização do arquivo
            dataHoraArq = datetime.fromtimestamp(ultAtualizacao).strftime('%d-%m-%Y') #formatando a data (dia-mês-ano)

            if dataHoraArq == now.strftime('%d-%m-%Y'): #condicional para saber se a data da última atualização é igual à data de hoje

                #escrever em um arquivo sem apagar seu conteúdo
                with open('Diário Oficial.txt', 'r', newline='', encoding='iso-8859-1') as saida: #abre o arquivo e o lê
                    conteudo = saida.readlines() #abre o arquivo e o lê
                    conteudo.append(textoIdentificacao + "\n" + textoParagraph+'\n') #adiciona um conteúdo

                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                    saida.writelines(conteudo) #abre novamente o arquivo e escreve o conteúdo criado anteriormente
            else:
                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida: #sobrescreve o conteúdo
                    saida.write(textoIdentificacao + "\n" + textoParagraph + '\n') #sobrescreve o conteúdo

            with open('Diário Oficial completo.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                conteudo = saida.readlines()
                conteudo.append('\n' + textoIdentificacao + '\tData: ' + dataHoraArq + "\n" + textoParagraph + '\n')

            with open('Diário Oficial completo.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                saida.writelines(conteudo)

    def tipoExtratoContrato(self): #função para extrair o conteúdo do Tipo de Ato Extrato de Contrato
        os.chdir('C:\\Users\\reinan.oliveira\\Documents\\Dou') #caminho onde o arquivo está salvo
        now = datetime.now() #pegando a data  atual
        url = [] #criando uma lista vazia

        url.append(DOU.link)  #adicionando os links capturados no documento Dou.py em uma outra lista
        for url in DOU.link:  #lendo os links capturados
            page = requests.get(url) #fazendo a requisição da página através do link
            soup = bs(page.text, 'html.parser') #buscando o conteúdo html da página

            # conteinerInfo = soup.find(class_='texto-dou')
            identificacao = soup.find_all(class_='identifica') #buscando o título do conteúdo, através do nome da classe no html
            paragrafo = soup.find_all(class_='dou-paragraph') #buscando o texto do parágrafo do conteúdo, através do nome da classe no html

            try:
                titulo = identificacao #buscando o título do conteúdo
                processo = paragrafo[0].contents #buscando o número do processo do conteúdo
                tituloProcess = paragrafo[1].contents #buscando o texto do parágrafo do conteúdo
                corpoParagraph = paragrafo[2].contents #buscando o texto do parágrafo do conteúdo

                titulo = str(titulo) #convertendo a variável para string
                processo = str(processo) #convertendo a variável para string
                tituloProcess = str(tituloProcess) #convertendo a variável para string
                corpoParagraph = str(corpoParagraph) #convertendo a variável para string

                textoIdentificacao = titulo[23:-5] #eliminando letras e símbolos do início e final do conteúdo da variável
                textoParagraph = processo[2:-2] + '\n' + tituloProcess[2:-2] + '\n' + corpoParagraph[2:-2] #eliminando letras e símbolos do início e final do conteúdo da variável
            except:
                titulo = identificacao
                corpoParagraph = paragrafo[0].contents

                titulo = str(titulo)
                corpoParagraph = str(corpoParagraph)

                textoIdentificacao = titulo[23:-5]
                textoParagraph = '\n' + corpoParagraph[2:-2]

            textoIdentificacao = str(textoIdentificacao)
            textoParagraph = str(textoParagraph)

            '''print(textoIdentificacao)
            print(textoParagraph)
            print('----' * 50)'''

            ultAtualizacao = os.path.getmtime('Diário Oficial.txt') #pegando a data da última atualização do arquivo
            dataHoraArq = datetime.fromtimestamp(ultAtualizacao).strftime('%d-%m-%Y') #formatando a data (dia-mês-ano)

            if dataHoraArq == now.strftime('%d-%m-%Y'): #condicional para saber se a data da última atualização é igual à data de hoje

                # escrever em um arquivo sem apagar seu conteúdo
                with open('Diário Oficial.txt', 'r', newline='', encoding='iso-8859-1') as saida: #abre o arquivo e o lê
                    conteudo = saida.readlines() #abre o arquivo e o lê
                    conteudo.append('\n' + textoIdentificacao + "\n" + textoParagraph + '\n') #adiciona um conteúdo

                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida: #abre novamente o arquivo e escreve o conteúdo criado anteriormente
                    saida.writelines(conteudo)  #abre novamente o arquivo e escreve o conteúdo criado anteriormente
            else:
                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida: #sobrescreve o conteúdo
                    saida.write(textoIdentificacao + "\n" + textoParagraph + '\n') #sobrescreve o conteúdo

            with open('Diário Oficial completo.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                conteudo = saida.readlines()
                conteudo.append(textoIdentificacao + dataHoraArq + "\n\n" + textoParagraph + '\n')

            with open('Diário Oficial completo.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                saida.writelines(conteudo)

    def tipoExtratoRescisao(self): #função para extrair o conteúdo do Tipo de Ato Extrato de Rescisao    #03-12-2019
        os.chdir('C:\\Users\\reinan.oliveira\\Documents\\Dou')
        global textoIdentificacao
        global textoParagraph
        now = datetime.now()
        url = []

        url.append(DOU.link)  # adicionando os links capturados no documento Dou.py em uma outra lista
        for url in DOU.link:  # lendo os links capturados
            page = requests.get(url)
            soup = bs(page.text, 'html.parser')

            # conteinerInfo = soup.find(class_='texto-dou')
            identificacao = soup.find_all(class_='identifica')
            paragrafo = soup.find_all(class_='dou-paragraph')

            titulo = identificacao
            corpoParagraph = paragrafo[0]

            titulo = str(titulo)
            corpoParagraph = str(corpoParagraph)

            textoIdentificacao = '\n'+titulo[23:-5]
            textoParagraph = corpoParagraph[25:-4]

            '''print(textoIdentificacao)
            print(textoParagraph)
            print('----' * 50)'''

            ultAtualizacao = os.path.getmtime('Diário Oficial.txt')
            dataHoraArq = datetime.fromtimestamp(ultAtualizacao).strftime('%d-%m-%Y')

            if dataHoraArq == now.strftime('%d-%m-%Y'):

                with open('Diário Oficial.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                    conteudo = saida.readlines()
                    conteudo.append('\n' + textoIdentificacao + "\n\n" + textoParagraph + '\n')

                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                    saida.writelines(conteudo)
            else:
                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                    saida.write(textoIdentificacao + "\n\n" + textoParagraph)

            with open('Diário Oficial completo.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                conteudo = saida.readlines()
                conteudo.append('\n' + textoIdentificacao + dataHoraArq + "\n\n" + textoParagraph + '\n')

            with open('Diário Oficial completo.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                saida.writelines(conteudo)

    def tipoResultadoJulgamento(self):  #função para extrair o conteúdo do Tipo de Ato Resultado de Julgamento
        os.chdir('C:\\Users\\reinan.oliveira\\Documents\\Dou')
        now = datetime.now()
        url = []
        tipo = 'Resultado de Julgamento'

        url.append(DOU.link)  # adicionando os links capturados no documento Dou.py em uma outra lista
        for url in DOU.link:  # lendo os links capturados
            page = requests.get(url)
            soup = bs(page.text, 'html.parser')

            # conteinerInfo = soup.find(class_='texto-dou')
            identificacao = soup.find_all(class_='identifica')
            paragrafo = soup.find_all(class_='dou-paragraph')

            try:
                titulo = identificacao[0].contents
                subtitulo = identificacao[1].contents
                corpoParagraph = paragrafo[0].contents

                titulo = str(titulo)
                subtitulo = str(subtitulo)
                corpoParagraph = str(corpoParagraph)

                textoIdentificacao = titulo[2:-2] + '\n' + subtitulo[2:-2]
                textoParagraph = '\n' + corpoParagraph[2:-2]
            except:
                titulo = identificacao
                corpoParagraph = paragrafo

                titulo = str(titulo)
                corpoParagraph = str(corpoParagraph)

                textoIdentificacao = '\n' + titulo[23:-5]
                textoParagraph = '\n' + corpoParagraph[26:-5]

            '''print(textoIdentificacao)
            print(textoParagraph)
            print('----' * 50)'''

            ultAtualizacao = os.path.getmtime('Diário Oficial.txt')
            dataHoraArq = datetime.fromtimestamp(ultAtualizacao).strftime('%d-%m-%Y')

            if dataHoraArq == now.strftime('%d-%m-%Y'):

                with open('Diário Oficial.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                    conteudo = saida.readlines()
                    conteudo.append('\n' + textoIdentificacao + "\n\n" + textoParagraph + '\n')

                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                    saida.writelines(conteudo)
            else:
                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                    saida.write(textoIdentificacao + "\n\n" + textoParagraph)

            with open('Diário Oficial completo.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                conteudo = saida.readlines()
                conteudo.append('\n' + textoIdentificacao + dataHoraArq + "\n\n" + textoParagraph + '\n')

            with open('Diário Oficial completo.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                saida.writelines(conteudo)


