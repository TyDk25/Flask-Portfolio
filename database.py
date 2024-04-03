from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///responses.db', echo=True)

Base = declarative_base()
class Response(Base):
    __tablename__ = "responses"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    subject = Column(String)
    message = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
