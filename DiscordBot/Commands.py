from discord.ext.commands import Context
from discord import Message

class Commands():  
  async def exit(self, ctx: Context):
    if not await ctx.bot.is_owner(ctx.author):
      return await ctx.send(f"I'm sorry {ctx.author.name}, I'm afraid I can't do that")
    return await ctx.bot.logout();