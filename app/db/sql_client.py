from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

DB_NAME = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_PORT = os.environ.get("POSTGRES_PORT")

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Bright#1270@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class SQLDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            database=DB_NAME,
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )

    def execute_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()


sql_client = SQLDB()
