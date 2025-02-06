import discord
import asyncio
import random

TOKEN = "token of you bot"  # Reemplázalo con tu token de bot de Discord
GUILD_ID = 111111111111111  # Reemplázalo con el ID de tu servidor
CHANNEL_ID = 111111111111111111  # Reemplázalo con el ID del canal donde enviará los mensajes

TIPS = [
    "Usa bolsas reutilizables en lugar de bolsas plásticas.",
    "Recicla papel, cartón, vidrio y plástico correctamente.",
    "Apaga las luces cuando no las necesites para ahorrar energía.",
    "Reduce el consumo de agua cerrando el grifo mientras te cepillas los dientes.",
    "Usa transporte público o bicicleta para reducir la contaminación del aire.",
    "Evita los plásticos de un solo uso, como botellas y pajillas.",
    "Planta un árbol, ayuda a capturar CO2 y mejora la biodiversidad.",
    "Compra productos con empaques biodegradables o reciclables.",
    "Dona o reutiliza la ropa en lugar de desecharla.",
    "Evita imprimir documentos si no es necesario, ahorra papel."
]

class EcoBot(discord.Client):
    async def on_ready(self):
        print(f'Conectado como {self.user}')
        await self.send_tips()

    async def send_tips(self):
        await self.wait_until_ready()
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            while not self.is_closed():
                tip = random.choice(TIPS)
                await channel.send(f'♻️ Consejo ecológico del día: {tip}')
                await asyncio.sleep(86400)  
        else:
            print("No se encontró el canal. Verifica el ID.")

intents = discord.Intents.default()
bot = EcoBot(intents=intents)
bot.run("Mtoken of your bot")
