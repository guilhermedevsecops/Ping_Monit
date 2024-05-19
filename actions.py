import smtplib
from email.message import EmailMessage
import urllib
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from dotenv import load_dotenv
import os

load_dotenv()

def catastrofe():
    # Configurar email e senha
    EMAIL_ADDRESS = os.getenv("EMAIL")
    EMAIL_PASSWORD = os.getenv("PASSWORD")

    # Criar um e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Monitoramento Servidor'
    msg['From'] = os.getenv("EMAIL")
    msg['To'] = os.getenv("TO")
    msg.set_content(os.getenv("MSG"))

    # Enviar um email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print('mensagem enviada')
        telegram()


def telegram():
    # telegram
    print("telegram")
    
    api_id = os.getenv("API_ID_TELEGRAM")
    api_hash = os.getenv("API_HASH")
    token = os.getenv("TOKEN")
    phone = os.getenv("PHONE")
    message = "New test Telegram"

    client = TelegramClient('session', api_id, api_hash)

    client.connect()

    if not client.is_user_authorized():

        client.send_code_request(phone)

        client.sign_in(phone, input('Enter the code: '))

    try:

        receiver = InputPeerUser('user_id', 'user_hash')

        client.send_message(receiver, message, parse_mode='html')
    except Exception as e:

        print(e)
    client.disconnect()
    print("saindo")
    client.disconnect()

   # Login já efetuado no Whatsapp
