import discord
from discord.ext import commands
import datetime
from urllib import parse,request
import re

bot = commands.Bot(command_prefix=">", description="No soy un bot")

# Ping... pong
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

# Operaciones
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def rest(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne - numTwo)

@bot.command()
async def mult(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne * numTwo)

@bot.command()
async def div(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne / numTwo)

@bot.command()
async def pro(ctx):
    await ctx.send("El mas pro es @Maximo 4ever#8286")
 
# Informacion del servidor
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title=f"{ctx.guild.name}",
        description="Servidor del mas pro.",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue()
    )
    embed.add_field(name="Servidor creado el", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Creador del servidor", value=f"{ctx.guild.owner}")
    embed.add_field(name="Region del servidor", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del servidor", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80")
    await ctx.send(embed=embed)

# Busqueda de youtube
@bot.command()
async def YT(ctx, *, search):
    query_string = parse.urlencode({"search_query": search})
    html_content = request.urlopen("https://youtube.com/results?" + query_string)
    search_results = re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    #print(search_results)
    await ctx.send("https://www.youtube.com/watch\?v=" + search_results[0])

# Events
@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Streaming(
            name="Minecraft", url="https://www.twitch.tv/maximo_4ever"
        )
    )
    print("Bot listo")


bot.run("OTIxNzkzNDIzODQzOTM0MjA4.Yb4FBg.Nfvjva1u6RQTY8Xt9Ye-lW8E5LI")
