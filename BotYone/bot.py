from discord.ext import commands
import discord
import datetime
import os

carpeta_principal = os.path.dirname(__file__)
carpeta_info_text = os.path.join(carpeta_principal,"txt")


#MTIyMjcyOTI0ODIwNTMwNzk1NA.GafUx9.EE2WasEI6zX60dh_4Xz3YWMcgZxaBZfJf1Xt3g   PHPollo (Pepe)
#MTIyMjczMDAxODUwNTg4MzczOA.GHdXyb.EePGSLHa6XVRsBoVDyQvpCXcZqzE7rqCOtph0g   VN (Yone)
BOT_TOKEN = "MTIyMjczMDAxODUwNTg4MzczOA.GHdXyb.EePGSLHa6XVRsBoVDyQvpCXcZqzE7rqCOtph0g"
SERVIDOR_ID = 1217603886647345264
CANALES_ID = {
    "CODIGOS-BOTS" :1222728434371924101,
    "SANCIONES" : 1221317923864318013}
NAME_BOT = "Yone"

bot = commands.Bot(command_prefix= "!", intents= discord.Intents.all())

@bot.event
async def bot_encendido():
    print("El bot de prueba se encuentra en funcionamiento")
    canal = bot.get_channel(CANALES_ID["CODIGOS-BOTS"])
    await canal.send("El bot de prueba se encuentra en funcionamiento")

@bot.event
async def bienvenida(miembro : discord.Member):
    if miembro.guild.id == SERVIDOR_ID:
        canal = miembro.guild.get_channel(1217603886647345266)
        await canal.send(f"BIENVENIDO A PEPE {miembro.mention}")

@bot.command()
async def escribir(ctx, member: discord.Member):
    roles_sancion = [1226939943323041964, 1226940428679516240, 1226940558954467448, 1227360391458193501]
    await ctx.send(member.add_roles(ctx.guild.get_role(roles_sancion[3])))

@bot.command()
async def addrole(ctx, role: discord.Role, member: discord.Member):
    await member.add_roles(role)
    await ctx.send(f"Se ha asignado correctamente el rol {role.mention} a {member.mention}.")

@bot.command(name= "borrar_msg")
async def borrar_msg(ctx : commands.Context, id_mensaje : int):
    try:
        informacion_recopilada = {
            "MENSAJE_REPORTADO" : await ctx.fetch_message(id_mensaje),
            "CONTENIDO_MENSAJE" : (await ctx.fetch_message(id_mensaje)).content,
            "CANAL_ORIGEN" : ctx.message.channel,
            "AUTOR" : (await ctx.fetch_message(id_mensaje)).author.name,
            "ID_AUTOR" : (await ctx.fetch_message(id_mensaje)).author.id,
            "NOMBRE_EJECUTADOR" : ctx.author.name,
            "ID_EJECUTADOR" : ctx.author.id
        }

        await informacion_recopilada["MENSAJE_REPORTADO"].delete()

        roles_autor = ctx.guild.get_member(informacion_recopilada["ID_AUTOR"]).roles
        roles_ejecutador = ctx.guild.get_member(informacion_recopilada["ID_EJECUTADOR"]).roles
        nombres_roles_autor = [roles_autor.name for roles_autor in roles_autor]
        nombres_roles_ejecutador = [roles_ejecutador.name for roles_ejecutador in roles_ejecutador]
        await ctx.send(nombres_roles_ejecutador)
        if "𝑃𝑟𝑜𝑔𝑟𝑎𝑚𝑎𝑑𝑜𝑟👨\u200d💻" or "𝑲𝒊𝒏𝒈𝒔👑" in nombres_roles_ejecutador:
            await ctx.send ("ejecutar comando")
            
            lista_palabras_baneables = ["puto", "mierda", "ctm", "culeado", "concha de tu madre"]
            lectura_de_palabras_baneables = []
            for insultos in lista_palabras_baneables:
                ubicacion_insunto = informacion_recopilada["CONTENIDO_MENSAJE"].find(insultos)
                if ubicacion_insunto != -1:
                    lectura_de_palabras_baneables.insert(0, insultos)
            
            print("ARROZ")        
            if lectura_de_palabras_baneables.__len__() == 0:
                info_aviso_injustificado = f"""///AVISO DE COMANDO INJUSTIFICADO///
                Se presento comando ´borrar_msg´ pero el mensaje filtrado no presenta ningun signo de vocabulario indevido.
                Por esto mismo no se ejecutara completamente este comando.
                El que ejecuto el comando fue: {informacion_recopilada['NOMBRE_EJECUTADOR']}
                
                Por favor no me utilizes de esta forma o se tomaran medidas como se deben.
                Muchas gracias."""
                
                embed = discord.Embed(title= f"{ctx.guild.name}", description= info_aviso_injustificado, timestamp= datetime.datetime.utcnow())
                direccion_canal = bot.get_channel(CANALES_ID["SANCIONES"])
                await direccion_canal.send(embed= embed)
            
            if "+18👨🏻" in nombres_roles_autor:
                if lectura_de_palabras_baneables.__len__() > 0:
                    info_sancion_texto = f"""///MENSAJE BORRADO///
                    Se presento comando ´borrar_msg´.
                    El mensaje contenia lo siguiente escrito:
                    -{informacion_recopilada['CONTENIDO_MENSAJE']}-
                    La cantidad de palabras banebles que se detectaron fueron [{lectura_de_palabras_baneables.__len__()}]:
                    ~{lectura_de_palabras_baneables}~
                    El mensaje se ubicaba en {informacion_recopilada['CANAL_ORIGEN']}
                    Y su autor es: {informacion_recopilada['AUTOR']}
                    (VER SANCIÓN)"""

                    direccion_canal = bot.get_channel(CANALES_ID["SANCIONES"])
                    embed = discord.Embed(title= f"{ctx.guild.name}", description= info_sancion_texto, timestamp= datetime.datetime.utcnow())
                    await direccion_canal.send(embed= embed)
                    aviso_sancion = f"""A {informacion_recopilada['AUTOR']} se le detecto que utilizo [{lectura_de_palabras_baneables.__len__()}] palabras que se encuentran prohibidas dentro del seridor.
                    Las palabras que se encontraron fueron: {lectura_de_palabras_baneables}.
                    Por esto se te aplicara una sanción."""
                    
                    embed = discord.Embed(title= f"{ctx.guild.name}", description= aviso_sancion, timestamp= datetime.datetime.utcnow())
                    await ctx.send(embed= embed)
                    
                    roles_sanciones = ["Aviso1", "Aviso2", "aviso3", "Ban_temporal"]

                    if ("Aviso1" or "Aviso2" or "aviso3" or "Ban_temporal") not in nombres_roles_autor:
                        await ctx.guild.get_member(informacion_recopilada["ID_AUTOR"]).add_roles(ctx.guild.get_role(1226939943323041964))
                        print("1")

                    elif "Aviso1" in nombres_roles_autor:
                        await ctx.guild.get_member(informacion_recopilada["ID_AUTOR"]).add_roles(ctx.guild.get_role(1226940428679516240))
                        await ctx.guild.get_member(informacion_recopilada["ID_AUTOR"]).remove_roles(ctx.guild.get_role(1226939943323041964))
                        print("2")
                    
                    elif "Aviso2" in nombres_roles_autor:
                        await ctx.guild.get_member(informacion_recopilada["ID_AUTOR"]).add_roles(ctx.guild.get_role(1226940558954467448))
                        await ctx.guild.get_member(informacion_recopilada["ID_AUTOR"]).remove_roles(ctx.guild.get_role(1226940428679516240))
                        print("3")
                    
                    elif "Aviso3" in nombres_roles_autor:
                        await ctx.guild.get_member(informacion_recopilada["ID_AUTOR"]).add_roles(ctx.guild.get_role(1227360391458193501))
                        await ctx.guild.get_member(informacion_recopilada["ID_AUTOR"]).remove_roles(ctx.guild.get_role(1226940558954467448))
                        
                        print("4")
                    
                    print("SALMON")

                    #roles_sancion = [1226939943323041964, 1226940428679516240, 1226940558954467448, 1227360391458193501]

                    
        else:
            await ctx.send("...USTED NO TIENE PERMISO PARA UTILIZAR ESTE COMANDO...")
    except discord.NotFound:
        await ctx.send("El Mensaje que desea eliminar no se pudo encontrar")
    except discord.Forbidden:
        await ctx.send("/ACCIÓN DENEGADA/")
        
        

@bot.command()
async def estado_bot(ctx):
    with open('Errores_del_codigo.txt', 'r') as f:
        texto = f.read()
    diccionario_errores = {"@BOT.EVENT(bot_encendido)": "En pausa"
                           }
    embed = discord.Embed(title= f"{ctx.guild.name}", description= (texto[0:133] + str(diccionario_errores.__len__()) + texto[133:173] + NAME_BOT + texto[173:-1]) , timestamp= datetime.datetime.utcnow())
    await ctx.send(embed=embed)
    error_numero = 0
    for errores in diccionario_errores:
        error_numero += 1
        with open(f'ERROR_CODIGO_00{str(error_numero)}.txt', 'r') as f:
            texto_error = f.read()
        embed = discord.Embed(description= (errores + diccionario_errores[errores] + texto_error) , timestamp= datetime.datetime.utcnow())
        await ctx.send(embed=embed)

@bot.command()
async def list_commands(ctx):
    diccionario_comandos = {
        "comando (prueba) llamada_usuario" : "Completado",
        "comando borrar_msg" : "EN ACTUALIZANDO",
        "comando estado_bot" : "COMPLETADO"
    }
    for dcommands in diccionario_comandos:
        await ctx.send(f"- {dcommands} se encuentra en fase: /{diccionario_comandos[dcommands]}/")

bot.run(BOT_TOKEN)