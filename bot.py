import discord
from discord.ext import commands
import os
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import bot


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '>', intents=intents)

@client.event
async def on_ready():
  print("The bot is now ready for use!")
  print("-----------------------------")


  @client.command()
  async def hello(ctx):
    await ctx.send('Hello, i am omar but better and cooler')

@client.event
async def on_member_join(member):
  channel = client.get_channel(829328261905514503)
  await channel.send("A new member just spawned; suck his dick")

@client.event
async def on_member_remove(member):
  channel = client.bet_channel(829328261905514503)
  await channel.send("A member just despawned. no dick :(")


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'User {member} has been kicked')

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have permission to kick people!")



@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'User {member} has been banned')

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have permission to ban people!")


client.run('ODk0MjY0Mjk1MjAwODAwODA5.YVnehg.Bjab3DOx8OFv7B9L0efWRe7DivA')
