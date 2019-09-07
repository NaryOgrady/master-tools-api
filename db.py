from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TravelEvent(Base):
    __tablename__ = 'travel-events'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    def __repr(self):
        return self.description


def get_session():
    engine = create_engine('mysql://root:test@127.0.0.1:3306/master-tools')
    Session = sessionmaker(bind=engine)
    return Session()
