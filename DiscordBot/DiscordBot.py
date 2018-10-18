import os
from dotenv import load_dotenv
from pathlib import Path
from discord.ext.commands import Bot, Command
from .Commands import Commands

class DiscordBot(Bot):
  '''DiscrodBot class that implements the Bot class
  '''

  token: str
  client_id: int
  perms: int

  def __init__(self, env_filename:str = ".env"):
    '''Initializing the bot.
    
    Keyword Arguments:
      env_filename {str} -- Filename of the enviroment file to use. (default: {".env"})
    '''

    self.load_envs(env_filename)
    super().__init__(self.command_prefix)
    self.load_commands()
  
  def load_envs(self, env_filename:str = ".env"):
    '''Loading values from the enviroment file.
    
    Keyword Arguments:
      env_filename {str} -- Filename of the enviroment file to use. (default: {".env"})
    '''

    env_path = Path('.') / env_filename
    load_dotenv(dotenv_path=env_path)
    self.token = self.env("BOT_TOKEN")
    self.client_id = self.env("CLIENT_ID")
    self.perms = self.env("PERMISSIONS")
    self.command_prefix = self.env("COMMAND_PREFIX")
  
  def env(self, env_name: str) -> str:
    '''Loads enviroment value that has given name.
    
    Arguments:
      env_name {str} -- Name of the enviroment value to load.
    
    Returns:
      str -- Enviroment value for the given name.
    '''
    return os.getenv(env_name)

  def load_commands(self):
    '''Load commands from the Commands class.
    '''

    cmds = Commands()
    for cmd in  [func for func in dir(cmds) if callable(getattr(cmds, func)) and not func.startswith("__")]:
        self.add_command(Command(cmd, getattr(cmds, cmd)))

  def run(self):
    '''Starts up the bot with the token.
    '''

    super().run(self.token)
  
  async def on_ready(self):
    '''Informing the operator that the bot is ready and printing some information.
    '''

    print('Logged in as')
    print(self.user.name)
    print(self.user.id)
    print('------')
    print(f"Auth URL: https://discordapp.com/oauth2/authorize?client_id={self.client_id}&scope=bot&permissions={self.perms}")
    print('------')
    print('COMMANDS:')
    for cmd in self.commands:
      print(f'\t{self.command_prefix}{cmd.name}')