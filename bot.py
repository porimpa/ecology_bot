import discord
from discord.ext import commands
from random import choice
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ecology(ctx):
    lst = [
        'Замените обычную лампочку на энергосберегающую. Они потребляют на три четверти меньше энергии и работают в 10 раз дольше.',
        'Если у вас есть лишнее время то вот вам совет: посадите дерево во дворе или в парке',
        'Замените одноразовые полотенца традиционными из ткани'
    ]
    await ctx.send(choice(lst))


bot.run(TOKEN)
