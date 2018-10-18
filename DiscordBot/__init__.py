import sys
from .DiscordBot import DiscordBot

def main():
  try:
    mBot: DiscordBot
    mBot = DiscordBot()
    mBot.run()
  except:
    print("Unexpected error:", sys.exc_info()[0])
    raise