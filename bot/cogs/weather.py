import requests
import datetime as dt
import typing as t
import discord
from discord.ext import commands
import json

with open("data/api_key.0", "r", encoding="utf-8") as f:
    API_KEY = f.read()

class Weather(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="search")
    async def search_command(self, ctx):
        msg = ctx.message.content.split()
        place = '+'.join(msg[1:])
        url = f"http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}&lang=pt"
        response = requests.request("GET", url).json()
        temp = str("%.2f" % (float(response["main"]["temp"]) - 273.0))
        sens = str("%.2f" % (float(response["main"]["feels_like"]) - 273.0))
        temp_min = str("%.2f" % (float(response["main"]["temp_min"]) - 273.0))
        temp_max = str("%.2f" % (float(response["main"]["temp_max"]) - 273.0))
        pressure = str(response["main"]["pressure"])
        humidity = str(response["main"]["humidity"])
        new_place = ' '.join(msg[1:])
        newmsg = "Cidade: " + new_place + "\nClima: " + response["weather"][0]["description"] + "\nTemperatura: " + temp + "ºC \nSensação Térmica: " + sens + "ºC \nTemperatura mínima: " + temp_min + "ºC \nTemperatura máxima: " + temp_max + "ºC \nPressão: " + pressure + "\nUmidade: " + humidity
        await ctx.send(newmsg)

    @commands.command(name="state")
    async def state_command(self, ctx):
        await ctx.send("Digite a cidade desejada: ")
        city_msg = await self.bot.wait_for('message')
        tmp = city_msg.content.split()
        cidade = '+'.join(tmp)
        await ctx.send("Digite o estado desejado: ")
        state_msg = await self.bot.wait_for('message')
        tmp = state_msg.content.split()
        estado = '+'.join(tmp)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade},{estado}&appid={API_KEY}&lang=pt"
        response = requests.request("GET", url).json()
        temp = str("%.2f" % (float(response["main"]["temp"]) - 273.0))
        sens = str("%.2f" % (float(response["main"]["feels_like"]) - 273.0))
        temp_min = str("%.2f" % (float(response["main"]["temp_min"]) - 273.0))
        temp_max = str("%.2f" % (float(response["main"]["temp_max"]) - 273.0))
        pressure = str(response["main"]["pressure"])
        humidity = str(response["main"]["humidity"])
        newmsg = "Cidade: " + city_msg.content + ", " + state_msg.content + "\nClima: " + response["weather"][0]["description"] + "\nTemperatura: " + temp + "ºC \nSensação Térmica: " + sens + "ºC \nTemperatura mínima: " + temp_min + "ºC \nTemperatura máxima: " + temp_max + "ºC \nPressão: " + pressure + "\nUmidade: " + humidity
        await ctx.send(newmsg)

def setup(bot):
    bot.add_cog(Weather(bot))

#modularizar o código --> aprimoração
    # Transformar em uma variavel -> conversão de temperatura
# Transformar a conversão de temperatura em função --> temp, sens ...
# Transformar a chamada da URL em função
# Colocar todas as funções dentro de uma classe WeatherAPI
