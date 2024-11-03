import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Lista de consecuencias de la deforestación en la extinción de especies
consecuencias_extincion = [
    "El tigre de Sumatra está en peligro debido a la destrucción de su hábitat.",
    "Los orangutanes en Borneo y Sumatra están amenazados por la deforestación.",
    "El jaguar sufre de la pérdida de bosques en América Latina.",
    "El elefante asiático pierde su hogar debido a la tala de árboles.",
    "El gorila de montaña está en peligro por la deforestación en África.",
    "El oso panda gigante depende de los bosques de bambú, que están desapareciendo.",
    "El rinoceronte de Java está amenazado por la destrucción de su hábitat."
]

# Lista de datos curiosos sobre el medio ambiente
datos_curiosos = [
    "Los árboles pueden comunicarse entre sí a través de sus raíces.",
    "Un solo árbol puede absorber hasta 22 kilos de dióxido de carbono al año.",
    "Los océanos producen más del 50% del oxígeno de la Tierra.",
    "Las abejas polinizan aproximadamente el 75% de los cultivos del mundo.",
    "El calentamiento global está causando la pérdida de hielo en los polos.",
    "Las ciudades verdes pueden reducir la contaminación y mejorar la salud.",
    "Las energías renovables están en constante crecimiento en el mundo."
]

# Comando para obtener una consecuencia de la deforestación
@bot.command(name='consecuencia_extincion')
async def consecuencia_extincion(ctx):
    consecuencia = random.choice(consecuencias_extincion)
    await ctx.send(consecuencia)

# Comando para obtener un dato curioso sobre el medio ambiente
@bot.command(name='dato_curioso')
async def dato_curioso(ctx):
    dato = random.choice(datos_curiosos)
    await ctx.send(dato)

# Ejecuta el bot con tu token
bot.run("TOKEN")



