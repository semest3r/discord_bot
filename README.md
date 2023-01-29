# SHIP WEB

## Database Design
    check diagram.plantuml

## List Slash Command
    /register user:[myuser]example address:@example startpoint:0
    /add_point user:@example add_point:0
    /remove_point user:@example remove_point:0

## Create Virtual Environment
    pythone -m venv env

## install requirement
    pip install -r requirements.txt

## Set Database
    My Version is using mysql for database engine

    create file ".env"

    DISCORD_TOKEN=
    DISCORD_GUILD=
    ENGINE_DB= 
    HOSTNAME_DB=
    PORT_DB=
    USERNAME_DB=
    #PASSWORD_DB=
    NAME_DB=


## RUN UVICORN
    bot.py

## Additional
    Create Trigger in your database to decrease or increase 