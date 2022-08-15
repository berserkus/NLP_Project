import pymysql
import sqlalchemy as alch
import dotenv
import os

dotenv.load_dotenv()
pass_w=os.getenv("sql_password")
dbName="news"

connectionData=f"mysql+pymysql://root:{pass_w}@localhost/{dbName}"
engine = alch.create_engine(connectionData)