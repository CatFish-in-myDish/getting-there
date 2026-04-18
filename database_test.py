import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_database():
    try:
        return psycopg2.connect(
            database=os.environ.get("database_name"),
            user=os.environ.get("database_username"),
            password=os.environ.get("database_password"),
            host=os.environ.get("database_host"),
            port=os.environ.get("database_port")
        )
    except:
        raise Exception("couldn't login to the database, try again")

connect_to_database()