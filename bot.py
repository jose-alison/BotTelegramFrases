import telebot
import requests
import json
from translate import Translator


CHAVE_API = 'API_KEY'

bot = telebot.TeleBot(CHAVE_API)


def consulta():
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response = json.loads(response.text)
    frase = (response['quoteText'] + response['quoteAuthor'])

    translator = Translator(to_lang="pt")
    translation = translator.translate(frase)

    return translation


@bot.message_handler(commands=['Pensamento'])
def pensamento(mensagem):
    bot.reply_to(mensagem, consulta())


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def menuinicial(mensagem):
    texto = '''Escolha uma opção:
/Pensamento
    '''

    bot.reply_to(mensagem, texto)


bot.polling()
