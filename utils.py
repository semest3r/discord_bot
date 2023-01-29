from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

class Env(BaseSettings):
    DISCORD_TOKEN:str
    DISCORD_GUILD:str
    ENGINE_DB:str
    HOSTNAME_DB:str
    PORT_DB:str
    USERNAME_DB:str
    #PASSWORD_DB:str
    NAME_DB:str
    ID_GUILD:int

    class Config:
        env_file = ".env"

env = Env()

engine = create_engine(f'{env.ENGINE_DB}://{env.USERNAME_DB}:@{env.HOSTNAME_DB}/{env.NAME_DB}')

Base = declarative_base()