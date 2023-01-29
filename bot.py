# bot.py
import random
import discord
import json
from sqlalchemy import select
from sqlalchemy.orm import Session, declarative_base
from models import database, schemas
from utils import env, engine, Base
from typing import List
Base.metadata.create_all(bind=engine)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = discord.app_commands.CommandTree(client)


@client.event
async def on_ready():
    await bot.sync(guild=discord.Object(id=env.ID_GUILD))
    print("Ready!")

@bot.command(name="register", description="Register Member", guild=discord.Object(id=env.ID_GUILD))
async def test(interaction, user:str, address:str, start_point:str):
    with Session(engine) as session:
        query = select(database.User).filter_by(username=user)
        user_id = session.scalars(query).first()
        if user_id:
            return await interaction.response.send_message("User Already Registered")
        session.add(database.User(username=user, address=address, total_point=start_point))
        session.commit()

    await interaction.response.send_message(f"Registrasi {user} Sukses")
    print("berhasil")

@bot.command(name="add_point", description="Add Point", guild=discord.Object(id=env.ID_GUILD))
async def test(interaction, user:str, addpoint:int):
    with Session(engine) as session:
        query = select(database.User).filter(database.User.address==user)
        user_id = session.scalars(query).first()
        if not user_id:
            return await interaction.response.send_message("User Not Found")
        session.add(database.AddPoint(add_point=addpoint, user_id=user_id.pk))
        session.commit()

    await interaction.response.send_message(f"Add Point Sukses")
    print("berhasil")

@bot.command(name="remove_point", description="Remove Point", guild=discord.Object(id=env.ID_GUILD))
async def test(interaction, user:str, removepoint:int):
    with Session(engine) as session:
        query = select(database.User).filter(database.User.address==user)
        user_id = session.scalars(query).first()
        if not user_id:
            return await interaction.response.send_message("User Not Found")
        session.add(database.RemovePoint(remove_point=removepoint, user_id=user_id.pk))
        session.commit()

    await interaction.response.send_message(f"Remove Point Sukses")
    print("berhasil")
#@client.event
#async def on_reaction_add(reaction, user):
#        await reaction.message.channel.send(f'{user.name} Is Adding Reaction')


client.run(f'{env.DISCORD_TOKEN}') 