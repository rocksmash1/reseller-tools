from discord.ext.commands import Bot
import discord
from discord.ext import commands
from discord.utils import get

TOKEN = "TOKEN GOES HERE"
BOT_PREFIX = "+"

client = Bot(command_prefix=BOT_PREFIX)
discor = discord.Client()

client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is logged on")

@client.command(name="fee",
                pass_context = True)
async def fee(ctx, amount):
   
    ppfee = float(amount)*0.025
    ppfinal = str(float(amount) - ppfee)

    mfee = float(amount)*0.1
    mfinal = str(float(amount) - mfee)

    eb1 = float(amount) *0.9
    eb2 = float(eb1)*0.029
    eb3 = float(eb1)-eb2
    eb4 = float(eb3)-0.3

    s1 = float(amount)*0.095
    s2 = float(amount)*0.03
    s3 = float(amount) - s1 - s2

    g1 = float(amount)*0.095
    g2 = float(amount) - g1
    g3 = float(g2) - 5

    gr1 = float(amount)*0.06
    gr2 = float(amount) - gr1
    gr3 = gr2*0.029
    gr3 = gr2-gr3
    gr4 = gr3-0.3

    ppemoji = get(client.get_all_emojis(), name='paypal')
    memoji = get(client.get_all_emojis(), name='mercari')
    eboji = get(client.get_all_emojis(), name='ebay')
    stoji = get(client.get_all_emojis(), name='stockx')
    goaji = get(client.get_all_emojis(), name='goatlogo')
    groji = get(client.get_all_emojis(), name="grailed")

    emb = discord.Embed(title='Total Profits', colour=1111111)
    emb.set_footer(text='Made by @xrocksmashx')
    emb.add_field(name=str(ppemoji) + "PayPal Total Profit (2.5% Fee)", value="$" + str(ppfinal), inline=False)
    emb.add_field(name=str(memoji) + "Mercari (10% Fee)", value="$" + str(mfinal), inline=False)
    emb.add_field(name=str(eboji) + "Ebay Total Profit (10% Fee - 2.9% Transaction Fee)", value="$" + str(eb4), inline=False)
    emb.add_field(name=str(stoji) + "StockX Total Profit (9.5% - 3% Fee)", value="$" + str(s3), inline=False)
    emb.add_field(name=str(goaji) + "GOAT Total Profit (9.5% - $5 Fee)", value="$" + str(g3), inline=False)
    emb.add_field(name=str(groji) + "Grailed Total Profit (6% - 2.9% Transaction Fee)", value="$" + str(gr4), inline=False)


    await client.send_message(ctx.message.channel, embed=emb)

@client.command(name="money",
                pass_context=True)
async def money(ctx, curr, val):
    if curr.upper() == "US":
        efinal = float(val) * 0.86
        pfinal = float(val) * 0.77
        emb = discord.Embed(title='US Dollar Converter', colour=1111111)
        emb.set_footer(text='Made by @xrocksmashx')
        emb.add_field(name="Euro", value="€" + str(efinal), inline=False)
        emb.add_field(name="British Pound", value="£" + str(pfinal), inline=False)
        await client.send_message(ctx.message.channel, embed=emb)
    if curr.upper() == "EU":
        efinal = float(val) * 1.16
        pfinal = float(val) * 0.89
        emb = discord.Embed(title='Euro Converter', colour=1111111)
        emb.set_footer(text='Made by @xrocksmashx')
        emb.add_field(name="American Dollar", value="$" + str(efinal), inline=False)
        emb.add_field(name="British Pound", value="£" + str(pfinal), inline=False)
        await client.send_message(ctx.message.channel, embed=emb)
    if curr.upper() == "UK":
        efinal = float(val) * 1.30
        pfinal = float(val) * 1.12
        emb = discord.Embed(title='British Pound Converter', colour=1111111)
        emb.set_footer(text='Made by @xrocksmashx')
        emb.add_field(name="American Dollar", value="$" + str(efinal), inline=False)
        emb.add_field(name="Euro", value="€" + str(pfinal), inline=False)
        await client.send_message(ctx.message.channel, embed=emb)
    else:
        await client.say("Currency type not supported, please use US, UK, or EU")

@client.command(name="size",
                pass_context=True)
async def shoe(ctx, region, size):
    if region.upper() == "US":
        efinal = float(size) - -0.5
        pfinal = float(size) + 32.5
        emb = discord.Embed(title='US Size Converter', colour=1111111)
        emb.set_footer(text='Made by @xrocksmashx')
        emb.add_field(name="UK Size", value=str(efinal), inline=False)
        emb.add_field(name="EU Size", value=str(pfinal), inline=False)
        await client.send_message(ctx.message.channel, embed=emb)
    if region.upper() == "UK":
        efinal = float(size) + 0.5
        pfinal = float(size) + 33
        emb = discord.Embed(title='UK Size Converter', colour=1111111)
        emb.set_footer(text='Made by @xrocksmashx')
        emb.add_field(name="US Size", value=str(efinal), inline=False)
        emb.add_field(name="EU Size", value=str(pfinal), inline=False)
        await client.send_message(ctx.message.channel, embed=emb)
    if region.upper() == "EU":
        efinal = float(size) - 32.5
        pfinal = float(size) -33
        emb = discord.Embed(title='EU Size Converter', colour=1111111)
        emb.set_footer(text='Made by @xrocksmashx')
        emb.add_field(name="US Size", value=str(efinal), inline=False)
        emb.add_field(name="UK Size", value=str(pfinal), inline=False)
        await client.send_message(ctx.message.channel, embed=emb)
    else:
        await client.say("Region not supported, please use US, UK, or EU")
        
@client.command(name="ping",
                pass_context=True)
async def ping(ctx):
    emb = discord.Embed(title='Pong', colour=1111111)
    emb.add_field(name="Online?", value=":white_check_mark:", inline=False)
    await client.send_message(ctx.message.channel, embed=emb)
    

@client.command(name="help",
                pass_context=True)
async def help(ctx):
    emb = discord.Embed(title='Help', colour=1111111)
    emb.set_footer(text='Made by @xrocksmashx')
    emb.add_field(name="Size Converter", value="Use +size [UK, US, or EU] [size]. This will convert your size into other sizes from different regions", inline=False)
    emb.add_field(name="Money Converter", value="Use +money [UK, Us or EU] [amount]. This will give you a conversion for each currency", inline=False)
    emb.add_field(name="Fee Checker", value="Use +fee [amount]. This will give you the total you will make after fees from each site", inline=False)
    emb.add_field(name="Ping", value="Use +ping to check if the bot is online!", inline=False)
    emb.add_field(name="Help", value="Use +help to show this page", inline=False)
    await client.send_message(ctx.message.channel, embed=emb)   

client.run(TOKEN)