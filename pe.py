from discord.ext import commands
import discord



bot = commands.Bot(command_prefix= "!", intents= discord.Intents.all())


@bot.event
async def encendido():
    canal = bot.get_channel(CANAL_ID)
    await canal.send("Cuchufli")

@bot.command()
async def hola(ctx):
    await ctx.send("HOLA")

@bot.command()
async def eliminar_msg(ctx, id_
                        : int, ubicacion):
    ubicacion_mensaje = {
        "ID_MENSAJE" : await ctx.fetch_message(id_m),
        "ID_CANAL" : await ctx.channel_id(CANAL_ID),
        "ID_SERVER" : await ctx.guild_id(SERVER_ID)

    }
    print(ubicacion_mensaje[ubicacion])
    await ctx("mensaje eliminado")






@bot.command()
async def message(ctx, id_mensaje : int):
    try:
        # Obtener el mensaje por su ID
        message = await ctx.fetch_message(id_mensaje)
        # Eliminar el mensaje
        await message.delete()
        await ctx.send("Mensaje eliminado correctamente.")
    except discord.NotFound:
        await ctx.send("Mensaje no encontrado.")
    except discord.Forbidden:
        await ctx.send("Permiso denegado. No puedo eliminar ese mensaje.")



bot.run(TOKEN_BOT)