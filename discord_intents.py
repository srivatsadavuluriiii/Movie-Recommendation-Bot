import discord
import pandas as pd
from discord import Intents  
from discord.ext import commands 


intents = discord.Intents.default()
intents.message_content = True 
intents.guilds = True 

client = commands.Bot(command_prefix="!", intents=intents)