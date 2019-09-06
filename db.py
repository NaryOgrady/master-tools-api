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


if __name__ == '__main__':
    engine = create_engine('mysql://admin:Therion01@master-tools.c90m93uasd0o.us-east-2.rds.amazonaws.com/master-tools')
    Session = sessionmaker(bind=engine)
    session = Session()
    for event in session.query(TravelEvent).order_by(TravelEvent.id):
        print(event.title)
