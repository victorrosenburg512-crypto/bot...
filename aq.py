import discord
import random
from discord.ext import commands
import os
from model import get_class
 
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def dicaslixo(ctx):
    await ctx.channel.send('Para reuzir o lixo é preciso mudar seus hábitos, usando como base os 3®️s:')
    await ctx.channel.send("Reduzir: reduzir oque você compra, tambem reduz o lixo que você gera")
    await ctx.channel.send('Reutilizar: significa dar nova utilidade a um objeto antes de descartá-lo.')
    await ctx.channel.send("Reciclar:  transformar o resíduo em matéria-prima para algo novo, que tenha uma nova função")

@bot.command()
async def dicasr3rs(ctx):
    await ctx.channel.send('Para colocar os 3®️s em pratica, você precisa reduzir oque você compra, focando em produtos com pouca embalagem. Você deve reutilizar sacolas plasticas, folhas usadas e separar seu lixo corretamente para a coleta seletiva.')
    await ctx.channel.send("Reciclar em casa transforma resíduos como papelão, garrafas PET, vidros e rolos de papel higiênico em itens decorativos e organizadores, economizando dinheiro e ajudando o meio ambiente.")

@bot.command()
async def perigos(ctx):
    await ctx.channel.send("⚠️O descarte de maneira errada de lixo causa sérios riscos à saúde pública, como a proliferação animais de causadores de doenças, poluição do solo e lençóis freáticos, contaminação do ar, entupimento de bueiros causando enchentes, além de danos à vida animal.⚠️")
    await ctx.channel.send("✅O descarte correto do lixo envolve separar resíduos em recicláveis e orgânicos, limpar embalagens, e destinar lixo eletronico a pontos de coleta específicos. Essa prática evita a contaminação, facilita a reciclagem, protege o meio ambiente e evita entupimentos de esgoto.✅")

@bot.command()
async def ondefica(ctx):
    await ctx.channel.send("O lixo e descartado em varios locais mas os principais são lixões e aterros:")
    await ctx.channel.send("Aterros sanitários🖼️: são estruturas de engenharia projetadas para o descarte seguro de resíduos, com impermeabilização do solo e tratamento de gases, evitando contaminação ambiental.(+1000 de aura👍)")
    await ctx.channel.send("Lixões 🗑️: são depósitos a céu aberto, sem qualquer proteção, ilegais e prejudiciais à saúde pública.(-10000 de aura👎)")

@bot.command()
async def tempo(ctx):
    with open( 'images/lixo.png', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def comandos(ctx):
     await ctx.channel.send("ondefica : mostra onde o lixo fica/ tempo: mostra o tempo de decomposição /perigos: perigos de descartar errado o lixo e como descartar /dicaslixo : mostra dicas para reduzir o lixo /dicasr3rs: mostra dicas para realizar os 3rs")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            print(f"Recebendo imagem{file_name} - URL{file_url}")
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Imagem salva em ./{attachment.filename}")
            #fazer previsão com o modelo
            class_name, confidence_score = get_class(model_path="./keras_model.h5", labels_path="./labels.txt", image_path= f"./{attachment.filename}")
            await ctx.send(f"Classe: {class_name}, Confiança: {confidence_score:.2f}")




    else:
        await ctx.send("Nenhuma imagem foi enviada.")


bot.run("")