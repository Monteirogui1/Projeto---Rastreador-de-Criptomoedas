# 1100925310
#
from classes import CoinGeckoAPI, TelegramBot
import locale
from datetime import datetime
from time import sleep

id_moeda = input('Qual o ID da moeda a ser rastreada? ')
valor_minimo = int(input('Qual o valor mínimo para iniciar rastreamento? '))
valor_maximo = int(input('Qual o valor máximo para iniciar rastreamento? '))

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


api = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
bot = TelegramBot(token='', chat_id=)

while True:

    if api.ping():
        print('API Online!')
        preco, atualizado_em = api.consulta_preco(id_moeda=id_moeda)
        print('Consulta realizada com sucesso!')
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = None

        if preco < valor_minimo:
            mensagem = f'*Cotação do Ethereum*: \n\t *Preço*: R$ {preco} \n\t *Horário*: {data_hora} ' \
                       f'\n\t *Motivo*: Valor menor que o mínimo'
        elif preco > valor_maximo:
            mensagem = f'*Cotação do Ethereum*: \n\t *Preço*: R$ {preco} \n\t *Horário*: {data_hora} ' \
                       f'\n\t *Motivo*: Valor maior que o máximo'
        if mensagem:
            bot.envia_mensagem(texto_markdown=mensagem)
    else:
        print('API Offline, tente novamente mais tarde!')

    sleep(300)
