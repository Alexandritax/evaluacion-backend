from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DBURL=os.getenv("DBURL")
DBTABLE=os.getenv("DBTABLE")
DATABASE_URL = "mysql+pymysql://"+USER+":"+PASSWORD+"@"+DBURL+"/"+DBTABLE
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()