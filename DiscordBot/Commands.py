import urllib.request
from discord import File
from discord.ext.commands import Context

class Commands():  
  async def exit(self, ctx: Context):
    if not await ctx.bot.is_owner(ctx.author):
      return await ctx.send(f"I'm sorry {ctx.author.mention}, I'm afraid I can't do that")
    await ctx.message.delete()
    return await ctx.bot.logout();
  
  async def download(self, ctx: Context, url: str):
    file: bytes = urllib.request.urlopen(url).read()
    await ctx.message.delete()
    return await ctx.author.send(
      content=f"{ctx.author.mention} Your file",
      file=File(
        file,
        url
      )
    )