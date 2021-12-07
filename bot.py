import discord
from discord.ext import commands
client = commands.Bot(command_prefix='sh!')

@client.event
async def on_ready():
    print('status:online')


@client.command(aliases=['purge'])
async def clear(ctx, amount=11):
    if (not ctx.author.guild_permissions.administrator):
        await ctx.send(' admin perms needed')
        return
    amount = amount + 1
    if amount > 99999:
        await ctx.send("wont work - reduce the number you are erasing")
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send('purge process: successfull')

#https://github.com/abutalhaalam/discordpurgebot/


client.run('TOKEN)
