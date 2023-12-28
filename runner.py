import discord
import pandas as pd
from discord import Intents  
from discord.ext import commands 

intents = discord.Intents.default()
intents.message_content = True 
intents.guilds = True 

client = commands.Bot(command_prefix="!", intents=intents)

movies_df = pd.read_csv("movies_metadata.csv")
print(movies_df.head())
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.command()
async def recommend(ctx, genre):
    try:
        recommended_movies = movies_df[
            movies_df['genres'].apply(lambda x: genre in [genre_dict['name'] for genre_dict in eval(x)])] \
            .sort_values(by='vote_count', ascending=False) \
            .head(5)


        response = f"**Here are some highly-rated movies in the {genre} genre:**\n\n"
        for index, row in recommended_movies.iterrows():
            response += f"• **{row['title']}** ({row['vote_average']} stars on IMDb) - {row['overview']}\n"
            response += f"   {row['poster_path']}\n\n"  

 
        await ctx.send(response)

    except (ValueError, KeyError) as e:
        await ctx.send(f"Error: Could not process recommendation. Please check the genre name and dataset format.")

client.run("MTE4ODU0NDg2MjQwOTIwNzgzOA.Ggec2k.T9ZxqmfC0rCZjWkutNNtQt4qX0QRlha8qcdcVw")