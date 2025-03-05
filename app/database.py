from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import psycopg2

from . config import settings

SQL_DATABASE_URL = (
    f'postgresql://{settings.database_username}:'
    f'{settings.database_password}@'
    f'{settings.database_hostname}:'
    f'{settings.database_port}/'
    f'{settings.database_name}'
)



SQL_DATABASE_URL=f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'
engine = create_engine(SQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush=False,bind = engine)
Base = declarative_base()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# #DATABASE CONNECTION
# while True:
#    try:
#       conn = psycopg2.connect(host = settings.database_hostname,database=settings.database_name,user=settings.database_username,password=settings.database_password)
#       cursor =conn.cursor()
#       print("Database successfully connected!")
#       break
#    except Exception as error:
#       error = "Failed to connect to the database"
#       print(error)
