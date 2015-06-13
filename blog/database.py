from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from blog import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
Base.query = db_session.query_property()